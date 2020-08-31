#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A script to test the solvers.py using the problems.py

@author: ajayraj
"""

from problems import Dahlquist
from solvers import explicitEuler

import unittest

class TestSum(unittest.TestCase):
    def test1D(self):
        """
        Test that the explicitEuler works for 1D problem
        """
        tEnd = 2
        h = 0.005
        A = 1
        x0 = 5
        prob = Dahlquist(A,x0)
        solution, path = explicitEuler(prob.ode,x0,tEnd,h)
        analSol = prob.analytical(tEnd)
        self.assertAlmostEqual(analSol, solution, places=5)
        
    

if __name__ == "__main__":
    unittest.main()


