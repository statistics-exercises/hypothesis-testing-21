import numpy as np
import scipy.stats 

def testStatistic( data1, data2 ) :
  # This function should calcualte and return the test statistic T that is 
  # described in the panel on the right.  Notice that you will need to compute 
  # estimates of the two sample variances in order to complete this function.
  

def pvalue( data1, data2 ) : 
  # You need to write code to determine the pvalue here.  This code will need to
  # include a call to test statistic
  
  
data1, data2 = np.loadtxt("mydata1.dat"), np.loadtxt("mydata2.dat")
print("Null hypothesis: the expectations for the two sampled distributions are the same")
print("Alternative hypothesis: the expectation for the distribution that was sampled")
print("to generate the data in the first column is less than")
print("the expectation for the distribution that was sampled to generate the data")
print("in the second column")
print("The p-value for this hypothsis test is", pvalue( data1, data2 ) )
