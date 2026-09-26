def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here

	return [list([x*scalar for x in row]) for row in matrix]