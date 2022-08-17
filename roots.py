""" Find roots of quadratic given coefficients"""

from numpy import sqrt as sqrt
from cmath import sqrt as csqrt

def roots(a, b, c):
    if b**2 - 4*a*c > 0:
        x1 = -1*b + sqrt(b**2 - 4*a*c) / 2*a
        x2 = -1*b - sqrt(b**2 - 4*a*c) / 2*a
        print("2 real roots: ", end='')
        return [x1, x2]
    elif b**2 - 4*a*c == 0:
        x1 = -1*b + sqrt(b**2 - 4*a*c) / 2*a
        print("1 real root, at the vertex: ", end='')
        return x1
    elif  b**2 - 4*a*c < 0:
        x1 = -1*b + csqrt(b**2 - 4*a*c) / 2*a
        x2 = -1*b - csqrt(b**2 - 4*a*c) / 2*a
        print("2 imaginary roots: ", end='')
        return [x1, x2]
    
while True:
    print("Enter coefficients \n")
    a = float(input("a: "))
    if a == 0:
        raise ValueError("'a' must be nonzero")
    b = float(input("b: "))
    c = float(input("c: "))
    print(roots(a,b,c),"\n")
    
    prompt = input("Continue? ")
    if prompt == 'no':
        break
    elif prompt == 'yes':
        print()
        continue
    else:
        raise ValueError("Statement must be 'yes' or 'no'")
    
    
    
    
    
    
    
    
    
    