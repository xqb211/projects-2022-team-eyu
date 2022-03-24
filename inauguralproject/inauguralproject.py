import numpy as np
from scipy import random

def u(z, v = -2):
    """
    calculates a utility level given input z and curvature parameter v

    Args:
    
        z: input float on which utility function should be applied on
        v: default=-2, input integer to change curvature of function
        
    Returns:
    
        utility value: function applied to z.
    
    """
    return z**(1+v)/(1+v)

###################################################################

def u_unins(x, y = 1, p = 0.2):
    """

    calculates utility value if not insured

    Args:
    
        x: input float of loss
        p: default=0.2, input float of probability of loss
        
    Returns:
    
        utility value of not being insured
    
    """

    
    return p*u(y-x) + (1-p)*u(y)
###################################################################

def u_ins(q, x, y = 1, p = 0.2, v = -2):
    """

    calculates utility value if being insured

    Args:
    
        q: input float of coverage amount
        x: input float of loss
        y: input float of assets of agent
        p: default=0.2, input float of probability of loss
        v: input integer for curvature of utility function
        
    Returns:
    
        utility value of  being insured
    
    """

    return p*u(y-x+q-p*q,v=v) + (1-p)*u(y-p*q,v=v)


###################################################################
def u_ins_pi(q, pi, x=0.6, y = 1, p = 0.2, v = -2):
    """

    calculates utility value if being insured and you can select pi

    Args:
    
        q: input float of coverage amount
        pi: input float for price of insurance
        x: input float of loss
        y: input float of assets of agent
        p: default=0.2, input float of probability of loss
        v: input integer for curvature of utility function
        
    Returns:
    
        utility value of  being insured with a given pi
    
    """
    
    return p*u(y-x+q-pi, v=v) + (1-p)*u(y-pi, v=v)



def v(gamma, pi):
    """

    calculate utility for given gamma and pi

    Args:
    
        gamma: input float coverage ratio
        pi: input float for price of insurance

        
    Returns:
    
        utility value of  being insured with a given pi and gamma
    
    """
    # array of zeros of length N
    a = 2
    b = 7
    N = 10000
    x = np.zeros(N)

    # iterating over each Value of x and filling it with a random value in beta distribution (a,b)
    np.random.seed(123)
    for i in range (len(x)):
        x[i] = random.beta(a,b)

    #create integral to store utility
    integral = 0

    for i in x:
        y = 1
        z = y - (1 - gamma)*i - pi
        integral += u(z, v=-2)
    
    ans = 1/N*integral 
    return ans  