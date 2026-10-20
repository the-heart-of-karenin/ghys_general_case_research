"""Exact algebra checks for note106; no numerical Anosov threshold is asserted."""
from fractions import Fraction as F
from pathlib import Path
import json


def zero(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def eye(n):
    a = zero(n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def add(a, b, scale=F(1)):
    return [[x + scale * y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def power(a, n):
    result = eye(len(a))
    for _ in range(n):
        result = mul(result, a)
    return result


def rank(a):
    a = [row[:] for row in a]
    k = 0
    for j in range(len(a[0])):
        p = next((i for i in range(k, len(a)) if a[i][j]), None)
        if p is None:
            continue
        a[k], a[p] = a[p], a[k]
        pivot = a[k][j]
        a[k] = [v / pivot for v in a[k]]
        for i in range(len(a)):
            if i != k:
                c = a[i][j]
                a[i] = [x - c * y for x, y in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k


B = [[F(2), F(1)], [F(1), F(1)]]
eps = F(1, 100)  # Only checks identities, not that this chosen epsilon is Anosov.
A = zero(8)
for k in range(4):
    for i in range(2):
        for j in range(2):
            A[2*k+i][2*k+j] = B[i][j]
M = [row[:] for row in A]
M[2][0] = eps


def polynomial(a, trace=F(3)):
    return add(add(mul(a, a), a, -trace), eye(len(a)))


q = polynomial(M)
expected = zero(8)
for i, row in enumerate([[1, 1], [1, 0]]):
    for j, value in enumerate(row):
        expected[2+i][j] = eps * value
checks = {
    'B_satisfies_t2_minus_3t_plus_1': polynomial(B) == zero(2),
    'A_satisfies_t2_minus_3t_plus_1': polynomial(A) == zero(8),
    'M_polynomial_exact_formula': q == expected,
    'M_polynomial_has_rank_two': rank(q) == 2,
    'M_polynomial_nonzero': q != zero(8),
    'M_polynomial_square_zero': mul(q, q) == zero(8),
}
for m in range(1, 9):
    bm = power(B, m)
    trace = bm[0][0] + bm[1][1]
    pm = polynomial(power(M, m), trace)
    checks[f'fixed_return_{m}_nonsemisimple_rank_two'] = rank(pm) == 2
    checks[f'fixed_return_{m}_polynomial_square_zero'] = mul(pm, pm) == zero(8)

# Arbitrary successive lower blocks model orbit derivatives, not sampled orbits.
product = eye(8)
for m in range(1, 9):
    step = [row[:] for row in A]
    for i in range(2):
        for j in range(2):
            step[2+i][j] = F((m+i+1)*(j+2), 101+m)
    product = mul(step, product)
    bm = power(B, m)
    checks[f'arbitrary_lower_blocks_{m}_diagonal_blocks'] = all(
        product[2*k+i][2*k+j] == bm[i][j]
        for k in range(4) for i in range(2) for j in range(2)
    )
    checks[f'arbitrary_lower_blocks_{m}_block_triangular'] = all(
        product[i][j] == 0 for i in range(8) for j in range(8) if i//2 < j//2
    )

assert all(checks.values()), checks
result = {
    'scope': 'Exact rational identities for note106 only; not a proof of holomorphicity or a numerical Anosov threshold.',
    'epsilon_for_identity_checks': str(eps),
    'checks': checks,
    'passed': sum(checks.values()),
    'total': len(checks),
}
Path(__file__).with_name('toral_scalar_Jordan_checks.json').write_text(
    json.dumps(result, indent=2), encoding='utf-8'
)
print(f"{result['passed']}/{result['total']} exact algebra checks passed.")
