import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	matrix= np.array(matrix)
	rows, cols =matrix.shape
	if mode=="column":
		matrix=matrix.T
		return [ sum(elem)/rows for elem in matrix]

	return [ sum(elem)/cols for elem in matrix]