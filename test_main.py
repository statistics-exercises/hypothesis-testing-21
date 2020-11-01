import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_testStatistic(self) : 
        N1, N2 = len(data1), len(data2)
        mu1, mu2 = sum(data1) / N1,  sum(data2) / N2
        sigma21 = ( N1 / (N1-1) )*( sum(data1*data1) / N1 - mu1*mu1 )
        sigma22 = ( N2 / (N2-1) )*( sum(data2*data2) / N2 - mu2*mu2 )
        stat = ( mu1 - mu2 ) / np.sqrt( sigma21 / N1  + sigma22 / N2 )
        self.assertTrue( np.abs( stat - testStatistic( data1, data2 ) )<1e-7, "the test statistic has not been computed correctly" )
        
    def test_pvalue(self) : 
        myt = testStatistic( data1, data2 )
        pval = scipy.stats.norm.cdf( myt )
        self.assertTrue( np.abs( pval - pvalue( data1, data2 ) )<1e-7, "your function for computing the p-value does not work" )
