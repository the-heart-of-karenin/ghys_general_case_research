"""Exact algebra checks for notes 61-63.

This verifies finite-dimensional identities, not the global Dolbeault theorem,
the gauge argument, convergence of a formal conjugacy, or novelty.
No optional symbolic algebra dependency is used.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
import random


class P:
    """Sparse polynomial over Q; monomials are sorted tuples of names."""
    def __init__(self, terms=None):
        self.terms = {k: Q(v) for k, v in (terms or {}).items() if v}

    @staticmethod
    def coerce(value):
        return value if isinstance(value, P) else P({(): value})

    def __add__(self, other):
        out = defaultdict(Q, self.terms)
        for key, value in self.coerce(other).terms.items():
            out[key] += value
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        out = defaultdict(Q)
        for key, value in self.terms.items():
            for other_key, other_value in self.coerce(other).terms.items():
                out[tuple(sorted(key + other_key))] += value * other_value
        return P(out)

    __rmul__ = __mul__

    def __bool__(self):
        return bool(self.terms)

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms

    def __str__(self):
        return ' + '.join(f'{v}*' + ('*'.join(k) or '1')
                          for k, v in sorted(self.terms.items())) or '0'


def var(name):
    return P({(name,): 1})


def clean(form):
    return {k: P.coerce(v) for k, v in form.items() if v}


def add(*forms):
    out = defaultdict(P)
    for form in forms:
        for key, value in form.items():
            out[key] += value
    return clean(out)


def scale(form, value):
    return clean({key: value * coefficient for key, coefficient in form.items()})


def wedge(left, right):
    out = defaultdict(P)
    for key, coefficient in left.items():
        for other, other_coefficient in right.items():
            if set(key).intersection(other):
                continue
            inversions = sum(i > j for i in key for j in other)
            out[tuple(sorted(key + other))] += ((-1) ** inversions
                                               * coefficient * other_coefficient)
    return clean(out)


def d(form):
    out = {}
    for key, coefficient in form.items():
        for place, index in enumerate(key):
            part = wedge(wedge({key[:place]: P.coerce(1)}, derivatives[index]),
                         {key[place + 1:]: P.coerce(1)})
            out = add(out, scale(part, (-1) ** place * coefficient))
    return out


def rank(rows, columns):
    rows = [[Q(value) for value in row] for row in rows]
    k = 0
    for j in range(columns):
        pivot = next((i for i in range(k, len(rows)) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[k], rows[pivot] = rows[pivot], rows[k]
        z = rows[k][j]
        rows[k] = [value / z for value in rows[k]]
        for i in range(len(rows)):
            if i != k and rows[i][j]:
                z = rows[i][j]
                rows[i] = [value - z * other for value, other in zip(rows[i], rows[k])]
        k += 1
    return k


names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta']
vector_names = ['X', 'Y', 'Z', 'A', 'B', 'C']
weights = [2, -1, 1, -2, 1, -1]
one = [{(j,): P.coerce(1)} for j in range(12)]
derivatives = [{} for j in range(12)]
derivatives[2] = {(1, 6): P.coerce(1)}
derivatives[5] = {(4, 9): P.coerce(1)}
derivatives[8] = {(0, 7): P.coerce(-1)}
derivatives[11] = {(3, 10): P.coerce(-1)}
assert all(not d(d(form)) for form in one)

# Complexified tangent brackets, independently dual to the exterior derivative.
structure = {(6, 1): {2: 1}, (0, 7): {8: 1},
             (9, 4): {5: 1}, (3, 10): {11: 1}}
structure.update({(b, a): {k: -v for k, v in value.items()}
                  for (a, b), value in list(structure.items())})
for (i, j), value in structure.items():
    for k, derivative in enumerate(derivatives):
        sign = 1 if i < j else -1
        assert sign * derivative.get(tuple(sorted((i, j))), P()) == -value.get(k, 0)


def bracket(left, right):
    out = defaultdict(P)
    for i, coefficient in left.items():
        for j, other in right.items():
            for k, value in structure.get((i, j), {}).items():
                out[k] += value * coefficient * other
    return clean(out)


# All invariant (0,*) forms are D-closed, and D Y=baralpha Z,
# D B=bardelta C. Derive D from the brackets rather than hard-code its ranks.
Dvector = [dict() for j in range(6)]
for j in range(6):
    for i in range(6):
        for k, coefficient in structure.get((i + 6, j), {}).items():
            if k < 6:
                Dvector[j][((i,), k)] = coefficient
assert Dvector[1] == {((0,), 2): 1}
assert Dvector[4] == {((3,), 5): 1}


def dolbeault_basis(q):
    return [(bars, target) for bars in combinations(range(6), q) for target in range(6)]


def dolbeault_column(bars, target):
    out = defaultdict(Q)
    for (new_bars, new_target), coefficient in Dvector[target].items():
        j = new_bars[0]
        if j in bars:
            continue
        inversions = sum(i > j for i in bars)
        out[(tuple(sorted(bars + (j,))), new_target)] += ((-1) ** (len(bars) + inversions)
                                                        * coefficient)
    return {key: value for key, value in out.items() if value}


def dolbeault_rank(q, fixed_only=False):
    source = dolbeault_basis(q)
    target = dolbeault_basis(q + 1)
    if fixed_only:
        source = [(bars, j) for bars, j in source
                  if sum(weights[i] for i in bars) == weights[j]]
        target = [(bars, j) for bars, j in target
                  if sum(weights[i] for i in bars) == weights[j]]
    columns = [dolbeault_column(bars, j) for bars, j in source]
    rows = [[col.get(item, 0) for col in columns] for item in target]
    return len(source), rank(rows, len(source))


dim0, rank0 = dolbeault_rank(0)
dim1, rank1 = dolbeault_rank(1)
fixed_dim0, fixed_rank0 = dolbeault_rank(0, True)
fixed_dim1, fixed_rank1 = dolbeault_rank(1, True)
assert (dim0, rank0, dim1, rank1) == (6, 2, 36, 10)
assert (fixed_dim0, fixed_rank0, fixed_dim1, fixed_rank1) == (0, 0, 10, 4)
fixed_closed = [(bars, j) for bars, j in dolbeault_basis(1)
                if sum(weights[i] for i in bars) == weights[j]
                and not dolbeault_column(bars, j)]
assert fixed_closed == [((0,), 0), ((1,), 5), ((2,), 2),
                        ((3,), 3), ((4,), 2), ((5,), 5)]

xi, eta, p, r, q, s, u, v, w, t = map(var, 'xi eta p r q s u v w t'.split())
graph = [{6: 1, 0: xi}, {9: 1, 3: eta},
         {8: 1, 2: p, 4: r}, {10: 1, 2: q, 4: s},
         {7: 1, 1: u, 5: v}, {11: 1, 1: w, 5: t}]
graph = [clean(row) for row in graph]
graph_labels = ['U', 'V', 'P', 'Q', 'R', 'S']
by_bar = {next(k for k in row if k >= 6): row for row in graph}
remainders = {}
for i, j in combinations(range(6), 2):
    value = bracket(graph[i], graph[j])
    remainder = dict(value)
    for k, coefficient in value.items():
        if k >= 6:
            remainder = add(remainder, scale(by_bar[k], -coefficient))
    if remainder:
        remainders[graph_labels[i] + graph_labels[j]] = remainder
assert remainders == {'UR': {2: u - xi * p, 4: -xi * r},
                      'US': {2: w}, 'VP': {5: r},
                      'VQ': {5: s - eta * t, 1: -eta * w}}

# Coframe after integrability: r=w=0, u=xi*p, s=eta*t.
theta = [add(one[0], scale(one[6], -xi)),
         add(one[1], scale(one[7], -xi * p)),
         add(one[2], scale(one[8], -p), scale(one[10], -q)),
         add(one[3], scale(one[9], -eta)),
         add(one[4], scale(one[10], -eta * t)),
         add(one[5], scale(one[7], -v), scale(one[11], -t))]
K, L, M, N, O = map(var, 'K L M N O'.split())


def symplectic_form(coframe, coeffs):
    a, b, c, e, f, g = coframe
    k, ell, m, n, o = coeffs
    return add(scale(wedge(a, e), k), scale(wedge(c, b), ell),
               scale(wedge(c, g), m), scale(wedge(f, b), n),
               scale(wedge(g, f), o))


omega = symplectic_form(theta, (K, L, M, N, O))
domega = d(omega)
assert domega[(1, 5, 6)] == -M
assert domega[(0, 1, 7)] == -L * p
assert domega[(3, 4, 10)] == -O * t
abstract_omega = symplectic_form(one[:6], (K, L, M, N, O))
cube = wedge(wedge(abstract_omega, abstract_omega), abstract_omega)
assert cube == {(0, 1, 2, 3, 4, 5): 6 * K * (L * O + M * N)}

family_coframe = [add(one[0], scale(one[6], -xi)), one[1],
                  add(one[2], scale(one[10], -q)),
                  add(one[3], scale(one[9], -eta)), one[4],
                  add(one[5], scale(one[7], -v))]
family_omega = symplectic_form(family_coframe, (K, L, 0, N, O))
assert not d(family_omega)
for i, form in enumerate(family_coframe):
    for key in form:
        assert weights[key[0] % 6] == weights[i]

# Closure at first order after the full-pair gauge reduction.
k, ell, m, n, o = map(var, 'k ell m n o'.split())
eta_form = symplectic_form(one[:6], (k, ell, m, n, o))
eta_form = add(eta_form, scale(wedge(one[6], one[3]), -xi),
               scale(wedge(one[0], one[9]), -eta),
               scale(wedge(one[8], one[1]), -p),
               scale(wedge(one[10], one[1]), -q),
               scale(wedge(one[7], one[4]), -v),
               scale(wedge(one[11], one[4]), -t))
deta_form = d(eta_form)
linear_parameters = 'xi eta p q v t k ell m n o'.split()
linear_rows = [[coefficient.terms.get((name,), 0) for name in linear_parameters]
               for coefficient in deta_form.values()]
assert rank(linear_rows, len(linear_parameters)) == 3
assert deta_form[(1, 5, 6)] == -m
assert deta_form[(0, 1, 7)] == -p
assert deta_form[(3, 4, 10)] == -t


def bch(left, right):
    return add(left, right, scale(bracket(left, right), Q(1, 2)))


def constant_vector(vector):
    return {j: value.terms.get((), Q(0)) for j, value in vector.items()
            if value.terms.get((), Q(0))}


def first_coefficient(vector, parameter):
    return {j: P.coerce(value.terms.get((parameter,), Q(0)))
            for j, value in vector.items() if value.terms.get((parameter,), Q(0))}


# Independent exact tests of the nonlinear formula used in the elliptic lemma.
# These verify signs and two-step group order, not the elliptic estimate.
random.seed(61263)
tau = var('tau')
center = {2, 5, 8, 11}
Aw = [Q(2) ** j for j in weights + weights]


def apply_A(vector):
    return clean({j: Aw[j] * value for j, value in vector.items()})


def sample():
    return clean({j: Q(random.randint(-4, 4), random.randint(1, 5)) for j in range(12)})


for iteration in range(200):
    uu, VV, kk = sample(), sample(), sample()
    path = bch(bch(scale(uu, -1), scale(VV, tau)), add(uu, scale(kk, tau)))
    expected = add(VV, kk, scale(bracket(uu, VV), -1),
                   scale(bracket(uu, kk), Q(-1, 2)))
    assert first_coefficient(path, 'tau') == expected

    values = [sample() for j in range(4)]
    average = scale(add(*values), Q(1, 4))
    residual = [bch(value, scale(average, -1)) for value in values]
    assert not add(*residual)
    assert all(bch(value, average) == original for value, original in zip(residual, values))

    bb = sample()
    bq = constant_vector(bb)
    cv = {j: P.coerce(Aw[j] * value / (1 - Aw[j]))
          for j, value in bq.items() if j not in center}
    correction = scale(bracket(apply_A(cv), apply_A(bb)), Q(1, 2))
    cc = dict(cv)
    for j in center:
        value = (Aw[j] * bb.get(j, P()) + correction.get(j, P()))
        cc[j] = value * (1 / (1 - Aw[j]))
    cc = clean(cc)
    assert bch(apply_A(cc), apply_A(bb)) == cc
    gg = sample()
    conjugated = bch(apply_A(bch(bch(gg, cc), bb)), scale(cc, -1))
    assert conjugated == apply_A(gg)

result = {
    'purpose': 'Exact finite-dimensional identities for notes 61-63; not a global proof or convergence/novelty test.',
    'complex_dimension_of_model': 6,
    'weights': weights,
    'dolbeault': {'dim_C0': dim0, 'rank_D0': rank0, 'dim_C1': dim1,
                  'rank_D1': rank1, 'h0': dim0 - rank0,
                  'h1': dim1 - rank1 - rank0,
                  'fixed_C0': fixed_dim0, 'fixed_C1': fixed_dim1,
                  'fixed_D1_rank': fixed_rank1, 'fixed_H1': 6,
                  'fixed_H1_representatives': [f'bar{names[bars[0]]} tensor {vector_names[j]}'
                                               for bars, j in fixed_closed]},
    'graph_integrability_remainders': {label: {vector_names[j]: str(value)
                                                for j, value in row.items()}
                                      for label, row in remainders.items()},
    'integrable_fixed_F_complex_structure_parameters': ['xi', 'eta', 'p', 'q', 'v', 't'],
    'closure_isolating_coefficients': {str(key): str(domega[key])
                                      for key in [(1, 5, 6), (0, 1, 7), (3, 4, 10)]},
    'abstract_symplectic_cube_coefficient': str(cube[(0, 1, 2, 3, 4, 5)]),
    'fixed_F_symplectic_triple_parameters': ['xi', 'eta', 'q', 'v', 'K', 'L', 'N', 'O'],
    'family_closed_identically': not d(family_omega),
    'linearized_form_closure_rank': 3,
    'linearized_general_triple_dimension_after_gauge': 8,
    'two_step_Maurer_Cartan_differential_exact_tests': 200,
    'zero_mean_factorization_exact_tests': 200,
    'right_translation_conjugacy_exact_tests': 200,
    'elliptic_estimate_proved_in_note_62_not_tested_numerically': True,
    'all_assertions_passed': True,
}
out_path = Path(__file__).with_name('six_dimensional_model_deformation_checks.json')
out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
