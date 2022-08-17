def aliquot_sum(n):
    if type(n) == str:
        raise ValueError("n must be an integer")
    elif n <= 0:
        raise ValueError("n must be positive")
    elif n != int(n):
        raise ValueError("n must be an integer")
    else:
        proper_divisors = 0
        for x in range(1, n):
            if n % x == 0:
                proper_divisors += x
    return proper_divisors

for n in range(1, 101):
    print(f'n: {n} | Aliquot Sum: {aliquot_sum(n)}')