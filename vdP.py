# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:13:19 2019
@author: Hezy Amiel
"""

"""
find the sheet resistance Rs from R1 = R_AB,CD and R2 = R_BC,AD
the solution is from the equation in a paper L. J. van der Pauw "A method of measuring the resistivity and hall coefficients of Lamellae of arbitrary shape", Philips Technical Review, Vol 26, 220.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# these are the resistance R_AB,CD and R_BC,AD respectivly
R1 = 65
R2 = 89

# define the equation
def fun(Rs):
    return np.exp(-np.pi*R1/Rs) + np.exp(-np.pi*R2/Rs) - 1
     
# plot the fuction
Rs = np.linspace (0, 10*np.sqrt(R1*R2), 200)
# Rs = np.linspace (0, 10000, 200)
plt.plot(Rs,fun(Rs))
plt.axhline(color = "r")
plt.show()

# find the solution
root = optimize.root(fun, [1])

print (root)
