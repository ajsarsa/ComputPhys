import numpy as np


def snell_law(n1, n2, theta1):
    '''
    Ley de Snell, calcula el angulo de refracción

    n1: refraction index
    n2: refraction index
    theta1: incidence angle

    return theta2: refraction angle    
    '''

    stheta2 = n1*np.sin(theta1)/n2

    return np.arcsin(stheta2)
