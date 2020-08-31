# -*- coding: utf-8 -*-
"""
A script of all the solvers
"""

import numpy as np

def explicitEuler(F, y0, tEnd, h):
    
    try:
        dim = y0.size
    except AttributeError:
        dim = 1
    
    steps = int(tEnd/h)
    
    path = np.zeros((dim, steps))
    path[:,0] = y0
    
    for i in range(steps-1):
        path[:,i+1] = path[:,i] + h*F(i*h,path[:,i])
    
    if dim == 1:    
        return path[0,-1], path[0,:]
    return path[:,-1], path
    


