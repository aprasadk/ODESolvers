#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script with test problems for the solvers

@author: ajayraj
"""

import numpy as np

class Dahlquist():
    """
    Class of Dahlquist problems x_dot = -A*x
    """
    def __init__(self,A, x0):
        self.A = A
        self.x0 = x0
        
    def ode(self,t,x):
        return -self.A*x
    
    def analytical(self,tEnd):
        try:
            _ = self.x0.size
            return np.exp(-self.A*tEnd)@self.x0
        
        except AttributeError:
            return np.exp(-self.A*tEnd)*self.x0