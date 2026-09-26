import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.ndim != v2.ndim or (np.linalg.norm(v1)==0 or np.linalg.norm(v2)==0) or v1.size==0 or v2.size==0:
		return 

	dot_prod= np.dot(v1,v2) 
	l2_v1= np.sqrt(sum([x*x for x in v1]))
	l2_v2= np.sqrt(sum([x*x for x in v2]))

	return dot_prod/ (l2_v1 * l2_v2)
