def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	b = [list() for i in range(len(a[0]))]

	for i in range(len(a[0])):
		for j in range(len(a)):
			b[i].append(a[j][i])
	return b