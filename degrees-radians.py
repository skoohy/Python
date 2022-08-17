import numpy as np

print("To exit console type 'exit'")

while True:
    prompt = input("Convert to: ").lower()

    if prompt == 'degrees':
        radians = float(input("Enter Radians: "))
        if str(radians) == 'exit':
            exit
        else:
            print(f'{radians} to degrees is {radians*(180/np.pi)}°')

    elif prompt == 'radians':
        degrees = float(input("Enter Degrees: "))
        print(f'{degrees}° to radians is {degrees*(np.pi/180)}')

        
    elif prompt == 'exit':
        break
        
    else:
        raise ValueError("Please enter 'Degrees'/'degrees' or 'Radians'/'radians'")
    
    
    
    
    
    
    
    
    