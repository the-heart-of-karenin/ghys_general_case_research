"""Exact auxiliary checks for notes 36-38; not a proof of bundle existence."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

root = Path(__file__).resolve().parent

def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def mod2(a):
    return [[v % 2 for v in row] for row in a]

def diag(*values):
    return [[values[i] if i == j else F(0) for j in range(len(values))]
            for i in range(len(values))]

def tup(a):
    return [[str(v) for v in row] for row in a]

chern = []
for family, cc, euler, mixed, fujiki, ts in [
    ("K3_square", 828, 324, 30, 3, [6, -26]),
    ("Kummer_fourfold", 756, 108, 54, 9, [-6]),
]:
    for t in ts:
        caa = mixed * t
        a4 = fujiki * t * t
        bb = F(cc + 2*caa + a4, 4)
        bc = F(cc + caa, 2)
        baa = F(caa + a4, 2)
        j = (bb - bc - 2*baa) / 2
        assert bb == euler
        assert j.denominator == 1 and j % 6 == 0
        chern.append(dict(family=family, q_a=t, b_squared=int(bb), J=int(j)))

# The unknown lower-right block does not affect invertibility of odd Sq^2.
indices = [(i, j) for i in range(4) for j in range(i, 4)]
odd_blocks = 0
for bits in product([0, 1], repeat=len(indices)):
    c = [[0]*4 for _ in range(4)]
    for (i, j), value in zip(indices, bits):
        c[i][j] = c[j][i] = value
    m = [[0]*8 for _ in range(8)]
    inv = [[0]*8 for _ in range(8)]
    for i in range(4):
        m[i][4+i] = m[4+i][i] = 1
        inv[i][4+i] = inv[4+i][i] = 1
        for j in range(4):
            m[4+i][4+j] = c[i][j]
            inv[i][j] = c[i][j]
    assert mod2(mm(m, inv)) == eye(8)
    odd_blocks += 1

# Coefficients of the two positive completed-square polynomials.
assert [3, 30, 324] == [3, 2*3*5, 3*(5*5+83)]
assert [9, 54, 108] == [9, 2*9*3, 9*(3*3+3)]

# KSp^0 coefficients and the two incoming d2 sources, with q measured in KSp.
ko = {0: "Z", 1: "Z2", 2: "Z2", 3: "0", 4: "Z", 5: "0", 6: "0", 7: "0"}
def ksp_coefficient(q):
    return ko[(4-q) % 8]  # KSp^q = KO^(q-4).
possible = [(p, -p, ksp_coefficient(-p)) for p in range(9)
            if ksp_coefficient(-p) != "0"]
assert possible == [(0, 0, "Z"), (4, -4, "Z"), (5, -5, "Z2"),
                    (6, -6, "Z2"), (8, -8, "Z")]
assert ksp_coefficient(-4) == "Z"
assert ksp_coefficient(-5) == ksp_coefficient(-6) == "Z2"

# Exact central-error amplification with uniformly contracting stable blocks.
models = []
for m in range(1, 13):
    k = F(2)
    rho = F(1, 4)
    eps = F(1, 2**m)
    d = diag(k, 1/k)
    dinv = diag(1/k, k)
    p = eye(2)
    q = eye(2)
    for j in range(2*m):
        b = [[rho*v for v in row] for row in (d if j < m else dinv)]
        bt = b if j != m else mm(b, [[1, 0], [eps, 1]])
        p = mm(b, p)
        q = mm(bt, q)
    assert p == diag(rho**(2*m), rho**(2*m))
    rel = [[v/rho**(2*m) for v in row] for row in q]
    assert rel == [[1, 0], [eps*k**(2*m), 1]]
    assert eps*k**(2*m) == 2**m
    # At the perturbed step, ||B|| <= rho*K*(1+eps) <= 3/4.
    assert rho*k*(1+eps) <= F(3, 4)
    models.append(dict(m=m, normalized_error=str(eps*k**(2*m))))

result = dict(
    chern_top_cell_checks=chern,
    odd_Steenrod_block_matrices_checked=odd_blocks,
    line_obstruction_completed_squares=True,
    KSp_total_zero_terms=possible,
    exact_shadowing_models=models,
    scope="Checks formulas only. Existence, Thom-Gysin identification, and AHSS arguments are proved in notes 36-38, not by this script.",
)
(root / "actual_reduction_and_shadowing_checks.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
