import numpy as np

def ran_numbers(a, b, n):
    return [np.random.randint(a, b+1) for num in range(1, n+1)]

while True:    
    a = int(input("Lower bound: "))
    b = int(input("Upper bound: "))
    if a >= b:
        raise ValueError("'b' must be greater than 'a'")
    n = int(input("Number of elements: "))
    
    nums = ran_numbers(a, b, n)
    
    print(f'List of {len(nums)} random numbers: ', end='')
    for i in range(0, len(nums)-1):
        print(f'{nums[i]}, ', end='')
    print(nums[len(nums)-1], "\n")

    prompt = input("Continue? ")
    if prompt == 'no':
        break
    elif prompt == 'yes':
        print()
        continue
    else:
        raise ValueError("Statement must be 'yes' or 'no'")