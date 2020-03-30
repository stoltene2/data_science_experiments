import numpy as np

def successive_poisson(tau1, tau2, size=1):
    """Compute the time for arrival of two successive Poisson processes"""
    t1 = np.random.exponential(tau1, size=size)
    t2 = np.random.exponential(tau2, size=size)
    return t1 + t2
