"""Exact checks for the mixed quadratic/cubic leaf-geometry example."""
import json
from pathlib import Path
from fractions import Fraction
from itertools import product

# Gaussian rational arithmetic keeps all checks exact and uses the standard library.
def add(z, w): return (z[0]+w[0], z[1]+w[1])
def neg(z): return (-z[0], -z[1])
def sub(z, w): return add(z, neg(w))
def mul(z, w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def conj(z): return (z[0], -z[1])
def power(z, degree):
    result = (Fraction(1), Fraction(0))
    for _ in range(degree): result = mul(result, z)
    return result
def scale(z, value): return (value*z[0], value*z[1])
def direct(z):
    a,b,c = z
    return [a, add(b,power(conj(a),2)), add(c,power(conj(b),3))]
def inverse(w):
    a,b,c = w
    return [a, sub(b,power(conj(a),2)),
            sub(c,power(sub(conj(b),power(a,2)),3))]

weights = [1,2,6]
scaling_factor = Fraction(1,2)
points = [tuple((Fraction(k), Fraction(k+1)) for k in values)
          for values in product(range(-2,3), repeat=3)]
inverse_checks = []
equivariance_checks = []
for point in points:
    value = direct(point)
    inverse_checks.append(inverse(value) == list(point) and direct(inverse(point)) == list(point))
    scaled_point = [scale(z,scaling_factor**degree) for z,degree in zip(point,weights)]
    equivariance_checks.append(direct(scaled_point) ==
                               [scale(z,scaling_factor**degree) for z,degree in zip(value,weights)])
report = {
    "description": "P(z)=(z1,z2+conj(z1)^2,z3+conj(z2)^3)",
    "stable_positive_weights": [1,2,6],
    "rank": 3,
    "maximum_direct_degree": 3,
    "inverse": ["w1", "w2-conj(w1)^2", "w3-(conj(w2)-w1^2)^3"],
    "maximum_inverse_degree": 6,
    "proved_general_bound": 9,
    "real_jacobian_determinant": "1: block triangular with all diagonal blocks I_2",
    "exact_sample_count": len(points),
    "two_sided_inverse_checks_all_passed": all(inverse_checks),
    "weighted_equivariance_checks_all_passed": all(equivariance_checks),
    "symbolic_argument": "Substitution cancels the added conjugate monomials in order; weights obey 2=1+1 and 6=2+2+2.",
    "scope": "Exact rational sample checks plus a hand symbolic argument; no transverse C1 or classification conclusion."
}
target = Path(__file__).with_name("leaf_polynomial_checks.json")
target.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
