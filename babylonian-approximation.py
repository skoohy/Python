from numpy import sqrt

def babylonian(S):
    if S < 0:
        raise ValueError("n must be positive")
    elif S == 0:
        return 0
    x = S/2 # Initial guess of square root
    i = 0
    while i <= 50:
        x = (x + S/x) / 2
        i += 1
    return x

while True:
    x = float(input("Enter number for babylonian approximation: "))
    print(f'Babylonian approximation: {babylonian(x)}')
    print(f'Numpy approximation:      {sqrt(x)}\n')
    
    prompt = input("Continue? ")
    if prompt == 'no':
        break
    elif prompt == 'yes':
        print()
        continue
    else:
        raise ValueError("Statement must be 'yes' or 'no'")
