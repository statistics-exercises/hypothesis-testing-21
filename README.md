# Comparing means (again)

In this final task, we are going to repeat what we did in the previous exercise once more but we will make it more realistic in two regards:

1. I am not going to give you the values of the standard deviations for the two distributions that were sampled from.  You will thus need to estimate the two sample variances from the data set.
2. We are going to do a one-tail rather than a two-tail test.  We can thus use this method to test a hypothesis like the one I introduced in the previous exercise; namely, that on average women are paid less than men.  

With that in mind, the file `mydata.dat` contains two columns.  The first column is a set of samples from one distribution, while the second column samples from a second different distribution.  Your task is to test whether the expectation of the first distribution is less than the expectation of the second distribution.  As in the previous exercise, you will need to compute the following test statistic:

![](https://render.githubusercontent.com/render/math?math=T=\frac{\frac{1}{n_1}\sum_{i=1}^{n_1}X_i-\frac{1}{n_2}\sum_{j=1}^{n_2}Y_j-\theta_0}{\sqrt{\frac{\sigma_1^2}{n_1}%2B\frac{\sigma_2}{n_2}}})

 At variance with the previous exercise, however, you will need to estimate the two standard deviations (![](https://render.githubusercontent.com/render/math?math=\sigma_1) and ![](https://render.githubusercontent.com/render/math?math=\sigma_2)) by computing the sample variances:
 
 ![](https://render.githubusercontent.com/render/math?math=\sigma^2=\frac{n}{n-1}\left[\frac{1}{n}\sum_{i=1}^{n}X_i^2-\left(\frac{1}{n}\sum_{i=1}^{n}X_i\right)^2\right])

To get you started on this task I have written two functions for you to complete:

1. `testStatistic` - this function takes two  NumPy arrays in input:  `data1` that contains the samples from the first distribution and `data2` contains the samples from the second distribution.  This function should return the test statistic, T, that is defined using the formula above.   You will also need to compute the two sample variances in this function.  
2. `pvalue` - this function takes two  NumPy arrays in input:  `data1` that contains the samples from the first distribution and `data2` contains the samples from the second distribution.   To complete the task you must use the value of the `testStatistic` to calculate the p-value.  The p-value should then be returned.

As a final point, notice that different numbers of samples have been taken from the two distributions that the test is being run on.  It should be clear, from the formulas above that this is not a big problem for this kind of test.   
