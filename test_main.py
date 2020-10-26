import numpy as np
import unittest
import scipy.stats as st
import main

class UnitTests(unittest.TestCase) :
    def test_mean(self) : 
        for i in range(1,9) : 
            p, mean = i*0.1, 0
            for j in range(100) : mean = mean + bernoulli(0.5)
            mean = mean / 100
            bar = np.sqrt(0.25/100)*st.norm.ppf( (0.99 + 1) / 2 )
            self.assertTrue( np.fabs( mean - p )<bar, "The function does not appear to be generating the random variable correctly" )
