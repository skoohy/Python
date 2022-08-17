def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def nCr(n, r):
    if n < r:
        raise ValueError("Requirement not met: n >= r >= 0")
    else:
        return (factorial(n)) / (factorial(r)*factorial(n-r))

def tetrahedral_num(n):
    return nCr(n+2, 3)

for x in range(1, 101):
    print(f'n: {x} | Tetrahedral number: {tetrahedral_num(x)}')