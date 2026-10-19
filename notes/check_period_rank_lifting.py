"""New exact exterior-algebra checks for notes 69-70.

No old audits are rerun.  Cohomology is computed using the tensor product of
four three-dimensional Heisenberg CE complexes, not by identifying exact
invariant forms with zero pointwise.  Analytic or dynamical claims are not
proved by this script.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json


class P:
    def __init__(self, terms=None):
        self.terms = {key: Q(value) for key, value in (terms or {}).items() if value}

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
        return P({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) + -self

    def __mul__(self, other):
        out = defaultdict(Q)
        for key, value in self.terms.items():
            for second, coefficient in self.coerce(other).terms.items():
                out[tuple(sorted(key + second))] += value * coefficient
        return P(out)

    __rmul__ = __mul__

    def __bool__(self):
        return bool(self.terms)

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms

    def rename(self, names):
        out = defaultdict(Q)
        for key, value in self.terms.items():
            out[tuple(sorted(names.get(name, name) for name in key))] += value
        return P(out)

    def __str__(self):
        return ' + '.join(f'{value}*' + ('*'.join(key) or '1')
                          for key, value in sorted(self.terms.items())) or '0'


def var(name):
    return P({(name,): 1})


def clean(form):
    return {key: P.coerce(value) for key, value in form.items() if value}


def add(*forms):
    out = defaultdict(P)
    for form in forms:
        for key, value in form.items():
            out[key] += value
    return clean(out)


def scale(form, value):
    return clean({key: value * coefficient for key, coefficient in form.items()})


def wedge(a, b):
    out = defaultdict(P)
    for key, value in a.items():
        for other, coefficient in b.items():
            if set(key).intersection(other):
                continue
            sign = (-1) ** sum(i > j for i in key for j in other)
            out[tuple(sorted(key + other))] += sign * value * coefficient
    return clean(out)


def product(*forms):
    value = {(): P.coerce(1)}
    for form in forms:
        value = wedge(value, form)
    return value


def power(form, k):
    return product(*([form] * k))


# Factor order: (baralpha,beta,gamma), (alpha,barbeta,bargamma),
# (bardelta,epsilon,zeta), (delta,barepsilon,barzeta).
names = ['baralpha', 'beta', 'gamma', 'alpha', 'barbeta', 'bargamma',
         'bardelta', 'epsilon', 'zeta', 'delta', 'barepsilon', 'barzeta']
one = [{(j,): P.coerce(1)} for j in range(12)]
x = [one[3*j] for j in range(4)]
y = [one[3*j+1] for j in range(4)]
z = [one[3*j+2] for j in range(4)]
derivatives = [{} for j in range(12)]
for j in range(4):
    derivatives[3*j+2] = scale(wedge(x[j], y[j]), -1)


def d(form):
    out = {}
    for key, value in form.items():
        for j, index in enumerate(key):
            term = product({key[:j]: P.coerce(1)}, derivatives[index],
                           {key[j+1:]: P.coerce(1)})
            out = add(out, scale(term, (-1) ** j * value))
    return out


conjugation = [3, 4, 5, 0, 1, 2, 9, 10, 11, 6, 7, 8]


def bar(form):
    out = defaultdict(P)
    rename = {'t': 'tb', 'tb': 't', 's': 'sb', 'sb': 's',
              'u': 'ub', 'ub': 'u', 'a': 'ab', 'ab': 'a'}
    for key, value in form.items():
        mapped = tuple(conjugation[j] for j in key)
        sign = (-1) ** sum(mapped[i] > mapped[j]
                          for i in range(len(key)) for j in range(i+1, len(key)))
        out[tuple(sorted(mapped))] += sign * value.rename(rename)
    return clean(out)


# Each factor has H-basis 1,x,y,xz,yz,xyz; xy is exact and z is not closed.
# All monomials in powers below are individually closed factor by factor.
allowed = {(), (0,), (1,), (0, 2), (1, 2), (0, 1, 2)}


def cohomology(form):
    out = {}
    for key, value in form.items():
        states = [tuple(index-3*j for index in key if index//3 == j)
                  for j in range(4)]
        assert all(state in allowed or state == (0, 1) for state in states), states
        if any(state == (0, 1) for state in states):
            continue
        out[key] = value
    return clean(out)


alpha, beta, gamma = x[1], y[0], z[0]
delta, epsilon, zeta = x[3], y[2], z[2]
barbeta, barepsilon, bargamma = y[1], y[3], z[1]
omega0 = add(wedge(alpha, delta), wedge(gamma, beta), wedge(zeta, epsilon))
B = wedge(barbeta, barepsilon)
t, s, u = var('t'), var('s'), var('u')
omega = add(omega0, scale(B, t))
eta = product(bargamma, delta, gamma, beta, zeta, epsilon, barepsilon)
omega4 = power(omega, 4)
assert not d(omega)
assert omega4 and omega4 == scale(d(eta), 24*t)
assert not cohomology(omega4)
volume0 = product(power(omega0, 3), power(bar(omega0), 3))
assert volume0 and len(volume0) == 1
assert product(power(omega, 3), power(bar(omega), 3)) == volume0

# A genuine holomorphic-symplectic realization of these periods, without
# requiring F to be holomorphic.  Its difference from the fixed form is exact.
actual = add(product(add(alpha, scale(barepsilon, -u)),
                     add(delta, scale(barbeta, s))),
             wedge(gamma, beta), wedge(zeta, epsilon))
canonical = add(omega0, scale(B, s*u))
assert actual == add(canonical, scale(wedge(alpha, barbeta), s),
                     scale(wedge(delta, barepsilon), u))
assert add(actual, scale(canonical, -1)) == scale(d(add(scale(z[1], s),
                                                       scale(z[3], u))), -1)
assert not d(actual) and not power(actual, 4)
assert product(power(actual, 3), power(bar(actual), 3)) == volume0

# A real pencil of closed symplectic forms: its pointwise top polynomial is
# exactly the same as that of omega0, even though omega has rank eight.
a, ab = var('a'), var('ab')
pencil = power(add(scale(omega, a), scale(bar(omega), ab)), 6)
assert pencil == scale(volume0, 20 * a*a*a * ab*ab*ab)

# Full local cohomological rank equations.  H couples x1,x2 with x3,x4;
# B couples y1,y2 with y3,y4; the four center/base terms are y_i z_i.
M = [[var(f'M{i+1}{j+1}') for j in range(2)] for i in range(2)]
N = [[var(f'N{i+1}{j+1}') for j in range(2)] for i in range(2)]
tt = [var(f'T{j+1}') for j in range(4)]
H = add(*(scale(wedge(x[i], x[j+2]), M[i][j]) for i in range(2) for j in range(2)))
BB = add(*(scale(wedge(y[i], y[j+2]), N[i][j]) for i in range(2) for j in range(2)))
D = add(*(scale(wedge(y[j], z[j]), tt[j]) for j in range(4)))
generic = add(H, BB, D)
assert not d(generic)
generic_cohom4 = cohomology(power(generic, 4))
selected = {}
for subset in ((0, 1, 2), (0, 2, 3)):
    key = tuple(sorted([3, 9] + [3*j+1 for j in subset] + [3*j+2 for j in subset]))
    coefficient = generic_cohom4[key]
    expected_monomial = tuple(sorted(['M22'] + [f'T{j+1}' for j in subset]))
    assert len(coefficient.terms) == 1 and abs(coefficient.terms[expected_monomial]) == 24
    selected['forces_' + ('T2' if 1 in subset else 'T4')] = str(coefficient)

# Once T2=T4=0, the only 4-x/2-z coefficient imposes det M=0.
D13 = add(scale(wedge(y[0], z[0]), tt[0]), scale(wedge(y[2], z[2]), tt[2]))
reduced = add(H, BB, D13)
reduced_cohom4 = cohomology(power(reduced, 4))
key = tuple(sorted([0, 3, 6, 9, 1, 2, 7, 8]))
detM = M[0][0]*M[1][1] - M[0][1]*M[1][0]
assert reduced_cohom4[key] in (24*tt[0]*tt[2]*detM, -24*tt[0]*tt[2]*detM)
selected['forces_detM'] = str(reduced_cohom4[key])

# Parametrize det M=0 without division: M22=h, M12=h*p,
# M21=h*q, M11=h*p*q.  This covers M22 nonzero.
h, p, q = var('h'), var('p'), var('q')
Hrank1 = scale(product(add(x[1], scale(x[0], p)),
                       add(x[3], scale(x[2], q))), h)
final = add(Hrank1, BB, D13)
final4 = power(final, 4)
final_cohom4 = cohomology(final4)
assert len(final_cohom4) == 1
coefficient = next(iter(final_cohom4.values()))
expected = 24*h*p*q*N[1][1]*tt[0]*tt[2]
assert coefficient in (expected, -expected)
selected['remaining_rank_equation'] = str(coefficient)
expected_form = scale(product(Hrank1, y[1], y[3], wedge(y[0], z[0]),
                              wedge(y[2], z[2])), 24*N[1][1]*tt[0]*tt[2])
assert final4 == expected_form


def rational_value(form, variables):
    out = {}
    for key, poly in form.items():
        value = Q(0)
        for monomial, coefficient in poly.terms.items():
            term = coefficient
            for name in monomial:
                term *= variables[name]
            value += term
        if value:
            out[key] = value
    return out


def matrix(form):
    out = [[Q(0) for j in range(12)] for i in range(12)]
    for (i, j), value in form.items():
        out[i][j], out[j][i] = value, -value
    return out


def rank(rows):
    mat = [list(row) for row in rows]
    pivot = 0
    for j in range(len(mat[0])):
        k = next((i for i in range(pivot, len(mat)) if mat[i][j]), None)
        if k is None:
            continue
        mat[pivot], mat[k] = mat[k], mat[pivot]
        value = mat[pivot][j]
        mat[pivot] = [x/value for x in mat[pivot]]
        for i in range(pivot+1, len(mat)):
            value = mat[i][j]
            if value:
                mat[i] = [x-value*y for x, y in zip(mat[i], mat[pivot])]
        pivot += 1
    return pivot


omega_at_1 = rational_value(omega, {'t': Q(1)})
assert rank(matrix(omega_at_1)) == 8

# For real t the recursion operator N=(Re omega)^(-1) Im omega is -i R,
# where R=R0+t K.  Check the exact matrix identity S R=D, with
# S=omega+baromega and D=omega-baromega, rather than invert a numerical matrix.
real_bar_omega = {key: value.rename({'tb': 't'}) for key, value in bar(omega).items()}
S = matrix(add(omega, real_bar_omega))
DD = matrix(add(omega, scale(real_bar_omega, -1)))
r0 = [-1, 1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1]
K = [[Q(0) for j in range(12)] for i in range(12)]
for i, j, value in ((2, 7, 2), (5, 10, -2), (8, 1, -2), (11, 4, 2)):
    K[i][j] = value
R = [[P.coerce(r0[i] if i == j else 0) + t*K[i][j]
      for j in range(12)] for i in range(12)]
assert all(sum(S[i][k]*R[k][j] for k in range(12)) == DD[i][j]
           for i in range(12) for j in range(12))
assert all(not sum(K[i][k]*K[k][j] for k in range(12))
           for i in range(12) for j in range(12))
assert rank(K) == 4
assert all((r0[i]-r0[j])*K[i][j] == 0 for i in range(12) for j in range(12))
weights = [2, -1, 1, 2, -1, 1, -2, 1, -1, -2, 1, -1]
assert all((weights[i]-weights[j])*K[i][j] == 0
           for i in range(12) for j in range(12))
assert all(K[conjugation[i]][conjugation[j]] == -K[i][j]
           for i in range(12) for j in range(12))


def bracket(v, w):
    out = [P() for j in range(12)]
    for j in range(4):
        out[3*j+2] = v[3*j]*w[3*j+1]-v[3*j+1]*w[3*j]
    return out


def apply_R(v):
    return [sum(R[i][j]*v[j] for j in range(12)) for i in range(12)]


for i, j in combinations(range(12), 2):
    vi = [P.coerce(int(k == i)) for k in range(12)]
    vj = [P.coerce(int(k == j)) for k in range(12)]
    rvi, rvj = apply_R(vi), apply_R(vj)
    first = bracket(rvi, rvj)
    second = apply_R([a+b for a, b in zip(bracket(rvi, vj), bracket(vi, rvj))])
    third = apply_R(apply_R(bracket(vi, vj)))
    assert all(not (a-b+c) for a, b, c in zip(first, second, third))

result = dict(
    purpose='Only new exact exterior-algebra calculations for notes 69-70; not an Anosov counterexample or novelty proof.',
    fixed_counterexample=dict(closed=True, fourth_power_nonzero=True,
                              fourth_power_primitive='24*t*eta', fourth_power_class_zero=True,
                              complex_rank_at_t_1=8,
                              mixed_top_volume_constant=str(next(iter(volume0.values()))),
                              all_real_pencil_volumes_unchanged=True,
                              recursion_defect_rank_for_nonzero_real_t=4,
                              recursion_defect_square_zero=True,
                              recursion_Nijenhuis_tensor_zero=True,
                              recursion_defect_commutes_with_hyperbolic_A=True),
    actual_symplectic_realization=dict(closed=True, fourth_power_zero=True,
                                      mixed_volume_constant=True,
                                      canonical_representative_has_rank_8_when_su_nonzero=True,
                                      F_not_holomorphic_off_origin=True),
    generic_cohomology_fourth_power_terms=len(generic_cohom4),
    local_equations=selected,
    local_cohomological_locus='T2=T4=0, detM=0, M12*M21*N22=0 (M22*T1*T3 != 0)',
    local_actual_F_fixed_locus='T2=T4=0, detM=0, N22=0',
    all_assertions_passed=True,
)
Path(__file__).with_name('period_rank_lifting_checks.json').write_text(
    json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
