import torch

def dice_statistics(n: int) -> tuple[float, float]:
    """
    Compute the expected value and variance of a fair n-sided die roll using PyTorch.

    Args:
        n (int): Number of sides of the die

    Returns:
        tuple: (expected_value, variance)
    """
    # Expected Value is the probability weighted value
	# Variance measures how far each value in the data is from the mean  
    return ((n+1)/2, ((n**2)-1)/12)