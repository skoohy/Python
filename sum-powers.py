def sum_powers(power, a, b):
    sum_of_powers = 0
    for x in range(a, b+1):
        sum_of_powers += x**power
    return sum_of_powers

print(sum_powers(8, 6, 21))