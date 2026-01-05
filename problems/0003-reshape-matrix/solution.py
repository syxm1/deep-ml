import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
        return []
    
    reshaped_matrix = [[] for i in range(new_shape[0])]

    k = 0
    l = 0
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            reshaped_matrix[i].append(a[k][l])
            l += 1
            if l >= len(a[0]):
                k += 1
                l %= len(a[0])

	return reshaped_matrix