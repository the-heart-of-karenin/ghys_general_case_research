"""Exact checks for notes 41--42; these are identity/model checks, not proofs."""
from fractions import Fraction as Q
import json
from pathlib import Path

root = Path(__file__).resolve().parent
checks = {}

# Sym^2(V) -> self-adjoint endomorphisms: integral(beta gamma)
# = tr(C_beta) tr(C_gamma) + 2 tr(C_beta C_gamma).
def pair(cn, ct, dn, dt):
    return (2 * cn + 21 * ct) * (2 * dn + 21 * dt) + 2 * (2 * cn * dn + 21 * ct * dt)

values = {
    "theta_N_squared": pair(1, 0, 1, 0),
    "theta_T_squared": pair(0, 1, 0, 1),
    "theta_N_theta_T": pair(1, 0, 0, 1),
    "theta_total_theta_N": pair(1, 1, 1, 0),
    "theta_total_theta_T": pair(1, 1, 0, 1),
    "D_squared": pair(23, -2, 23, -2),
    "c2_D": pair(Q(6, 5), Q(6, 5), 23, -2),
}
assert values == {
    "theta_N_squared": 8, "theta_T_squared": 483,
    "theta_N_theta_T": 42, "theta_total_theta_N": 50,
    "theta_total_theta_T": 525, "D_squared": 2300, "c2_D": 120,
}
assert 2 * 23 + 23 * (-2) == 0  # Lagrangian condition on D.
assert (2 * 23 + 21 * (-2)) + 2 * 23 == 50  # D H^2 / q(H).
checks["Fujiki_and_Chern_pairings"] = {key: str(value) for key, value in values.items()}

# The divisibility argument in note 41 is a proof for all integers.
# Enumeration only tests the elimination and parametrization formulas.
admissible_t = []
for t in range(-800, 801):
    e = Q(23 * t * t, 16)
    chi = (e - t) / 4
    admissible = e.denominator == chi.denominator == 1
    assert admissible == (t % 8 == 0)
    if admissible:
        v = t // 8
        k = Q(t, 40)
        assert k == Q(v, 5)
        assert e == 92 * v * v
        assert chi == 23 * v * v - 2 * v
        assert e == 2300 * k * k
        assert 120 * k == 3 * e - 12 * chi
        if v != 0:
            assert chi >= 21
        admissible_t.append(t)
checks["integer_parametrization"] = {
    "integers_tested": 1601, "admissible_count": len(admissible_t),
    "nonzero_chi_minimum": 21,
    "limitation": "Finite enumeration checks formulas; divisibility for every integer is proved in note 41.",
}

# Monomial x_i = u^(3-i) v^i for the twisted cubic cone.
exponents = [(3, 0), (2, 1), (1, 2), (0, 3)]
def add(left, right):
    return tuple(a + b for a, b in zip(left, right))
assert add(exponents[0], exponents[2]) == add(exponents[1], exponents[1])
assert add(exponents[0], exponents[3]) == add(exponents[1], exponents[2])
assert add(exponents[1], exponents[3]) == add(exponents[2], exponents[2])
weights = [u - v for u, v in exponents]
assert weights == [3, 1, -1, -3]
assert weights[0] + weights[3] == weights[1] + weights[2] == 0
def wedge_jacobian_coeff(left, right):
    u1, v1 = left
    u2, v2 = right
    return u1 * v2 - v1 * u2
w03 = wedge_jacobian_coeff(exponents[0], exponents[3])
w12 = wedge_jacobian_coeff(exponents[1], exponents[2])
assert add(exponents[0], exponents[3]) == add(exponents[1], exponents[2]) == (3, 3)
assert w03 == 9 and w12 == 3 and w03 - 3 * w12 == 0

# Resolution chart x_i = r t^i. The wedge of dx_i and dx_j is
# (j-i) r t^(i+j-1) dr^dt; compare the two terms of Omega.
assert (3 - 0) - 3 * (2 - 1) == 0
assert [3 - 2 * i for i in range(4)] == weights
checks["isolated_Lagrangian_cone"] = {
    "defining_relations_checked": 3,
    "ambient_weights": weights,
    "pullback_wedge_coefficients": [w03, w12],
    "symplectic_and_Lagrangian_identities": "passed",
    "resolution_chart_equivariance": "passed",
    "limitation": "This is a noncompact local model and is not a counterexample to the compact Ghys conjecture.",
}

result = {"all_checks_passed": True, "checks": checks,
          "scope": "Exact identities and finite arithmetic checks only; no existence or nonexistence theorem is inferred by computation."}
(root / "rank_two_periodic_surface_checks.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
