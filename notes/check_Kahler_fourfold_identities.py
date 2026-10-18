"""Exact algebra checks only; does not prove a geometric classification."""
from fractions import Fraction as F
import itertools
import json
from pathlib import Path

zero = (0, 0, 0, 0)
one = {zero: F(1)}


def add(*polys):
    result = {}
    for poly in polys:
        for monomial, value in poly.items():
            result[monomial] = result.get(monomial, F(0)) + value
    return {key: value for key, value in result.items() if value}


def scale(poly, coefficient):
    return {key: value * coefficient for key, value in poly.items()
            if value * coefficient}


def mul(left, right):
    result = {}
    for m, v in left.items():
        for n, w in right.items():
            exponent = tuple(a + b for a, b in zip(m, n))
            if sum(exponent) <= 4:
                result[exponent] = result.get(exponent, F(0)) + v * w
    return {key: value for key, value in result.items() if value}


def power(poly, exponent):
    result = one
    for _ in range(exponent):
        result = mul(result, poly)
    return result


roots = [{tuple(int(j == i) for j in range(4)): F(1)} for i in range(4)]
chern = [one]
for degree in range(1, 5):
    terms = []
    for indices in itertools.combinations(range(4), degree):
        term = one
        for i in indices:
            term = mul(term, roots[i])
        terms.append(term)
    chern.append(add(*terms))
c1, c2, c3, c4 = chern[1:]
todd = one
for x in roots:
    todd = mul(todd, add(one, scale(x, F(1, 2)),
                         scale(power(x, 2), F(1, 12)),
                         scale(power(x, 4), F(-1, 720))))
formula = add(
    one, scale(c1, F(1, 2)),
    scale(add(power(c1, 2), c2), F(1, 12)),
    scale(mul(c1, c2), F(1, 24)),
    scale(add(scale(power(c1, 4), -1),
              scale(mul(power(c1, 2), c2), 4),
              scale(power(c2, 2), 3), mul(c1, c3), scale(c4, -1)), F(1, 720)))
assert todd == formula

a, b = roots[:2]
whitney = mul(add(one, a, b), add(one, scale(a, -1), b))
assert whitney == add(one, scale(b, 2), scale(power(a, 2), -1), power(b, 2))

results = {
    "scope": "exact polynomial identities and characteristic-number arithmetic only",
    "todd_degree_four_checked": True,
    "whitney_E_plus_dual_checked": True,
    "torsion_case_euler_forced": str(F(2160, 11)),
    "torsion_case_euler_is_integer": F(2160, 11).denominator == 1,
    "types": {},
}
for name, quartic, mixed, c2square, roots_t in [
    ("K3^[2]", 3, 30, 828, [6, -26]),
    ("Kummer_2", 9, 54, 756, [-6, -6]),
]:
    euler = 3 * c2square - 2160
    constant = c2square - 4 * euler
    assert quartic * roots_t[0] * roots_t[1] == constant
    assert -quartic * sum(roots_t) == 2 * mixed
    for t in roots_t:
        assert quartic * t * t + 2 * mixed * t + constant == 0
    results["types"][name] = dict(euler=euler,
        polynomial_descending=[quartic, 2 * mixed, constant], necessary_q_values=roots_t)

dest = Path(__file__).with_name("Kahler_fourfold_identity_checks.json")
dest.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results, indent=2))
