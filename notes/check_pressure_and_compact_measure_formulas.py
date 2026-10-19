"""Finite algebra/sign and model checks only; the analytic proofs are in notes 55-56."""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json
import math

zero=(0,0,0,0)

def basis(indices, variable=None):
    indices=list(indices)
    inversions=sum(a>b for i,a in enumerate(indices) for b in indices[i+1:])
    exponents=list(zero)
    if variable is not None:
        exponents[variable]=1
    return {(sum(1<<i for i in indices),tuple(exponents)):(-1)**inversions}

def add(*forms):
    result=defaultdict(int)
    for form in forms:
        for key,coefficient in form.items(): result[key]+=coefficient
    return {key:value for key,value in result.items() if value}

def scale(form, coefficient):
    return {key:coefficient*value for key,value in form.items() if coefficient*value}

def wedge(left,right):
    result=defaultdict(int)
    for (mask_a,powers_a),coefficient_a in left.items():
        for (mask_b,powers_b),coefficient_b in right.items():
            if mask_a & mask_b: continue
            inversions=sum(1 for i in range(8) if mask_a>>i&1 for j in range(8) if mask_b>>j&1 and i>j)
            powers=tuple(a+b for a,b in zip(powers_a,powers_b))
            result[mask_a|mask_b,powers]+=coefficient_a*coefficient_b*(-1)**inversions
    return {key:value for key,value in result.items() if value}

def product(*forms):
    result={(0,zero):1}
    for form in forms: result=wedge(result,form)
    return result

# Ordered basis: dz1,dz2,dw1,dw2,dbarz1,dbarz2,dbarw1,dbarw2.
# The four formal variables are the coefficients of T1+,T1-,T2+,T2-.
plus=add(basis([0,4],0),basis([2,6],2))
minus=add(basis([1,5],1),basis([3,7],3))
omega=add(basis([0,1]),basis([2,3]))
omega_bar=add(basis([4,5]),basis([6,7]))

# Actual positive (1,1) forms carry i. Four factors give i^4=1;
# the mixed measure has two factors and hence carries i^2=-1.
green_raw=product(plus,plus,minus,minus)
mixed_raw=scale(product(plus,minus,omega,omega_bar),-1)
volume_raw=product(omega,omega,omega_bar,omega_bar)
assert green_raw=={(255,(1,1,1,1)):4}
assert mixed_raw=={(255,(1,1,0,0)):1,(255,(0,0,1,1)):1}
assert volume_raw=={(255,zero):4}
assert product(*([add(plus,minus)]*4))==scale(green_raw,6)

# Exact rational determinant and trace identities for the area-preserving model.
epsilon=Fraction(1,100)
fixed_point_checks=[]
for cosine in (1,-1):
    matrix=[[5+2*epsilon*cosine,2],[2+epsilon*cosine,1]]
    determinant=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    trace=matrix[0][0]+matrix[1][1]
    assert determinant==1 and trace==6+2*epsilon*cosine
    fixed_point_checks.append({'cosine':cosine,'determinant':str(determinant),'trace':str(trace)})
assert fixed_point_checks[0]['trace']!=fixed_point_checks[1]['trace']

# Independent finite-symbol check of both Chernoff signs and the critical threshold.
# This is a numerical illustration, not a proof of the Anosov or IHS theorems.
p=0.8
h=math.log(2)
delta=h/2-math.log(math.sqrt(p)+math.sqrt(1-p))
assert delta>0

def log_binomial_probability(n,k,rare_probability):
    return (math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
            +k*math.log(rare_probability)+(n-k)*math.log1p(-rare_probability))

bernoulli_checks=[]
for n in (10,30,100,300,1000):
    upper=[]
    lower=[]
    for k in range(n+1):
        sum_phi=-(n-k)*math.log(p)-k*math.log(1-p)
        if sum_phi>n*h:
            upper.append(math.exp(log_binomial_probability(n,k,1-p)))
        else:
            lower.append(math.exp(log_binomial_probability(n,k,0.5)))
    m_tail=sum(upper)
    theta_complement=sum(lower)
    bound=math.exp(-delta*n)
    assert m_tail<=bound*(1+1e-10) and theta_complement<=bound*(1+1e-10)
    bernoulli_checks.append({'n':n,'m_tail':m_tail,'theta_complement':theta_complement,'each_chernoff_bound':bound})

result={
    'exact_exterior_algebra':{
        'green_raw_coefficient':4,
        'mixed_raw_coefficients':[1,1],
        'symplectic_volume_raw_coefficient':4,
        'sum_fourth_power_equals_six_green_product':True,
        'interpretation':'Gaussian i factors accounted for explicitly; polynomial coefficients are integers.'
    },
    'exact_fixed_point_derivative_checks':fixed_point_checks,
    'bernoulli_pressure_gap':delta,
    'bernoulli_numerical_checks':bernoulli_checks,
    'scope':'Only finite coefficients, signs and toy-model bounds checked. No Anosov existence at epsilon=1/100, no infinite-dimensional or regularity conclusion is inferred. All analytic and geometric proofs are separate.'
}
path=Path(__file__).with_name('pressure_and_compact_measure_checks.json')
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'exact_exterior_checks':4,'exact_fixed_point_checks':2,'independent_bernoulli_checks':5,'passed':True,'output':str(path)},ensure_ascii=False))
