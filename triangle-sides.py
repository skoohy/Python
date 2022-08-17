print("Type 'exit' to quit")
print("c is the hypotenuse \n")

while True:
    prompt = input("Are you looking for a, b, c or exit: ")
    
    if prompt == 'a':
        b = float(input("Length of side b: "))
        c = float(input("Length of side c: "))
        a = (c**2 - b**2)**(1/2)
        print(f'Length of side a is {a} \n')
        
    elif prompt == 'b':
        a = float(input("Length of side ba: "))
        c = float(input("Length of side c: "))
        b = (c**2 - a**2)**(1/2)
        print(f'Length of side b is {b} \n')
        
    elif prompt == 'c':
        a = float(input("Length of side a: "))
        b = float(input("Length of side b: "))
        c = (a**2 + b**2)**(1/2)
        print(f'Length of side c is {c} \n')
        
    elif prompt == 'exit':
        break
        
    else:
        raise ValueError("Please choose 'a', 'b', or 'c' ")