"""Exact checks for the actual lattice realization and the Anosov obstruction."""
from fractions import Fraction as Q
import json
from pathlib import Path

root = Path(__file__).resolve().parent
def tr(matrix):
    return [list(row) for row in zip(*matrix)]
def mul(left, right):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*right)] for row in left]
def det(matrix):
    rows = [[Q(value) for value in row] for row in matrix]
    value = Q(1)
    for column in range(len(rows)):
        pivot = next((i for i in range(column, len(rows)) if rows[i][column]), None)
        if pivot is None:
            return Q(0)
        if pivot != column:
            rows[pivot], rows[column] = rows[column], rows[pivot]
            value *= -1
        scale = rows[column][column]
        value *= scale
        for i in range(column + 1, len(rows)):
            ratio = rows[i][column] / scale
            rows[i] = [x - ratio * y for x, y in zip(rows[i], rows[column])]
    return value

G = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
V = [[1, 0], [29, 0], [0, 1], [0, -58]]
GramN = [[58, 0], [0, -116]]
M = [[3363, 4756], [2378, 3363]]
assert mul(mul(tr(V), G), V) == GramN
assert det([V[0], V[2]]) == 1  # Primitivity of N.
assert mul(mul(tr(M), GramN), M) == GramN and det(M) == 1
assert 3363 * 3363 - 2 * 2378 * 2378 == 1
assert 3364 // 58 == 58 and 3364 % 58 == 0
assert 2378 // 58 == 41 and 2378 % 58 == 0
assert 4756 // 116 == 41 and 4756 % 116 == 0
assert 3364 // 116 == 29 and 3364 % 116 == 0
assert (3363 + 1) % 58 == (3363 + 1) % 116 == 0

C = [[58, -41], [41, -29]]
correction = mul(mul(mul(V, C), tr(V)), G)
A = [[correction[i][j] - int(i == j) for j in range(4)] for i in range(4)]
assert all(isinstance(value, int) for row in A for value in row)
assert mul(mul(tr(A), G), A) == G
assert mul(A, V) == mul(V, M)
W = [[1, 0], [-29, 0], [0, 1], [0, 58]]
assert mul(mul(tr(V), G), W) == [[0, 0], [0, 0]]
assert mul(A, W) == [[-value for value in row] for row in W]
assert det(A) == 1  # Remaining 19 directions are -I; full determinant is -1.
AminusI = [[A[i][j] - int(i == j) for j in range(4)] for i in range(4)]
assert det(AminusI) == -26896

# Torus countercheck: anti-symplectic hyperbolicity is possible without the IHS data.
B = [[2, 1], [1, 0]]
J = [[0, 1], [-1, 0]]
assert det(B) == -1
assert mul(mul(tr(B), J), B) == [[0, -1], [1, 0]]
assert det([[B[i][j] - int(i == j) for j in range(2)] for i in range(2)]) != 0
assert det([[B[i][j] + int(i == j) for j in range(2)] for i in range(2)]) != 0

euler = 1 + 23 + 276 + 23 + 1
assert euler == 324 and 4 * euler - 828 == 468
result = dict(all_checks_passed=True, picard_gram=GramN, picard_action=M,
              integral_action_on_two_hyperbolic_planes=A,
              action_on_orthogonal_complement="-I",
              determinant_A_minus_I_on_four_directions=str(det(AminusI)),
              full_H2_fixed_space_is_zero=True,
              positive_entropy_eigenvalue="3363 + 2378 sqrt(2)",
              euler_K3_square=euler, c2_squared=828, Chern_contradiction_gap=468,
              antisymplectic_torus_model="passed",
              limitation="Exact arithmetic checks only. Actual realization uses the period map, wall criterion, monodromy and strong Torelli; the Anosov exclusion uses the derivative argument in note 45.")
(root / "symplectic_power_and_actual_example_checks.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
