import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)

        f(x)= g(x) / h(x)

        f'(x)= g'(x). h(x) - g(x). h'(x) / h(x)^2
    """
    def hx(h_coeffs,x):

        h=0
        max_power= len(h_coeffs)-1
        for coeff in h_coeffs:
            h+= coeff*(x**max_power)
            max_power-=1

        return h


    def gx(g_coeffs, x):
        g=0
        max_power= len(g_coeffs)-1
        for coeff in g_coeffs:
            g+= coeff*(x**max_power)
            max_power-=1

        return g

    def deriv_g(g_coeffs, x):
        
        deriv=0
        max_power=len(g_coeffs)-1

        for coeff in g_coeffs[:-1]:
            deriv+= coeff*max_power*(x**(max_power-1))
            max_power-=1
            
        return deriv
    
    def deriv_h(h_coeffs,x):
        #if len =2 then max power is x^1
        #if len=3 then max power is x^2 

        deriv=0
        max_power=len(h_coeffs)-1

        for coeff in h_coeffs[:-1]:
            deriv+= coeff*max_power*(x**(max_power-1))
            max_power-=1

        return deriv

    return ((deriv_g(g_coeffs, x) * hx(h_coeffs,x)) - (deriv_h(h_coeffs,x) * gx(g_coeffs, x)))/ (hx(h_coeffs,x)**2)
    