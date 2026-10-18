"""Exact algebra and finite lattice checks for notes 31-34, not existence proofs."""
from fractions import Fraction as F
import itertools
import json
from math import gcd
from pathlib import Path

Z = (0, 0, 0)
ONE = {Z: F(1)}


def add(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = out.get(key, F(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(poly, coefficient):
    return {key: value * coefficient for key, value in poly.items()
            if value * coefficient}


def mul(left, right):
    out = {}
    for m, v in left.items():
        for n, w in right.items():
            key = tuple(i + j for i, j in zip(m, n))
            if sum(key) <= 4:
                out[key] = out.get(key, F(0)) + v * w
    return {key: value for key, value in out.items() if value}


def power(poly, n):
    out = ONE
    for _ in range(n):
        out = mul(out, poly)
    return out


def homogeneous(poly, degree):
    return {key: value for key, value in poly.items() if sum(key) == degree}


def exp(poly):
    out, term = ONE, ONE
    for n in range(1, 5):
        term = scale(mul(term, poly), F(1, n))
        out = add(out, term)
    return out


x, y, z = [{tuple(int(i == j) for i in range(3)): F(1)} for j in range(3)]
a, b = add(x, y), mul(x, y)
c = add(scale(b, 2), scale(power(a, 2), -1))
e = power(b, 2)
todd = ONE
for r in [x, y, scale(x, -1), scale(y, -1)]:
    todd = mul(todd, add(ONE, scale(r, F(1, 2)),
                         scale(power(r, 2), F(1, 12)),
                         scale(power(r, 4), F(-1, 720))))
lhs = homogeneous(mul(mul(add(exp(x), exp(y)), exp(z)), todd), 4)
rhs = add(scale(homogeneous(todd, 4), 2), scale(e, F(-1, 12)),
          scale(power(z, 4), F(1, 12)), scale(mul(a, power(z, 3)), F(1, 6)),
          scale(mul(c, power(z, 2)), F(-1, 6)),
          scale(mul(power(a, 3), z), F(-1, 12)),
          scale(mul(mul(c, a), z), F(-1, 6)))
assert lhs == rhs, "twisted-index formula failed"

p1W = add(power(add(x, y), 2), power(add(x, scale(y, -1)), 2))
p2W = mul(power(add(x, y), 2), power(add(x, scale(y, -1)), 2))
assert p1W == scale(c, -2)
assert p2W == add(power(c, 2), scale(e, -4))

M = [[9, 8, 12, -6], [8, 9, 12, -6],
     [6, 6, 9, -4], [-12, -12, -16, 9]]
Q = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return list(map(list, zip(*A)))


def determinant_char_poly(A):
    out = {}
    for perm in itertools.permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4))
        term = ONE
        for i, j in enumerate(perm):
            entry = scale(ONE, -A[i][j])
            if i == j:
                entry = add(entry, z)
            term = mul(term, entry)
        out = add(out, scale(term, (-1) ** inversions))
    return [out.get((0, 0, degree), F(0)) for degree in range(4, -1, -1)]


assert matmul(matmul(transpose(M), Q), M) == Q
char = determinant_char_poly(M)
assert char == [1, -36, 70, -36, 1]
assert all((M[i][j] - int(i == j)) % 2 == 0 for i in range(4) for j in range(4))
vectors = {
    "u": [1, 1, 0, 0], "r": [0, 0, 1, -2],
    "v": [1, -1, 0, 0], "w": [0, 0, 1, 2],
}
Mv = lambda vector: [row[0] for row in matmul(M, [[v] for v in vector])]
assert Mv(vectors["v"]) == vectors["v"]
assert Mv(vectors["w"]) == vectors["w"]
assert Mv(vectors["u"]) == [17*u + 12*r for u, r in zip(vectors["u"], vectors["r"])]
assert Mv(vectors["r"]) == [24*u + 17*r for u, r in zip(vectors["u"], vectors["r"])]

parity_cases = 0
for kind, t in [("K3", 6), ("K3", -26), ("Kummer", -6)]:
    for u in range(-20, 21, 2):
        for v in range(-10, 11):
            if kind == "K3":
                index = -21 + F(u*u, 4) - 5*u + F((2*u-t-20)*v, 4)
                wu = ((30 + t)*u + 2*v*v + (30+3*t)*v) // 2
            else:
                index = -3 + F(3*u*u, 4) - 9*u + F((3*u-9)*v, 2)
                wu = 18*u + 3*v*v
            assert (index.denominator == 1) == (v % 2 == 0)
            assert wu % 2 == v % 2
            parity_cases += 1

candidates = []
for name, d, p, r, k in [("K3_positive", 1, 2, 2, 1),
                         ("K3_negative", 1, 2, -6, 1),
                         ("Kummer_delta", 3, 0, 0, 1)]:
    q = 2*p*r - 2*d*k*k
    div = gcd(gcd(abs(p), abs(r)), abs(2*d*k))
    assert p % 2 == r % 2 == 0 and k % 2 == 1
    candidates.append(dict(name=name, q=q, divisibility=div,
                           coordinates_on_U_plus_delta=[p, r, k]))
assert [entry["q"] for entry in candidates] == [6, -26, -6]
assert [entry["divisibility"] for entry in candidates] == [2, 2, 6]

stable_J = {}
for t in [6, -26]:
    value = -45 - F(45*t, 2) - F(3*t*t, 2)
    assert value.denominator == 1 and value.numerator % 6 == 0
    stable_J[str(t)] = value.numerator

A = [[2, 1], [1, 1]]
K = [[-4, 2], [2, 4]]
assert matmul(matmul(transpose(A), K), A) == K
assert all(value % 2 == 0 for row in K for value in row)
det_K = K[0][0] * K[1][1] - K[0][1] * K[1][0]
assert det_K == -20
fiber_Omega = [[0, 0, 1, 0], [0, 0, 0, 1],
               [-1, 0, 0, 0], [0, -1, 0, 0]]
fiber_map = [[(F(1, 2) if i < 2 else F(2)) * int(i == j)
              for j in range(4)] for i in range(4)]
assert matmul(matmul(transpose(fiber_map), fiber_Omega), fiber_map) == fiber_Omega

results = dict(
    scope="Algebra, lattice and numerical obstruction checks only; no rank-two bundle or Anosov existence claim.",
    twisted_index_identity=True, rank_five_characteristic_identities=True,
    index_and_Wu_parity_cases=parity_cases,
    lattice_isometry=True, lattice_char_poly_descending=[int(v) for v in char],
    lattice_congruent_to_identity_mod_2=True, candidates=candidates,
    K3_rank_four_extension_obstruction_J=stable_J,
    compact_holomorphic_cocycle=dict(base_matrix=A, Hermitian_matrix=K,
        base_invariance_checked=True, trivial_semicharacter_compatible=True,
        stable_c1_square_on_twofold_factor=2*det_K, fiber_symplectic_map_checked=True,
        is_tangent_derivative=False))
Path(__file__).with_name("Chern_parity_and_lattice_checks.json").write_text(
    json.dumps(results, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results, indent=2))
