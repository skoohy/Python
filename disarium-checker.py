def is_disarium(n):
    digits, disarium = [int(a) for a in str(n)], 0
    for num in range(1, len(digits)+1):
        disarium += digits[num-1]**num
    if disarium == n:
        return True
    else:
        return False
    
for n in range(0, 501):
    print(f'Is {n} a Disarium number? {is_disarium(n)}')
