"""Exact new checks for notes 65-68, not old-test repetition or analytic proofs."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import factorial
from pathlib import Path
import json
import random


def zero(n):
    return [[Q(0) for j in range(n)] for i in range(n)]


def identity(n):
    a = zero(n)
    for i in range(n):
        a[i][i] = Q(1)
    return a


def ma(*matrices):
    n = len(matrices[0])
    return [[sum(a[i][j] for a in matrices) for j in range(n)] for i in range(n)]


def ms(a, c):
    return [[c * value for value in row] for row in a]


def mm(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def comm(a, b):
    return ma(mm(a, b), ms(mm(b, a), -1))


def exp_nil(a):
    n = len(a)
    value = identity(n)
    power = identity(n)
    for j in range(1, n):
        power = mm(power, a)
        value = ma(value, ms(power, Q(1, factorial(j))))
    return value


def log_nil(a):
    n = len(a)
    delta = ma(a, ms(identity(n), -1))
    power = identity(n)
    value = zero(n)
    for j in range(1, n):
        power = mm(power, delta)
        value = ma(value, ms(power, Q((-1) ** (j + 1), j)))
    return value


def exp_derivative(a, k):
    n = len(a)
    p, dp = identity(n), zero(n)
    value = zero(n)
    for j in range(1, n):
        p, dp = mm(p, a), ma(mm(dp, a), mm(p, k))
        value = ma(value, ms(dp, Q(1, factorial(j))))
    return value


def sample(n):
    a = zero(n)
    for i, j in combinations(range(n), 2):
        a[i][j] = Q(random.randint(-3, 3), random.randint(1, 5))
    return a


random.seed(650066)
high_step_checks = {}
for size in (4, 5):
    for trial in range(40):
        u, v, k = sample(size), sample(size), sample(size)
        left = mm(exp_nil(ms(u, -1)), ma(mm(v, exp_nil(u)), exp_derivative(u, k)))
        rhs = zero(size)
        av, ak = v, k
        for j in range(size):
            rhs = ma(rhs, ms(av, Q((-1) ** j, factorial(j))),
                     ms(ak, Q((-1) ** j, factorial(j + 1))))
            av, ak = comm(u, av), comm(u, ak)
        assert left == rhs
    high_step_checks[f'UT_{size}_nilpotency_step_{size-1}'] = 40

# The two-step mean formula is false at step three, with an explicit correction.
x, y = zero(4), zero(4)
x[0][1] = 1
y[1][2] = y[2][3] = 1
mean = ms(ma(x, y), Q(1, 2))


def residual_average(a):
    logs = [log_nil(mm(exp_nil(u), exp_nil(ms(a, -1)))) for u in (x, y)]
    return ms(ma(*logs), Q(1, 2))


residual = residual_average(mean)
expected = zero(4)
expected[0][3] = Q(-1, 48)
assert residual == expected
corrected = ma(mean, residual)
assert residual_average(corrected) == zero(4)


def clean(form):
    return {key: Q(value) for key, value in form.items() if value}


def fa(*forms):
    out = defaultdict(Q)
    for form in forms:
        for key, value in form.items():
            out[key] += value
    return clean(out)


def fs(form, value):
    return clean({key: value * coefficient for key, coefficient in form.items()})


def wedge(a, b):
    out = defaultdict(Q)
    for key, value in a.items():
        for other, coefficient in b.items():
            if set(key) & set(other):
                continue
            sign = (-1) ** sum(i > j for i in key for j in other)
            out[tuple(sorted(key + other))] += sign * value * coefficient
    return clean(out)


def differential(form, derivatives):
    out = {}
    for key, value in form.items():
        for j, index in enumerate(key):
            term = wedge(wedge({key[:j]: 1}, derivatives[index]), {key[j+1:]: 1})
            out = fa(out, fs(term, value * (-1) ** j))
    return out


def rank(rows, cols):
    a = [[Q(value) for value in row] for row in rows]
    k = 0
    for j in range(cols):
        p = next((i for i in range(k, len(a)) if a[i][j]), None)
        if p is None:
            continue
        a[k], a[p] = a[p], a[k]
        v = a[k][j]
        a[k] = [x/v for x in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j]:
                v = a[i][j]
                a[i] = [x-v*y for x, y in zip(a[i], a[k])]
        k += 1
    return k


weights = [2, -1, 1, -2, 1, -1] * 2
one = [{(j,): Q(1)} for j in range(12)]
derivatives = [{} for j in range(12)]
derivatives[2] = {(1, 6): 1}
derivatives[5] = {(4, 9): 1}
derivatives[8] = {(0, 7): -1}
derivatives[11] = {(3, 10): -1}
two = list(combinations(range(12), 2))
three = list(combinations(range(12), 3))
fixed_two = [key for key in two if sum(weights[j] for j in key) == 0]
fixed_d = [differential({key: 1}, derivatives) for key in fixed_two]
rank_fixed_d = rank([[col.get(key, 0) for col in fixed_d] for key in three], len(fixed_two))
fixed_closed_dim = len(fixed_two) - rank_fixed_d
assert len(fixed_two) == 20 and fixed_closed_dim == 12
assert all(weights[j] != 0 for j in range(12))
# No invariant exact two-form: im d(C1) has only the nonzero C1 weights.
assert all(sum(weights[j] for j in key) == weights[i]
           for i, derivative in enumerate(derivatives) for key in derivative)

# A genuine non-abelian complex-parallelisable base on the original compact model.
sharp = fa(wedge(one[6], one[9]), wedge(one[2], one[1]), wedge(one[5], one[4]))
assert not differential(sharp, derivatives)
sharp_holomorphic_indices = {6, 1, 2, 9, 4, 5}
assert all(set(key) <= sharp_holomorphic_indices for key in sharp)
assert all(sum(weights[j] for j in key) == 0 for key in sharp)


def power(form, k):
    value = {(): Q(1)}
    for j in range(k):
        value = wedge(value, form)
    return value


assert power(sharp, 3)
assert not power(sharp, 4)

# A sampled period form: kernel dimension and the pointwise period conditions.
xi, eta, q, v = Q(1, 5), Q(-1, 4), Q(1, 7), Q(1, 9)
theta = [fa(one[0], fs(one[6], -xi)), one[1], fa(one[2], fs(one[10], -q)),
         fa(one[3], fs(one[9], -eta)), one[4], fa(one[5], fs(one[7], -v))]
omega = fa(fs(wedge(theta[0], theta[3]), 2), fs(wedge(theta[2], theta[1]), 3),
           fs(wedge(theta[4], theta[1]), Q(1, 2)), fs(wedge(theta[5], theta[4]), 5))
assert not differential(omega, derivatives)
assert not power(omega, 4)
bar = {}
for key, value in omega.items():
    mapped = tuple((i+6) % 12 for i in key)
    sign = (-1) ** sum(mapped[i] > mapped[j] for i in range(2) for j in range(i+1, 2))
    bar[tuple(sorted(mapped))] = sign * value
volume = wedge(power(omega, 3), power(bar, 3))
assert volume and len(volume) == 1
matrix = [[Q(0) for j in range(12)] for i in range(12)]
for (i, j), value in omega.items():
    matrix[i][j], matrix[j][i] = value, -value
assert rank(matrix, 12) == 6

# A Jordan-block CE algebra test, not asserted to carry an invariant lattice.
# [e1,e2]=e3, A(e1)=2e1, A(e2)=e1+2e2, A(e3)=4e3, A(e4)=e4/2.
dim = 4
der = [{}, {}, {(0, 1): -1}, {}]
T1 = [[Q(0) for j in range(dim)] for i in range(dim)]
for i, value in enumerate([2, 2, 4, Q(1, 2)]):
    T1[i][i] = value
T1[1][0] = 1
basis2, basis3 = list(combinations(range(dim), 2)), list(combinations(range(dim), 3))
t_one = [{(i,): T1[i][j] for i in range(dim) if T1[i][j]} for j in range(dim)]
t_two = [wedge(t_one[i], t_one[j]) for i, j in basis2]
d1 = [differential({(j,): 1}, der) for j in range(dim)]
d2 = [differential({key: 1}, der) for key in basis2]
for j in range(dim):
    left = differential(t_one[j], der)
    right = {}
    for (a, b), value in der[j].items():
        right = fa(right, fs(wedge(t_one[a], t_one[b]), value))
    assert left == right
delta = [[t_two[j].get(key, 0) - (1 if i == j else 0)
          for j in range(len(basis2))] for i, key in enumerate(basis2)]
closed_rows = [[col.get(key, 0) for col in d2] for key in basis3]
fixed_Z_dim = len(basis2) - rank(closed_rows + delta, len(basis2))
block = [row + [Q(0)]*dim for row in closed_rows]
for i, key in enumerate(basis2):
    block.append(delta[i] + [-col.get(key, 0) for col in d1])
fixed_H_dim = len(basis2) - rank(block, len(basis2)+dim)
assert fixed_Z_dim == fixed_H_dim == 1

result = dict(
    purpose='Only new finite-dimensional identities; no numerical test claims to prove elliptic compactness, closedness, or external preprint results.',
    arbitrary_step_Maurer_Cartan_checks=high_step_checks,
    three_step_naive_mean_residual_entry_14=str(residual[0][3]),
    three_step_central_correction_succeeds=True,
    six_dimensional_model=dict(fixed_C2=20, fixed_closed_C2=12,
                               fixed_exact_C2=0, fixed_H2_dimension=12,
                               nonabelian_sharp_base_closed_symplectic=True,
                               sample_period_form_rank=6, sample_period_top_volume=str(next(iter(volume.values())))),
    nonsemisimple_algebra_test=dict(fixed_Z2=1, fixed_H2=1,
                                   invariant_lattice_not_asserted=True),
    all_assertions_passed=True,
)
Path(__file__).with_name('nil_period_progression_checks.json').write_text(
    json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
