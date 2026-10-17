"""Exact algebra checks for notes 22--25; not a proof of analytic estimates."""
from fractions import Fraction as F
import json
import math
from pathlib import Path


def tr(a):
    return [list(c) for c in zip(*a)]


def mm(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inv(a):
    n = len(a)
    aug = [list(row) + list(e) for row, e in zip(a, eye(n))]
    for j in range(n):
        pivot = next((i for i in range(j, n) if aug[i][j]), None)
        if pivot is None:
            raise ZeroDivisionError("singular matrix")
        aug[j], aug[pivot] = aug[pivot], aug[j]
        c = aug[j][j]
        aug[j] = [x / c for x in aug[j]]
        for i in range(n):
            if i != j:
                c = aug[i][j]
                aug[i] = [x - c * y for x, y in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def sym(i, shift):
    return [[F((i + shift) % 7 - 3, 9), F((2 * i + shift) % 5 - 2, 11)],
            [F((2 * i + shift) % 5 - 2, 11), F((3 * i + shift) % 7 - 3, 10)]]


matrix_checks = 0
for i in range(1, 101):
    m, n, b = sym(i, 1), sym(i, 2), sym(i, 4)
    l = add(eye(2), mm(b, m))
    li = inv(l)
    c = mm(li, b)
    assert c == tr(c), "L^-1 Z_p must be symmetric"
    q = [[F(i % 5 - 2, 3)], [F(i % 7 - 3, 4)]]
    z = mm(li, q)
    z1 = scale(-1, mm(mm(mm(li, b), n), z))
    z2 = scale(2, mm(mm(mm(mm(mm(li, b), n), li), b), mm(n, z)))
    implicit = add(scale(2, mm(n, z1)), mm(m, z2))
    gradient = scale(-2, mm(mm(mm(mm(tr(li), n), c), n), z))
    assert implicit == gradient
    matrix_checks += 1


nonlinear_checks = 0
for i in range(1, 101):
    z = F(i % 9 - 4, 10)
    beta = F(i % 5 + 1, 10)
    l = 1 + 2 * beta * z
    v = F(2, 3) + F(3, 5) * z + F(4, 7) * z * z
    vp = F(3, 5) + F(8, 7) * z
    z1 = -beta * v / l
    z2 = -(2 * beta * z1 * z1 + 2 * beta * vp * z1) / l
    implicit = 2 * z1 * z1 + 2 * z * z2 + 2 * vp * z1
    gradient = -2 * beta * v * vp / (l * l) + 2 * beta * beta * v * v / (l ** 3)
    assert implicit == gradient
    nonlinear_checks += 1


symplectic_checks = 0
affine_checks = 0
s = F(1, 2)
d = 1 / (s * s)
j = [[F(0), F(0), F(1), F(0)],
     [F(0), F(0), F(0), F(1)],
     [F(-1), F(0), F(0), F(0)],
     [F(0), F(-1), F(0), F(0)]]
for i in range(1, 101):
    q1, p2, kappa = F(i % 11 - 5, 7), F(i % 9 - 4, 6), F(i % 5 + 1, 3)
    jac = [[s, 0, 0, 0],
           [s * s * kappa * q1, s * s, 0, 0],
           [-kappa * p2 / s, 0, 1 / s, -kappa * q1 / s],
           [0, 0, 0, d]]
    assert mm(mm(tr(jac), j), jac) == j
    symplectic_checks += 1
    a = [[s, F(0)], [F(0), s * s]]
    c = [[-kappa * p2 / s, F(0)], [F(0), F(0)]]
    h = scale(-1, mm(tr(a), c))
    assert h == [[kappa * p2, 0], [0, 0]]
    b0 = sym(i, 3)
    pushed = mm(add(c, mm(tr(inv(a)), b0)), inv(a))
    pulled = add(mm(mm(tr(a), pushed), a), h)
    assert pulled == b0
    affine_checks += 1


def alog(u):
    return 0j if u == 0 else u * math.log(abs(u))


def critical_map(q1, q2, p1, p2):
    sf = 0.5
    df = 4.0
    k = -math.log(df)
    return (sf * q1, sf * sf * (q2 + k * q1 * q1 / 2),
            (p1 - k * q1 * p2) / sf, df * p2)


float_invariance_errors = []
for i in range(1, 101):
    u = complex((i % 13 - 6) / 17, (i % 11 - 5) / 19)
    q1 = complex((i % 7 - 3) / 23, (i % 5 - 2) / 29)
    q2 = complex((i % 9 - 4) / 31, (i % 7 - 3) / 37)
    t1 = complex((i % 5 - 2) / 41, (i % 3 - 1) / 43)
    q1p, q2p, p1p, p2p = critical_map(q1, q2, t1 + q1 * alog(u), u)
    float_invariance_errors.append(abs(p1p - (2 * t1 + q1p * alog(p2p))))
assert max(float_invariance_errors) < 1e-13

critical_ratios = []
for n in (4, 8, 12, 16, 20):
    h = 4.0 ** (-n)
    ratio = (alog(2 * h) - 2 * alog(h)).real / h
    assert abs(ratio - 2 * math.log(2)) < 1e-12
    critical_ratios.append({"n": n, "normalized_second_difference": ratio})

stable_weights = [-1, -2, -1]
assert stable_weights[0] + stable_weights[0] - stable_weights[1] == 0
assert s * s * d == 1

result = {
    "scope": "Algebra checks only; analytic proofs are in notes 22--25.",
    "exact_rational_matrix_second_variation_checks": matrix_checks,
    "exact_rational_nonlinear_scalar_second_variation_checks": nonlinear_checks,
    "exact_rational_symplectic_Jacobian_checks": symplectic_checks,
    "exact_rational_affine_plane_pullback_checks": affine_checks,
    "floating_critical_foliation_invariance_checks": len(float_invariance_errors),
    "maximum_floating_invariance_error": max(float_invariance_errors),
    "critical_logarithmic_model_second_difference_ratios": critical_ratios,
    "compact_six_dimensional_resonance_weight": 0,
    "all_checks_passed": True,
}
out = Path(__file__).with_name("second_variation_and_critical_model_checks.json")
out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2, ensure_ascii=False))
