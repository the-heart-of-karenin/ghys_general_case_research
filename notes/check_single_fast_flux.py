"""Only the new exterior-algebra identities in note98.

Does not prove Hopf ergodicity, the flow equalities, the quotient geometry,
Grauert base change, or the Dolbeault obstruction theorem. No old suite runs.
"""
from itertools import combinations, permutations
from collections import defaultdict
from math import factorial
from pathlib import Path
import json


class P:
    def __init__(self, values=None):
        self.values = {k: v for k, v in (values or {}).items() if v}

    @staticmethod
    def coerce(value):
        return value if isinstance(value, P) else P({(): value})

    def __add__(self, other):
        out = defaultdict(int, self.values)
        for key, value in self.coerce(other).values.items():
            out[key] += value
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.values.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __mul__(self, other):
        out = defaultdict(int)
        for key, value in self.values.items():
            for second, coefficient in self.coerce(other).values.items():
                out[tuple(sorted(key+second))] += value*coefficient
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        result = P.coerce(1)
        for _ in range(exponent):
            result = result*self
        return result

    def __bool__(self):
        return bool(self.values)

    def __eq__(self, other):
        return self.values == self.coerce(other).values

    def __str__(self):
        return ' + '.join(f'{v}*'+('*'.join(k) or '1')
                          for k, v in sorted(self.values.items())) or '0'


def symbols(names):
    return [P({(name,): 1}) for name in names.split()]

x = [3*i for i in range(4)]
y = [3*i+1 for i in range(4)]
z = [3*i+2 for i in range(4)]
h = symbols('h11 h12 h21 h22')
n = symbols('n11 n12 n21 n22')
d = symbols('d1 d2 d3 d4')


def mul(a, b):
    if set(a) & set(b):
        return None, 0
    sign = (-1)**sum(i > j for i in a for j in b)
    return tuple(sorted(a+b)), sign


def monomial(indices):
    key, sign = (), 1
    for i in indices:
        key, a = mul(key, (i,))
        if not a:
            return None, 0
        sign *= a
    return key, sign


H = [(tuple(sorted((x[i], x[j+2]))), h[2*i+j])
     for i in range(2) for j in range(2)]
B = [(tuple(sorted((y[i], y[j+2]))), n[2*i+j])
     for i in range(2) for j in range(2)]
D = [((y[i], z[i]), d[i]) for i in range(4)]
terms = H+B+D
top = tuple(range(12))


def coefficient(prefix, choices, factor):
    out = P()
    for choice in choices:
        key, sign = monomial(prefix)
        if not sign:
            continue
        c = P.coerce(sign)
        for pair, value in choice:
            key, sign = mul(key, pair)
            if not sign:
                break
            c *= sign*value
        else:
            if key == top:
                out += c*factor
    return out


theta6 = coefficient([], combinations(terms, 6), factorial(6))
expected6 = coefficient([], (hh+tuple(D) for hh in combinations(H, 2)),
                        15*factorial(2)*factorial(4))
assert theta6 == expected6
assert theta6 != 0

pairing = [[P() for _ in range(8)] for _ in range(8)]
for i, a in enumerate(x+y):
    for j, b in enumerate(x+y):
        value = coefficient([a, b], combinations(terms, 5), factorial(5))
        pairing[i][j] = value
        if i < 4 and j < 4:
            expected = coefficient([a, b], ((hh,)+tuple(D) for hh in H),
                                   5*factorial(4))
            assert value == expected
        else:
            assert value == 0

determinant = P()
for perm in permutations(range(4)):
    sign = (-1)**sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
    value = P.coerce(sign)
    for i in range(4):
        value = value*pairing[i][perm[i]]
    determinant = determinant+value
product_d = P.coerce(1)
for value in d:
    product_d = product_d*value
expected_det = (120*product_d)**4*(h[0]*h[3]-h[1]*h[2])**2
assert determinant == expected_det

report = {
    'scope': 'New formal exterior identities only; not a proof certification.',
    'theta_sixth_top_coefficient': str(theta6),
    'theta6_equals_15_H2_D4': True,
    'all_64_Lefschetz_pairing_entries_checked': True,
    'slow_block_zero': True,
    'fast_pairing_determinant': str(determinant),
    'fast_determinant_factorization': '(120*d1*d2*d3*d4)^4*(h11*h22-h12*h21)^2',
    'fast_nondegeneracy_under_nonzero_top_volume': True,
}
Path(__file__).with_name('single_fast_flux_checks.json').write_text(
    json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
