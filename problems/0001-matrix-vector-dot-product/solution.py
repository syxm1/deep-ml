import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	arr = []
	possible = True

	for i in range(len(a)):
		cur = 0

		if (len(a[i]) != len(b)):
			possible = False
			break

		for j in range(len(a[i])):
			cur += a[i][j] * b[j]

		arr.append(cur)
	
	return arr if possible else -1
	