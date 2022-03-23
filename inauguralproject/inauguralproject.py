def u(z, v = -2):
    """
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
    
    return p*u(y-x+q-pi) + (1-p)*u(y-pi)