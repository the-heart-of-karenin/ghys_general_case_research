"""Exact finite-dimensional checks newly used in notes 74-76.

Does not prove A'Campo, Franks-Manning, Hopf ergodicity, the L1 arguments,
the compact holomorphic group action, or the torus-bundle reconstruction.
No previous test suite is imported or rerun.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from math import isqrt
from pathlib import Path
import json


def wedge(a, b):
    out = defaultdict(Q)
    for u, v in a.items():
        for w, z in b.items():
            if set(u).intersection(w):
                continue
            sign = (-1) ** sum(i > j for i in u for j in w)
            out[tuple(sorted(u + w))] += sign * v * z
    return {u: v for u, v in out.items() if v}


def add(*forms):
    out = defaultdict(Q)
    for f in forms:
        for u, v in f.items():
            out[u] += v
    return {u: v for u, v in out.items() if v}


def form(*indices):
    out = {(): Q(1)}
    for i in indices:
        out = wedge(out, {(i,): Q(1)})
    return out


x = [3*j for j in range(4)]
y = [3*j+1 for j in range(4)]
z = [3*j+2 for j in range(4)]
H = [form(x[i], x[j+2]) for i, j in product(range(2), repeat=2)]
B = [form(y[i], y[j+2]) for i, j in product(range(2), repeat=2)]
D = [form(y[i], z[i]) for i in range(4)]
basis = H+B+D
assert len(basis) == 12

# Every coefficient of e*a*omega^2*bar(omega)^3 vanishes.
# Conjugation permutes the same 12 supports; distinct simple even factors
# suffice, because any repeated simple factor wedges to zero.
flux_count = 0
for a in y:
    for e in x+y:
        for terms in combinations(range(12), 5):
            value = form(e, a)
            for k in terms:
                value = wedge(value, basis[k])
            assert not value
            flux_count += 1
assert flux_count == 25344

# With at most one central coefficient in omega, omega and its conjugate
# together have at most two z variables. Every possible top coefficient is 0.
conjugate_index = [1, 0, 3, 2]
one_D_top_count = 0
for i in range(4):
    allowed = H+B+[D[j] for j in sorted({i, conjugate_index[i]})]
    for terms in combinations(allowed, 6):
        value = {(): Q(1)}
        for f in terms:
            value = wedge(value, f)
        assert not value
        one_D_top_count += 1

# On the abelian fast-primary kernel, each two-z square coefficient is
# uniquely supplied by the corresponding two D terms, with factor 2.
two_D_coefficients = []
for i, j in combinations(range(4), 2):
    s = add(D[i], D[j], *B)
    value = wedge(s, s)
    key = tuple(sorted([y[i], z[i], y[j], z[j]]))
    assert abs(value[key]) == 2
    two_D_coefficients.append({'i': i+1, 'j': j+1, 'coefficient': int(value[key])})


def zero(n, m=None):
    return [[Q(0) for j in range(m if m is not None else n)] for i in range(n)]


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def ma(a, b):
    return [[u+v for u, v in zip(row, other)] for row, other in zip(a, b)]


def scale(a, c):
    return [[c*u for u in row] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def rank(a):
    a = [list(map(Q, row)) for row in a]
    p = 0
    for j in range(len(a[0])):
        k = next((k for k in range(p, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[p], a[k] = a[k], a[p]
        c = a[p][j]
        a[p] = [v/c for v in a[p]]
        for k in range(len(a)):
            if k != p:
                c = a[k][j]
                a[k] = [v-c*w for v, w in zip(a[k], a[p])]
        p += 1
        if p == len(a):
            break
    return p


# R=Z[i,sqrt(3)], basis 1,i,sqrt(3),i*sqrt(3).
def ring_mul(a, b):
    out = [Q(0)]*4
    for j, u in enumerate(a):
        for k, v in enumerate(b):
            ip, dp = (j % 2)+(k % 2), (j // 2)+(k // 2)
            out[(ip % 2)+2*(dp % 2)] += u*v*((-1)**(ip // 2))*(3**(dp // 2))
    return out


def conjugate(a):
    return [a[0], -a[1], a[2], -a[3]]


def mul_matrix(a):
    columns = [ring_mul(a, row) for row in eye(4)]
    return transpose(columns)


def blockdiag(a, b):
    out = zero(len(a)+len(b))
    for i in range(len(a)):
        for j in range(len(a)):
            out[i][j] = a[i][j]
    for i in range(len(b)):
        for j in range(len(b)):
            out[len(a)+i][len(a)+j] = b[i][j]
    return out


def monodromy(r):
    out = eye(8)
    m = mul_matrix(conjugate(r))
    for i in range(4):
        for j in range(4):
            out[4+i][j] = m[i][j]
    return out


lam = [Q(2), Q(0), Q(1), Q(0)]
laminv = [Q(2), Q(0), Q(-1), Q(0)]
lam2 = ring_mul(lam, lam)
A = blockdiag(mul_matrix(laminv), mul_matrix(lam))
Ainv = blockdiag(mul_matrix(lam), mul_matrix(laminv))
assert mm(A, Ainv) == eye(8)
assert ma(ma(mm(A, A), scale(A, -4)), eye(8)) == zero(8)
values = eye(4)+[[Q(1), Q(-2), Q(3), Q(1)], [Q(-3), Q(1), Q(0), Q(2)]]
for r in values:
    R = monodromy(r)
    N = ma(R, scale(eye(8), -1))
    assert mm(N, N) == zero(8)
    assert mm(mm(A, R), Ainv) == monodromy(ring_mul(lam2, r))
monodromy_additive_count = 0
for r, s in product(eye(4), repeat=2):
    assert mm(monodromy(r), monodromy(s)) == monodromy([u+v for u, v in zip(r, s)])
    monodromy_additive_count += 1
common_fixed_constraints = []
for r in eye(4):
    common_fixed_constraints += ma(transpose(monodromy(r)), scale(eye(8), -1))
assert rank(common_fixed_constraints) == 4
common_fixed_dimension = 8-rank(common_fixed_constraints)

# Noncompact half-power flow: exact squares, no floating point approximation.
def sqrtq(v):
    v = abs(Q(v))
    a, b = isqrt(v.numerator), isqrt(v.denominator)
    assert a*a == v.numerator and b*b == v.denominator
    return Q(a, b)


def local_flow(t, point):
    u, v = point
    return u+t, v+sqrtq(u+t)-sqrtq(u)


def local_F(point):
    u, v = point
    return 16*u, 4*v


local_flow_count = 0
for a, b, c in product(range(4), repeat=3):
    point = (Q(a*a), Q(2))
    s, t = Q(b*b-a*a), Q(c*c-b*b)
    assert local_flow(t, local_flow(s, point)) == local_flow(s+t, point)
    assert local_F(local_flow(s, point)) == local_flow(16*s, local_F(point))
    local_flow_count += 1
assert local_flow(Q(1), (Q(0), Q(0))) == (Q(1), Q(1))

# z^k has a k-point local Milnor fibre with cyclic permutation: Lefschetz=0.
local_monodromies = []
for k in range(2, 7):
    permutation = [[int(i == (j+1) % k) for j in range(k)] for i in range(k)]
    trace = sum(permutation[i][i] for i in range(k))
    assert trace == 0
    local_monodromies.append({'k': k, 'H0_dimension': k, 'Lefschetz_number': trace})

result = {
    'status': 'passed',
    'scope': 'Only new finite-dimensional identities for notes 74-76; no global theorem proved by this script.',
    'flux_support_coefficients_checked': flux_count,
    'one_D_top_supports_checked': one_D_top_count,
    'two_D_square_coefficients': two_D_coefficients,
    'exact_ring_monodromy_normalizations': len(values),
    'monodromy_group_law_checks': monodromy_additive_count,
    'common_fixed_H1_dimension_real': common_fixed_dimension,
    'fiber_linearization_minimal_polynomial': 't^2-4t+1',
    'noncompact_half_power_flow_checks': local_flow_count,
    'local_Milnor_monodromies': local_monodromies,
}
path = Path(__file__).with_name('slow_form_reduction_checks.json')
path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False))
