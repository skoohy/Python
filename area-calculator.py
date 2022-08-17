import numpy as np

print("To exit console type 'exit'")

shape = input("Enter 2D shape (Max 10 sides): ")

while True:
    if shape == 'circle':
        r = float(input("Radius: "))
        print(f'Area = {np.pi * r**2}')
        
    elif shape == 'square':
        s = float(input("Side Length: "))
        print(f'Area = {s**2}')
        
    elif shape == 'rectangle':
        l = float(input("Length: "))
        w = float(input("Width: "))
        print(f'Area = {l*w}')
        
    elif shape == 'trapezoid':
        a = float(input("Base 1: "))
        b = float(input("Base 2: "))
        h = float(input("Height: "))
        print(f'Area = {(1/2)*(a+b)*h}')
        
    elif shape == 'triangle':
        b = float(input("Base: "))
        h = float(input("Height Perpendicular to the Height: "))
        print(f'Area = {(1/2)*b*h}')
        
    elif shape == 'rhombus':
        d1 = float(input("Diagonal 1: "))
        d2 = float(input("Diagonal 2: "))
        print(f'Area = {(1/2)*d1*d2}')
        
    elif shape == 'pentagon':     
        a = float(input("Side Length (Regular Pentagon): "))
        print(f'Area = {(1/4)*np.sqrt(5*(5+2*np.sqrt(5)))}')
        
    elif shape == 'hexagon':
        a = float(input("Side Length (Regular Hexagon): "))
        print(f'Area = {(3/2)*(np.sqrt(3))*(a**2)}')
        
    elif shape == 'heptagon':    
        a = float(input("Side Length (Regular Heptagon): "))
        print(f'Area = {(7/4)*(a**2)*(1/np.tan(np.pi/7))}')
        
    elif shape == 'octogon':
        a = float(input("Side Length (Regular Octogon): "))
        print(f'Area = {2*(1+np.sqrt(2))*(a**2)}')
        
    elif shape == 'nonagon':        
        a = float(input("Side Length (Regular Nonagon): "))
        print(f'Area = {(9/4)*(a**2)*(1/np.tan(np.pi/9))}')
        
    elif shape == 'decagon':    
        a = float(input("Side Length (Regular Nonagon): "))
        print(f'Area = {(5/2)*(a**2)*np.sqrt(5+2*(np.sqrt(5)))}')
    
    else:
        raise ValueError("Please enter ")

             
        
        
        
        
        
        