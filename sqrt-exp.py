from numpy import sqrt as sqrt
from numpy import exp as exp

while True:
    x = float(input("Enter number: "))
    print(f'The square root of {x} is : {sqrt(x)}')
    print(f'The exponential of {x} is : {exp(x)} \n')
    
    prompt = input("Continue? ")
    if prompt == 'no':
        break
    elif prompt == 'yes':
        print()
        continue
    else:
        raise ValueError("Statement must be 'yes' or 'no'")