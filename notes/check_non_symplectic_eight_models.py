"""Exact auxiliary checks for notes108–109; not a substitute for either proof."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def ident(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def add(a, b, scale=F(1)):
    return [[x+scale*y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def tensor(a, b):
    return [[a[i][j]*b[k][l] for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def blocks(*matrices):
    n = sum(len(m) for m in matrices)
    result = [[F(0) for _ in range(n)] for _ in range(n)]
    off = 0
    for mat in matrices:
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                result[off+i][off+j] = F(x)
        off += len(mat)
    return result


def rank(a):
    a = [[F(x) for x in row] for row in a]
    k = 0
    for j in range(len(a[0])):
        p = next((i for i in range(k, len(a)) if a[i][j]), None)
        if p is None:
            continue
        a[k], a[p] = a[p], a[k]
        pivot = a[k][j]
        a[k] = [v/pivot for v in a[k]]
        for i in range(len(a)):
            if i != k:
                c = a[i][j]
                a[i] = [x-c*y for x, y in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k


def det(a):
    a = [[F(x) for x in row] for row in a]
    value = F(1)
    for j in range(len(a)):
        p = next((i for i in range(j, len(a)) if a[i][j]), None)
        if p is None:
            return F(0)
        if p != j:
            a[j], a[p] = a[p], a[j]
            value = -value
        pivot = a[j][j]
        value *= pivot
        for i in range(j+1, len(a)):
            c = a[i][j]/pivot
            a[i] = [x-c*y for x, y in zip(a[i], a[j])]
    return value


def bracket(v, w):
    result = [F(0)]*8
    for i in range(2):
        for j in range(2):
            result[4+2*i+j] = v[i]*w[2+j]-w[i]*v[2+j]
    return result


def nijenhuis(j, v, w):
    terms = [bracket(mv(j, v), mv(j, w)), bracket(v, w),
             mv(j, bracket(mv(j, v), w)), mv(j, bracket(v, mv(j, w)))]
    return [terms[0][i]-terms[1][i]-terms[2][i]-terms[3][i] for i in range(8)]


I2, I8 = ident(2), ident(8)
R = [[F(0), F(-1)], [F(1), F(0)]]
J = blocks(R, R, tensor(R, I2))
basis = ident(8)
checks = {'explicit_J_square_minus_I': mm(J, J) == [[-x for x in row] for row in I8]}
for i, v in enumerate(basis):
    for k, w in enumerate(basis):
        checks[f'explicit_J_Nijenhuis_{i}_{k}'] = nijenhuis(J, v, w) == [0]*8

for p1, p2, q1, q2 in product([-1, 0, 1], repeat=4):
    v = [F(p1), F(p2), F(q1), F(q2)]+[F(0)]*4
    ad = [bracket(v, x)[4:] for x in basis[:4]]
    actual = rank(list(map(list, zip(*ad))))
    p_nonzero, q_nonzero = bool(p1 or p2), bool(q1 or q2)
    expected = 3 if p_nonzero and q_nonzero else (2 if p_nonzero or q_nonzero else 0)
    checks[f'ad_rank_{p1}_{p2}_{q1}_{q2}'] = actual == expected

# A nonintegrable almost complex structure that does not preserve the center.
J_bad = [[F(0) for _ in range(8)] for _ in range(8)]
for i in range(4):
    J_bad[4+i][i] = F(1)
    J_bad[i][4+i] = F(-1)
checks['noncentral_almost_J_square_minus_I'] = mm(J_bad, J_bad) == [[-x for x in row] for row in I8]
checks['noncentral_almost_J_not_integrable'] = any(
    nijenhuis(J_bad, v, w) != [0]*8 for v in basis for w in basis
)

B0 = [[F(2), F(1)], [F(1), F(1)]]
C0 = [[F(3), F(2)], [F(1), F(1)]]
A_integer = blocks(B0, C0, tensor(B0, C0))
B_local = [[F(2)*x for x in row] for row in I2]
C_local = [[F(1, 3)*x for x in row] for row in I2]
A_local = blocks(B_local, C_local, tensor(B_local, C_local))
for label, a in [('integral_Anosov_model', A_integer), ('noncompact_holomorphic_model', A_local)]:
    for i, v in enumerate(basis):
        for k, w in enumerate(basis):
            checks[f'{label}_bracket_{i}_{k}'] = mv(a, bracket(v, w)) == bracket(mv(a, v), mv(a, w))
checks['integral_model_quotient_determinant_one'] = det(B0)*det(C0) == 1
checks['integral_model_total_determinant_one'] = det(A_integer) == 1
checks['integral_model_not_preserving_explicit_J'] = mm(A_integer, J) != mm(J, A_integer)
checks['local_hyperbolic_model_preserves_J'] = mm(A_local, J) == mm(J, A_local)
checks['local_hyperbolic_model_quotient_determinant_4_over_9'] = det(B_local)*det(C_local) == F(4, 9)
checks['local_hyperbolic_model_diagonal_no_unit_modulus'] = all(abs(A_local[i][i]) != 1 for i in range(8))

# Representative cases of the spectral lemma, including real Jordan blocks.
cases = [
    ('distinct_real', [[F(2),0],[0,F(1,2)]], [[F(2),0],[0,F(1,2)]], 'real_unit'),
    ('opposite_sign_real', [[F(2),0],[0,F(-1,2)]], [[F(2),0],[0,F(-1,2)]], 'real_unit'),
    ('repeated_real', B_local, [[F(1,2),0],[0,F(1,2)]], 'real_unit'),
    ('real_Jordan', [[F(2),1],[0,F(2)]], [[F(1,2),0],[0,F(1,2)]], 'real_unit'),
    ('complex_plus_real', [[0,F(-2)],[F(2),0]], [[F(1,2),0],[0,F(1,2)]], 'orthogonal'),
    ('two_nonreal_pairs', [[F(6,5),F(-8,5)],[F(8,5),F(6,5)]],
     [[F(3,10),F(-2,5)],[F(2,5),F(3,10)]], 'orthogonal'),
]
for label, b, c, kind in cases:
    k = tensor(b, c)
    checks[label+'_unit_quotient_determinant'] = abs(det(b)*det(c)) == 1
    if kind == 'real_unit':
        checks[label+'_tensor_unit_eigenvalue'] = det(add(k, ident(4), -1)) == 0 or det(add(k, ident(4))) == 0
    else:
        kt = list(map(list, zip(*k)))
        checks[label+'_tensor_orthogonal'] = mm(kt, k) == ident(4)

assert all(checks.values()), {k:v for k,v in checks.items() if not v}
result = {'scope':'New explicit algebraic checks for note108 only; no finite calculation replaces the universal center or spectral proof.',
          'passed':sum(checks.values()), 'total':len(checks), 'checks':checks}
Path(__file__).with_name('non_symplectic_eight_model_checks.json').write_text(json.dumps(result, indent=2),encoding='utf-8')
print(f"{result['passed']}/{result['total']} exact checks passed.")
