def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		means = [0 for i in range(len(matrix))]

		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				means[i] += matrix[i][j]
			
			means[i] /= len(matrix[0])

	if mode == 'column':
		means = [0 for i in range(len(matrix[0]))]

		for j in range(len(matrix[0])):
			for i in range(len(matrix)):
				means[j] += matrix[i][j]

			means[j] /= len(matrix)

	return means
