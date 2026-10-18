"""Exact arithmetic certificates for notes 49--50; no numerical dynamics simulation."""
from fractions import Fraction as Q
from functools import reduce
from itertools import product, combinations
from math import gcd
from pathlib import Path
import json

root=Path(__file__).resolve().parent
def tr(a): return list(map(list,zip(*a)))
def mul(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def matpow(a,n):
    r=eye(len(a))
    for _ in range(n): r=mul(r,a)
    return r
def inv(a):
    n=len(a)
    b=[[Q(v) for v in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        k=next(i for i in range(j,n) if b[i][j])
        b[k],b[j]=b[j],b[k]
        c=b[j][j];b[j]=[x/c for x in b[j]]
        for i in range(n):
            if i!=j:
                c=b[i][j];b[i]=[x-c*y for x,y in zip(b[i],b[j])]
    return [r[n:] for r in b]
def det(a):
    if len(a)==2: return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    if len(a)==3: return sum((-1)**j*a[0][j]*det([[a[i][k] for k in range(3) if k!=j] for i in (1,2)]) for j in range(3))
    raise ValueError("only orders two and three needed")
def mod(a,p): return [[int(v)%p for v in row] for row in a]
G=[[2,16,16],[16,2,16],[16,16,2]]
B=[[1,-15,1],[0,1,-1],[-1,0,1]]
a=[[1],[-1],[1]]
kappa=[[14],[-1],[1]]
R=[[16,16,1],[-1,0,0],[0,-1,0]]
S=[[1,16,16],[0,0,-1],[0,-1,0]]
P=[[3585,3824,240],[-240,-255,-16],[16,16,1]]
C=[[0,1],[-1,15]]
J=[[0,1],[1,0]]
assert det(B)==-13
assert mul(mul(tr(B),G),B)==[[-28,210,0],[210,-28,0],[0,0,-26]]
assert mul(inv(B),[[1],[0],[0]])==[[Q(-1,13)],[Q(-1,13)],[Q(-1,13)]]
assert mul(mul(tr(kappa),G),kappa)==[[364]]
assert mul(mul(tr(kappa),G),a)==[[0]]
for A in (R,S):
    assert mul(mul(tr(A),G),A)==G
    assert mul(A,a)==a
assert det(R)==1 and det(S)==-1
assert matpow(R,3)==P and matpow(S,2)==eye(3)
assert mul(mul(S,R),S)==inv(R)

entries_gcd=reduce(gcd,(abs(v) for row in G for v in row))
minor_gcd=reduce(gcd,(abs(det([[G[i][j] for j in cols] for i in rows]))
                     for rows in combinations(range(3),2) for cols in combinations(range(3),2)))
smith=[entries_gcd,minor_gcd//entries_gcd,abs(det(G))//minor_gcd]
assert smith==[2,14,238]
assert inv(G)==[[Q(8-17*int(i==j),238) for j in range(3)] for i in range(3)]
assert mod(matpow(C,13),13)==eye(2)
assert all(mod(matpow(C,k),13)!=eye(2) for k in range(1,13))
assert mod(mul(C,[[1],[1]]),13)==[[1],[1]]
assert mul(J,[[1],[1]])==[[1],[1]]
gluing_cases=0
for k in range(13):
    for flip in (False,True):
        A=matpow(C,k)
        if flip: A=mul(A,J)
        for nu in (1,-1):
            D=[[A[0][0],A[0][1],0],[A[1][0],A[1][1],0],[0,0,nu]]
            full=mul(mul(B,D),inv(B))
            integral=all(v.denominator==1 for row in full for v in row)
            assert integral==(nu==1)
            gluing_cases+=1
V7=[[1,0],[-1,1],[0,-1]]
RD=[[0,1],[-1,1]]
SD=[[-1,0],[-1,1]]
assert mod(mul(G,V7),7)==[[0,0],[0,0],[0,0]]
assert mod(mul(R,V7),7)==mod(mul(V7,RD),7)
assert mod(mul(S,V7),7)==mod(mul(V7,SD),7)
assert mod(matpow(RD,6),7)==eye(2)
assert mod(matpow(RD,3),7)==[[6,0],[0,6]]
for k in range(6):
    T=mod(mul(matpow(RD,k),SD),7)
    assert (T[0][0]+T[1][1])%7==0 and det(T)%7==6
assert mod(mul(G,[[1],[1],[1]]),17)==[[0],[0],[0]]
assert mod(mul(R,[[1],[1],[1]]),17)==[[16],[16],[16]]
order_table=[]
for k in range(6):
    d7=6//gcd(6,k)
    d17=1 if k%2==0 else 2
    order_table.append(dict(k_mod_6=k,order_at_7=d7,order_at_17=d17,
                            compatible=(k%3==0),forced_order=d17 if k%3==0 else None))

# Rational polynomial identities in p,c.
def clean(p): return {k:Q(v) for k,v in p.items() if v}
def add(p,q):
    r=dict(p)
    for k,v in q.items(): r[k]=r.get(k,Q(0))+v
    return clean(r)
def scale(p,c): return clean({k:c*v for k,v in p.items()})
def pmul(p,q):
    r={}
    for (i,j),v in p.items():
        for (k,l),w in q.items(): r[i+k,j+l]=r.get((i+k,j+l),Q(0))+v*w
    return clean(r)
def sq(p): return pmul(p,p)
def constant(v): return {(0,0):Q(v)} if v else {}
p={(1,0):Q(1)}
c={(0,1):Q(1)}
zlag=add(scale(p,-2),scale(c,-22))
elag=add(add(scale(sq(p),4),scale(sq(zlag),2)),scale(sq(c),44))
assert add(elag,scale(sq(c),Q(-1100,3)))==scale(sq(add(p,scale(c,Q(22,3)))),12)
zsym=scale(add(scale(p,2),scale(c,20)),Q(-1,3))
esym=add(add(scale(sq(zsym),6),scale(sq(p),4)),scale(sq(c),40))
c2sym=scale(zsym,-60)
E={(2,0):Q(5),(1,1):Q(40),(0,2):Q(230),(1,0):Q(-30),(0,1):Q(-300),(0,0):Q(18)}
assert add(add(c2sym,constant(-24)),scale(esym,-1))==scale(E,Q(-4,3))
U=scale(add(add(p,scale(c,4)),constant(-3)),Q(5,9))
V=scale(add(scale(c,5),constant(-3)),Q(1,9))
assert add(add(sq(U),scale(sq(V),30)),constant(-5))==scale(E,Q(5,81))
conic_mod9=[(m,n,k) for m,n,k in product(range(9),repeat=3) if (m*m+30*n*n-5*k*k)%9==0]
assert len(conic_mod9)==27 and all(all(v%3==0 for v in triple) for triple in conic_mod9)

# Cohomological Lefschetz values, checked directly from the integral P matrix.
fixed_counts=[]
for n in range(1,9):
    Pn=matpow(P,n);P2n=matpow(P,2*n)
    tn=sum(Pn[i][i] for i in range(3))+20*(-1)**n
    t2n=sum(P2n[i][i] for i in range(3))+20
    Sn=sum(Pn[i][i] for i in range(3))-1
    L=2+2*tn+(tn*tn+t2n)//2
    formula=Sn*Sn+(3+20*(-1)**n)*Sn+214+60*(-1)**n
    assert L==formula and L>0
    if n<=3: fixed_counts.append(dict(n=n,L=str(L)))
assert fixed_counts[0]["L"]=="11032444"

result=dict(all_checks_passed=True,
    normalizer=dict(NS_generator_R=R,formal_reverser_S=S,Smith_invariants=smith,
                    index_H_plus_a=13,complete_mod13_gluing_cases=gluing_cases,
                    discriminant_R_at_7=RD,discriminant_S_at_7=SD,
                    R_at_17=-1,order_table=order_table,
                    scope="Arithmetic verified. Pell-unit exhaustion, simple-Hodge cyclotomic purity, equivariant gluing and H2 faithfulness are mathematical inputs/proofs, not established by finite checks."),
    geometry=dict(ample_axis_class=[14,-1,1],BBF_square=364,
                  Lagrangian_completed_square="e - 1100*c^2/3 = 12*(p+22*c/3)^2",
                  symplectic_K3_conic="U^2+30*V^2=5",complete_mod9_solutions=len(conic_mod9),
                  fixed_point_intersection_totals=fixed_counts,
                  scope="No periodic multipliers or Anosov property were computed. Fixed-point totals include local intersection multiplicities."),
    limitation="Exact auxiliary matrix and polynomial checks only; complete proofs and the very-general restriction for the non-Lagrangian surface exclusion are in notes 49--50.")
(root/"boundary_normalizer_and_surface_checks.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2))
