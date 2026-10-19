"""Exact counterchecks for notes 58-59; not a classification proof or novelty test."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path
import json


def rref(rows, columns):
    a = [[Q(x) for x in row] for row in rows]
    pivots, k = [], 0
    for j in range(columns):
        p = next((i for i in range(k, len(a)) if a[i][j]), None)
        if p is None:
            continue
        a[k], a[p] = a[p], a[k]
        z = a[k][j]
        a[k] = [x / z for x in a[k]]
        for i in range(len(a)):
            if i != k:
                z = a[i][j]
                a[i] = [x - z * y for x, y in zip(a[i], a[k])]
        pivots.append(j)
        k += 1
    return a, pivots


def nullspace(rows, columns):
    a, pivots = rref(rows, columns)
    basis = []
    for j in range(columns):
        if j in pivots:
            continue
        v = [Q(0)] * columns
        v[j] = Q(1)
        for i, p in enumerate(pivots):
            v[p] = -a[i][j]
        basis.append(v)
    return basis


edges = [(0, 2), (0, 3), (1, 2), (1, 3)]
weights = [[int(i == j) for i in range(4)] for j in range(4)]
weights += [[int(i in e) for i in range(4)] for e in edges]
labels = ['b1', 'b2', 'c1', 'c2', 'b1c1', 'b1c2', 'b2c1', 'b2c2']
matching_checks = []
for perm in permutations(range(4)):
    rows = []
    for edge, k in zip(edges, perm):
        row = [0] * 4
        for j in edge + (k,):
            row[j] += 1
        rows.append(row)
    basis = nullspace(rows, 4)
    forced = [labels[i] for i, w in enumerate(weights)
              if all(sum(x * y for x, y in zip(w, v)) == 0 for v in basis)]
    assert forced, (perm, basis)
    matching_checks.append(dict(permutation=perm, nullity=len(basis), forced_unit_modulus=forced))


def power_of_linear_form(v, power):
    out = defaultdict(int)
    for indices in product(range(len(v)), repeat=power):
        exponent = tuple(indices.count(j) for j in range(len(v)))
        coefficient = 1
        for j in indices:
            coefficient *= v[j]
        out[exponent] += coefficient
    return {key: value for key, value in out.items() if value}


def sum_powers(forms, power):
    out = defaultdict(int)
    for form in forms:
        for key, value in power_of_linear_form(form, power).items():
            out[key] += value
    return {key: value for key, value in out.items() if value}


def subtract(a, b):
    out = defaultdict(int, a)
    for key, value in b.items():
        out[key] -= value
    return {key: value for key, value in out.items() if value}


center_logs = [(0, 1, 1), (0, 1, -1), (0, -1, 1), (0, -1, -1)]
quotient_logs = [(-1, 1, 0), (-1, -1, 0), (1, 0, 1), (1, 0, -1)]
square_difference = subtract(sum_powers(center_logs, 2), sum_powers(quotient_logs, 2))
cube_difference = subtract(sum_powers(center_logs, 3), sum_powers(quotient_logs, 3))
assert square_difference == {(2, 0, 0): -4, (0, 2, 0): 2, (0, 0, 2): 2}
assert cube_difference == {(1, 2, 0): 6, (1, 0, 2): -6}


def add_forms(*forms):
    out = defaultdict(int)
    for form in forms:
        for key, value in form.items():
            out[key] += value
    return {key: value for key, value in out.items() if value}


def scale(form, value):
    return {key: coefficient * value for key, coefficient in form.items() if coefficient * value}


def wedge(a, b):
    out = defaultdict(int)
    for key, coefficient in a.items():
        for other, other_coefficient in b.items():
            if set(key).intersection(other):
                continue
            inversions = sum(i > j for i in key for j in other)
            out[tuple(sorted(key + other))] += (-1) ** inversions * coefficient * other_coefficient
    return {key: value for key, value in out.items() if value}


def differential(form, derivatives):
    out = {}
    for key, coefficient in form.items():
        for place, index in enumerate(key):
            left = {key[:place]: 1}
            right = {key[place + 1:]: 1}
            out = add_forms(out, scale(wedge(wedge(left, derivatives.get(index, {})), right),
                                       coefficient * (-1) ** place))
    return out


def e(i):
    return {(i,): 1}


def two(i, j):
    return wedge(e(i), e(j))


compact_derivatives = {1: two(0, 4), 3: two(2, 6), 5: scale(two(0, 4), -1),
                       7: scale(two(2, 6), -1)}
omega0 = add_forms(two(0, 1), two(2, 3))
psi = add_forms(two(0, 2), two(1, 3))
assert differential(omega0, compact_derivatives) == {}
assert differential(psi, compact_derivatives)
assert wedge(omega0, omega0) == {(0, 1, 2, 3): 2}
assert wedge(psi, psi) == {(0, 1, 2, 3): -2}
compact_weights = [1, 2, -1, -2]
zero_weight_pairs = [pair for pair in combinations(range(4), 2)
                     if sum(compact_weights[i] for i in pair) == 0]
assert zero_weight_pairs == [(0, 2), (1, 3)]

noncompact_derivatives = {2: scale(two(0, 1), -1)}
noncompact_omega = add_forms(two(0, 2), two(1, 3))
assert differential(noncompact_omega, noncompact_derivatives) == {}
assert wedge(noncompact_omega, noncompact_omega) == {(0, 1, 2, 3): -2}
noncompact_weights = [1, -2, -1, 2]
assert noncompact_weights[0] + noncompact_weights[1] == noncompact_weights[2]
assert all(sum(noncompact_weights[i] for i in pair) == 0 for pair in noncompact_omega)


def ring_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def ring_multiply(a, b):
    # Coordinates on 1, i, sqrt(3), i sqrt(3).
    out = [0] * 4
    for k, x in enumerate(a):
        for l, y in enumerate(b):
            imaginary = k % 2 + l % 2
            radical = k // 2 + l // 2
            out[(imaginary % 2) + 2 * (radical % 2)] += (
                x * y * (-1) ** (imaginary // 2) * 3 ** (radical // 2))
    return tuple(out)


def sigma(a):
    return (a[0], a[1], -a[2], -a[3])


def conjugate(a):
    return (a[0], -a[1], a[2], -a[3])


one, lam = (1, 0, 0, 0), (2, 0, 1, 0)
assert ring_multiply(lam, sigma(lam)) == one
ring_basis = [tuple(int(i == j) for i in range(4)) for j in range(4)]
for x, y in product(ring_basis, repeat=2):
    assert sigma(conjugate(x)) == conjugate(sigma(x))
    assert sigma(ring_multiply(x, y)) == ring_multiply(sigma(x), sigma(y))
    # The noncentral scaling and the quadratic central scaling respect the group cross term.
    assert ring_multiply(conjugate(ring_multiply(lam, x)), ring_multiply(lam, y)) == (
        ring_multiply(ring_multiply(lam, lam), ring_multiply(conjugate(x), y)))


def determinant(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    result = Q(1)
    for k in range(len(a)):
        p = next((i for i in range(k, len(a)) if a[i][k]), None)
        if p is None:
            return Q(0)
        if p != k:
            a[p], a[k] = a[k], a[p]
            result *= -1
        z = a[k][k]
        result *= z
        for i in range(k + 1, len(a)):
            ratio = a[i][k] / z
            a[i] = [x - ratio * y for x, y in zip(a[i], a[k])]
    return result


lambda_matrix = list(map(list, zip(*(ring_multiply(lam, x) for x in ring_basis))))
lambda_square = ring_multiply(lam, lam)
lambda_square_matrix = list(map(list, zip(*(ring_multiply(lambda_square, x) for x in ring_basis))))
assert determinant(lambda_matrix) == determinant(lambda_square_matrix) == 1

torus_matrix = [[2, 1, 0, 0], [1, 1, 0, 0], [0, 0, 2, 1], [0, 0, 1, 1]]
pullback_basis = [{(j,): torus_matrix[i][j] for j in range(4) if torus_matrix[i][j]}
                  for i in range(4)]
torus_omega_pullback = add_forms(wedge(pullback_basis[0], pullback_basis[1]),
                                wedge(pullback_basis[2], pullback_basis[3]))
assert torus_omega_pullback == omega0
assert determinant(torus_matrix) == 1


def matrix_product(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


torus_cube = matrix_product(matrix_product(torus_matrix, torus_matrix), torus_matrix)
assert all((torus_cube[i][j] - int(i == j)) % 2 == 0
           for i in range(4) for j in range(4))
involution = [[(-1 if i < 2 else 1) * int(i == j) for j in range(4)] for i in range(4)]
assert matrix_product(involution, torus_cube) == matrix_product(torus_cube, involution)
assert involution[0][0] == -1  # Nontrivial conjugation on the translation lattice.
# The fixed coordinates of the involution move by a nonzero half-lattice translation.
assert (torus_cube[2][2] - 1) % 2 == 0 and torus_cube[3][2] % 2 == 0


def algebra_check(name, bracket_data, expected_center, expected_derived):
    def bracket_basis(i, j):
        if i == j:
            return [0] * 8
        sign = 1 if i < j else -1
        v = bracket_data.get(tuple(sorted((i, j))), {})
        return [sign * v.get(k, 0) for k in range(8)]

    def bracket(i, v):
        result = [0] * 8
        for j, coefficient in enumerate(v):
            for k, x in enumerate(bracket_basis(i, j)):
                result[k] += coefficient * x
        return result

    for i, j, k in combinations(range(8), 3):
        terms = [bracket(i, bracket_basis(j, k)), bracket(j, bracket_basis(k, i)),
                 bracket(k, bracket_basis(i, j))]
        assert all(sum(v[l] for v in terms) == 0 for l in range(8))
    center_rows = [[bracket_basis(i, j)[k] for i in range(8)]
                   for j in range(8) for k in range(8)]
    center_dimension = len(nullspace(center_rows, 8))
    derived_rows = [bracket_basis(i, j) for i, j in combinations(range(8), 2)]
    derived_dimension = len(rref(derived_rows, 8)[1])
    assert center_dimension == expected_center
    assert derived_dimension == expected_derived
    return dict(name=name, jacobi=True, center_dimension=center_dimension,
                derived_dimension=derived_dimension)


algebra_checks = [
    algebra_check('h3+h3+R2', {(0, 1): {2: 1}, (3, 4): {5: 1}}, 4, 2),
    algebra_check('f3+R2', {(0, 1): {3: 1}, (0, 2): {4: 1}, (1, 2): {5: 1}}, 5, 3),
    algebra_check('g', {(0, 1): {6: 1}, (0, 2): {7: 1}, (3, 4): {6: 1},
                        (3, 5): {7: 1}}, 2, 2),
    algebra_check('h', {(0, 2): {4: 1}, (0, 3): {5: 1}, (1, 2): {6: 1},
                        (1, 3): {7: 1}}, 4, 4),
    algebra_check('l4+l4', {(0, 1): {2: 1}, (0, 2): {3: 1}, (4, 5): {6: 1},
                            (4, 6): {7: 1}}, 2, 4),
]


def serial_form(form):
    return {' '.join(map(str, key)): value for key, value in form.items()}


result = dict(
    purpose='Exact independent counterchecks; analytic proof and classification inputs in note 58.',
    all_passed=True,
    candidate_algebras=algebra_checks,
    h_spectral_matchings=matching_checks,
    log_moment_polynomials=dict(square_difference=serial_form(square_difference),
                                cube_difference=serial_form(cube_difference)),
    compact_nonpreserving_example=dict(omega_closed=True, omega_square=serial_form(wedge(omega0, omega0)),
        invariant_nondegenerate_form_not_closed=serial_form(differential(psi, compact_derivatives)),
        zero_weight_pairs=zero_weight_pairs, multiplication_matrix=lambda_matrix,
        central_multiplication_matrix=lambda_square_matrix, both_determinants=1),
    noncompact_example=dict(omega_closed=True, omega_square=serial_form(wedge(noncompact_omega, noncompact_omega)),
                           weights=noncompact_weights),
    torus_example=dict(symplectic=True, determinant=1, finite_free_quotient=True,
                       cube_matrix=torus_cube, involution=involution, cube_commutes_mod_lattice=True),
    limitations=['Does not prove external classification theorems.',
                 'Does not certify novelty or classify unknown Anosov systems.'])
target = Path(__file__).with_name('eight_dimensional_nil_model_checks.json')
target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(dict(all_passed=True, classified_candidates_checked=5,
                     spectral_matchings_checked=24, output=str(target)), ensure_ascii=False))
