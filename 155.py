from fractions import Fraction
from typing import Set

def parallel(C1 : Fraction, C2 : Fraction) -> Fraction:
    return C1 + C2

def series(C1 : Fraction, C2 : Fraction) -> Fraction:
    return 1/(1/C1 + 1/C2)

cache = {1:{Fraction(1)}}

def F(n : int) -> Set[Fraction]:
    if n in cache.keys():
        return cache[n]

    print(n)
    res = set() 
    for i in range(1,n):
        for a in F(i):
            for b in F(n-i):
                res = res | {parallel(a,b), series(a,b)}
        res = res | F(i)


    cache[n] = res
    return res

def D(n : int) -> int:
    return len(F(n))

for i in range(1,4):
    print(f"{i}:{D(i)}")

print(D(18))
