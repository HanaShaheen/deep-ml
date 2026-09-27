import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	def get_dir(gradient):
		mag= get_mag(gradient)
		if mag ==0:
			return [0]*len(gradient)
		directions=[]
		for elem in gradient:
			directions.append(elem/mag)
		return directions

	def get_mag(gradient):
		return np.sqrt(sum([x*x for x in gradient])) 

	def get_descDir(gradient):
		return [-1*elem for elem in get_dir(gradient)]


	return {'magnitude':get_mag(gradient),'direction': get_dir(gradient),'descent_direction': get_descDir(gradient)}
	