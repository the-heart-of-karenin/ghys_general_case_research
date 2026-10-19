"""Exact new finite-dimensional checks for notes 71-73.

This does not prove Albanese surjectivity, Hartogs extension, freeness of the
global torus action, any external theorem, or the missing lower bound on W.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path
import json


def clean(a):
    return {key: Q(value) for key, value in a.items() if value}


def add(*forms):
    out = defaultdict(Q)
    for form in forms:
        for key, value in form.items():
            out[key] += value
    return clean(out)


def scale(a, c):
    return clean({key: c*value for key, value in a.items()})


def wedge(a, b):
    out = defaultdict(Q)
    for key, value in a.items():
        for second, coefficient in b.items():
            if set(key).intersection(second):
                continue
            sign = (-1)**sum(i > j for i in key for j in second)
            out[tuple(sorted(key+second))] += sign*value*coefficient
    return clean(out)


derivatives = [{} for j in range(12)]
for j in range(4):
    derivatives[3*j+2] = {(3*j, 3*j+1): Q(-1)}


def d(form):
    out = {}
    for key, coefficient in form.items():
        for pos, index in enumerate(key):
            term = wedge(wedge({key[:pos]: 1}, derivatives[index]),
                         {key[pos+1:]: 1})
            out = add(out, scale(term, (-1)**pos*coefficient))
    return out


closed_one_indices = [3*j+k for j in range(4) for k in (0, 1)]
cup_checks = 0
for key in combinations(closed_one_indices, 5):
    j = next(j for j in range(4) if 3*j in key and 3*j+1 in key)
    other = tuple(i for i in key if i not in (3*j, 3*j+1))
    primitive = wedge({(3*j+2,): 1}, {other: 1})
    value = d(primitive)
    assert len(value) == 1 and key in value and abs(value[key]) == 1
    primitive = scale(primitive, 1/value[key])
    assert d(primitive) == {key: Q(1)}
    cup_checks += 1
assert cup_checks == 56

# Quadratic-field arithmetic: coefficients of a+b sqrt(3).
def kmul(u, v):
    a, b = u
    c, e = v
    return a*c+3*b*e, a*e+b*c


lam = (Q(2), Q(1))
laminv = (Q(2), Q(-1))
lam2 = kmul(lam, lam)
assert kmul(lam, laminv) == (Q(1), Q(0))
assert tuple(x-4*y+z for x, y, z in zip(kmul(lam, lam), lam, (Q(1), Q(0)))) == (0, 0)
assert tuple(x-14*y+z for x, y, z in zip(kmul(lam2, lam2), lam2, (Q(1), Q(0)))) == (0, 0)

# All orientation choices are attained by 1,-1,sqrt(3),-sqrt(3).
choices = {(1, 1): (1, 0), (-1, -1): (-1, 0),
           (1, -1): (0, 1), (-1, 1): (0, -1)}
for signs, (a, b) in choices.items():
    actual = (a, a) if b == 0 else (b, -b)
    assert actual == signs
    # Trace(c*u*v), in Q-basis 1,sqrt(3), is an integral nondegenerate block.
    trace_block = [[2*a, 6*b], [6*b, 6*a]]
    assert trace_block[0][0]*trace_block[1][1]-trace_block[0][1]*trace_block[1][0]


def zero(n, m=None):
    return [[Q(0) for j in range(m or n)] for i in range(n)]


def rank(rows):
    a = [list(row) for row in rows]
    piv = 0
    for j in range(len(a[0])):
        k = next((i for i in range(piv, len(a)) if a[i][j]), None)
        if k is None:
            continue
        a[piv], a[k] = a[k], a[piv]
        q = a[piv][j]
        a[piv] = [v/q for v in a[piv]]
        for i in range(piv+1, len(a)):
            q = a[i][j]
            if q:
                a[i] = [v-q*w for v, w in zip(a[i], a[piv])]
        piv += 1
    return piv


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


# The noncompact local critical model, lambda=4.  This value is used only for
# a local exact check and is not asserted to preserve a compact lattice.
J = zero(6)
for j in range(3):
    J[2*j][2*j+1], J[2*j+1][2*j] = 1, -1
growth = [Q(16), Q(1, 16), Q(2), Q(1, 2), Q(1, 2), Q(2)]
assert all(growth[2*j]*growth[2*j+1] == 1 for j in range(3))
base_growth = [Q(16), Q(1, 16), Q(4), Q(1, 4)]
assert base_growth == [growth[0], growth[1], growth[2]**2, growth[4]**2]
observed_ranks = set()
for q2, q3 in product(map(Q, [-1, 0, 1]), repeat=2):
    Da = zero(4, 6)
    Da[0][0], Da[1][1], Da[2][2], Da[3][4] = 1, 1, 2*q2, 2*q3
    P = mm(mm(Da, J), transpose(Da))
    expected = zero(4)
    expected[0][1], expected[1][0] = 1, -1
    assert P == expected and rank(P) == 2
    observed_ranks.add(rank(Da))
    assert rank(Da) == 2+int(q2 != 0)+int(q3 != 0)
assert observed_ranks == {2, 3, 4}

# Global removal of a translation on the four-Heisenberg complexification:
# solve BCH(Au,v)=u directly, with the original invariant weights.
weights = [2, -1, 1, 2, -1, 1, -2, 1, -1, -2, 1, -1]
multiplier = [Q(2)**w for w in weights]


def bracket(u, v):
    out = [Q(0)]*12
    for j in range(4):
        out[3*j+2] = u[3*j]*v[3*j+1]-u[3*j+1]*v[3*j]
    return out


def bch(u, v):
    return [a+b+c/2 for a, b, c in zip(u, v, bracket(u, v))]


for trial in range(12):
    v = [Q((j+1)*(trial+1)-7, j+2) for j in range(12)]
    u = [Q(0)]*12
    for j in closed_one_indices:
        u[j] = v[j]/(1-multiplier[j])
    correction = bracket([a*x for a, x in zip(multiplier, u)], v)
    for j in [2, 5, 8, 11]:
        u[j] = (v[j]+correction[j]/2)/(1-multiplier[j])
    assert bch([a*x for a, x in zip(multiplier, u)], v) == u

result = dict(
    purpose='New exact algebra checks only; no proof of the missing W lower bound or global analytic steps.',
    fivefold_H1_cup_products_with_explicit_primitives=cup_checks,
    quadratic_field_minimal_polynomials_verified=True,
    Riemann_form_orientation_choices_verified=4,
    local_critical_model=dict(Anosov_symplectic_and_semiconjugacy_identity=True,
                              constant_Poisson_rank=2,
                              observed_map_ranks=sorted(observed_ranks),
                              compact_lattice_not_asserted=True),
    global_translation_equation_exact_checks=12,
    W_dimension_lower_bound_proved=False,
    global_Albanese_theorems_proved_by_script=False,
    all_assertions_passed=True,
)
Path(__file__).with_name('Albanese_bundle_reconstruction_checks.json').write_text(
    json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
