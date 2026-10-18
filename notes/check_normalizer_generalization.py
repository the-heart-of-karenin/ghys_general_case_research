"""Exact auxiliary checks; the arguments and actual realizations are in notes 46--48."""
from fractions import Fraction as Q
from itertools import product
from math import gcd
from functools import reduce
from pathlib import Path
import json

root = Path(__file__).resolve().parent
def transpose(a):
    return list(map(list, zip(*a)))
def matmul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]
def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]
def det(a):
    b = [[Q(x) for x in row] for row in a]
    ans = Q(1)
    for j in range(len(b)):
        k = next((i for i in range(j, len(b)) if b[i][j]), None)
        if k is None:
            return Q(0)
        if k != j:
            b[j], b[k] = b[k], b[j]
            ans = -ans
        pivot = b[j][j]
        ans *= pivot
        for i in range(j+1, len(b)):
            t = b[i][j]/pivot
            b[i] = [x-t*y for x, y in zip(b[i], b[j])]
    return ans
def rank(a):
    b = [[Q(x) for x in row] for row in a]
    h = 0
    for j in range(len(b[0])):
        k = next((i for i in range(h, len(b)) if b[i][j]), None)
        if k is None:
            continue
        b[h], b[k] = b[k], b[h]
        pivot = b[h][j]
        b[h] = [v/pivot for v in b[h]]
        for i in range(len(b)):
            if i != h:
                t = b[i][j]
                b[i] = [x-t*y for x, y in zip(b[i], b[h])]
        h += 1
        if h == len(b):
            break
    return h
def col(v):
    return [[x] for x in v]
def pairing(v, w, G):
    return matmul(matmul([v], G), col(w))[0][0]

# U^3 plus <-2>; E8(-1)^2 is orthogonal and each involution is -I there.
G = [[0]*7 for _ in range(7)]
for i in (0, 2, 4):
    G[i][i+1] = G[i+1][i] = 1
G[6][6] = -2
v1 = [1, 1, 0, 0, 0, 1, 0]
v2 = [1, 15, 1, -14, 0, 15, 0]
a = [0, 0, 0, 0, 2, -6, 1]
v3 = [a[i]-v1[i]+v2[i] for i in range(7)]
V = transpose([v1, v2, v3])
H = [[2 if i == j else 16 for j in range(3)] for i in range(3)]
assert matmul(matmul(transpose(V), G), V) == H
W = transpose([v1, v2, a])
assert det([W[i] for i in (0, 2, 6)]) == 1
assert pairing(a, a, G) == -26
assert reduce(gcd, (abs(x) for row in matmul([a], G) for x in row)) == 2
assert [x % 2 for x in a] == [0, 0, 0, 0, 0, 0, 1]
actions = []
for v in (v1, v2, v3):
    row = matmul([v], G)[0]
    A = [[v[i]*row[j]-int(i == j) for j in range(7)] for i in range(7)]
    assert matmul(matmul(transpose(A), G), A) == G
    assert matmul(A, col(v)) == col(v)
    assert matmul(A, A) == ident(7)
    actions.append(A)
P = matmul(matmul(actions[0], actions[1]), actions[2])
assert matmul(P, col(a)) == col(a)
assert rank([[P[i][j]-int(i == j) for j in range(7)] for i in range(7)]) == 6
HN_actions = []
for k in range(3):
    HN_actions.append([[int(i == k)*H[k][j]-int(i == j) for j in range(3)] for i in range(3)])
PN = matmul(matmul(HN_actions[0], HN_actions[1]), HN_actions[2])
assert matmul(P, V) == matmul(V, PN)
assert sum(PN[i][i] for i in range(3)) == 3331
assert det(PN) == 1
assert matmul(PN, [[1], [-1], [1]]) == [[1], [-1], [1]]
assert 1665**2-221*112**2 == 1

# Complete congruence checks used in the infinite chamber argument.
assert 6 not in {x*x % 7 for x in range(7)}
q_half = lambda x: 8*sum(x)**2-7*sum(t*t for t in x)
mod8_solutions = [x for x in product(range(8), repeat=3) if q_half(x) % 8 == 3]
assert mod8_solutions and all(all(t % 2 for t in x) for x in mod8_solutions)
# Polynomial identity: degree two, so coefficients from a basis of samples suffice.
samples = [(0,0,0), (1,0,0), (0,1,0), (0,0,1), (1,1,0), (1,0,1), (0,1,1)]
for x in samples:
    p = [16*sum(x)-14*t for t in x]
    assert p[0]*p[1] == 18*q_half(x)+14*(x[0]-x[1])**2+238*x[2]**2

# A genuinely realized rho=3 anti-symplectic model with no fixed H2 class.
u1 = [1,29,0,0,0,0,0]
u2 = [0,0,1,-58,0,0,0]
w = [0,0,0,0,1,-29,0]
U = transpose([u1,u2,w])
assert matmul(matmul(transpose(U),G),U) == [[58,0,0],[0,-116,0],[0,0,-58]]
assert det([U[i] for i in (0,2,4)]) == 1
U0 = transpose([u1,u2])
C = [[58,-41],[41,-29]]
correction = matmul(matmul(matmul(U0,C),transpose(U0)),G)
Qaction = [[correction[i][j]-int(i == j) for j in range(7)] for i in range(7)]
assert matmul(matmul(transpose(Qaction),G),Qaction) == G
assert matmul(Qaction,U) == matmul(U,[[3363,4756,0],[2378,3363,0],[0,0,-1]])
assert det([[Qaction[i][j]-int(i == j) for j in range(7)] for i in range(7)]) != 0

# Sparse two-variable polynomials with exact rational coefficients.
def clean(p):
    return {k:Q(v) for k,v in p.items() if v}
def add(p,q):
    r = dict(p)
    for k,v in q.items():
        r[k] = r.get(k,Q(0))+v
    return clean(r)
def scale(p,c):
    return clean({k:c*v for k,v in p.items()})
def multiply(p,q):
    r = {}
    for (i,j),v in p.items():
        for (k,l),w0 in q.items():
            r[i+k,j+l] = r.get((i+k,j+l),Q(0))+v*w0
    return clean(r)
def power(p,n):
    r = {(0,0):Q(1)}
    for _ in range(n):
        r = multiply(r,p)
    return r
def homogeneous(p,n):
    return clean({k:v for k,v in p.items() if sum(k) == n})
def paired_todd(p):
    r = {(0,0):Q(1)}
    for n,c in [(2,Q(-1,12)),(4,Q(1,240)),(6,Q(-1,6048))]:
        r = add(r,scale(power(p,n),c))
    return r
x = {(1,0):Q(1)}
y = {(0,1):Q(1)}
z = scale(add(x,y),-1)
b = add(add(multiply(x,y),multiply(x,z)),multiply(y,z))
c = multiply(multiply(x,y),z)
td = multiply(multiply(paired_todd(x),paired_todd(y)),paired_todd(z))
td6 = scale(add(scale(power(b,3),31),scale(power(c,2),-1)),Q(1,30240))
assert homogeneous(td,6) == td6
assert homogeneous(power(paired_todd(x),2),4) == {(4,0):Q(11,720)}
sixfold_euler = {"K3^[3]":3200,"Kummer_6":448,"OG6":1920}
residues = {k:v % 31 for k,v in sixfold_euler.items()}
assert residues == {"K3^[3]":7,"Kummer_6":14,"OG6":29}
assert (4*30240) % 31 == 29

result = dict(all_checks_passed=True,
    exceptional_model=dict(gram=H, basis_v1=v1,basis_v2=v2,basis_v3=v3,
                          stable_candidate=a,square=-26,full_lattice_divisibility=2,
                          action_on_NS=PN,trace=3331,fixed_H2_dimension=1,
                          entropy_eigenvalue="1665+112*sqrt(221)",
                          common_chamber_mod8_cases=len(mod8_solutions)),
    excluded_rho3_model=dict(gram=[[58,0,0],[0,-116,0],[0,0,-58]],fixed_H2_dimension=0),
    Todd_sixfold_formula="(31*b^3-c^2)/30240 when c1(E)=0",
    necessary_Euler_residue=29,sixfold_Euler_residues=residues,
    sharp_growth_torus=dict(B=[[2,1],[1,1]],S=[[1,1],[0,1]],
        limitation="Exponent 2 log(lambda) verified analytically by spectral projections in note 46, not by this script."),
    limitation="Exact arithmetic/polynomial checks only. Common chamber, actual Torelli realization and derivative implications require the proofs in notes 46--48. No invariant splitting or Anosov system is constructed on the IHS models.")
(root / "normalizer_generalization_checks.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2))
