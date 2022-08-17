def sum_divisors(n):
    if n == 1:
        return 1
    return sum(ni for ni in range(1,n) if n % ni == 0)

while True:
    x = int(input("Find the of sum of all divisors of: "))
    print(sum_divisors(x),"\n")
    
    prompt = input("Continue? ")
    if prompt == 'no':
        break
    elif prompt == 'yes':
        print()
        continue
    else:
        raise ValueError("Statement must be 'yes' or 'no'")