print("We treat the first catalan number, n=0, as the 1st number not the 0th \n")

def fac(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial

def nCr(n, r):
    return fac(n) / (fac(n-r) * fac(r))

def catalan(n):
    return int((1 / (n+1)) * nCr(2*n, n))

while True: 
    x = int(input("Which catalan number are you looking for: "))
    print(catalan(x-1),"\n")

    prompt = input("Continue? ")
    if prompt == 'no':
        break
    elif prompt == 'yes':
        print()
        continue
    else:
        raise ValueError("Statement must be 'yes' or 'no'")