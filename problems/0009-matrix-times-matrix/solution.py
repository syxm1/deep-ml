import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    
    try:
        multiplied = np.matmul(a, b)
    except:
        multiplied = -1
    
    return multiplied