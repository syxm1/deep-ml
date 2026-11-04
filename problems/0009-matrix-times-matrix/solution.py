import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	return np.dot(a, b) if np.shape(a)[1] == np.shape(b)[0] else -1