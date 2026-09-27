import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """

    # m is the number of rows, and training examples  
    #and n is the number of columns and features (variables that affect the output )
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros
    X_T= X.T

    for i in range(iterations):
        pred= X @ theta 
        error= pred-y
        gradient= (1/m)* (X_T@ error)
        theta= theta-(alpha*gradient)

    #flattens matrices, in this case the weights into a single dimension
    return theta.flatten()