from fractions import Fraction
def safefrac(a,b):
    if b == 0: 
        return Fraction(2,1)
    return Fraction(a,b)

acc = Fraction(1,1)
for a in range(10,100):
    for b in range(a+1,100):
        a1,a2 = [int(i) for i in list(str(a))]
        b1,b2 = [int(i) for i in list(str(b))]
        #print(f"{a} {b}")
        if a1 == b1 == 0 or a2 == b2 == 0:
            #print("continued")
            continue
#        if a1 == b1 and safefrac(a2,b2) == Fraction(a,b):
#            print(f"{a}/{b}")
#            continue
#        if a1 == b2 and safefrac(a2,b1) == Fraction(a,b):
#            print(f"{a}/{b}")
#            continue
        if a2 == b1 and safefrac(a1,b2) == Fraction(a,b):
            print(f"{a}/{b}")
            acc = acc * Fraction(a,b)
            continue
#        if a2 == b2 and safefrac(a1,b1) == Fraction(a,b):
#            print(f"{a}/{b}")
#            continue
#

print(acc)


            
