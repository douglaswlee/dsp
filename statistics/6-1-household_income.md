[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

Import the needed modules
```python
import hinc
import hinc2
import thinkstats2
import thinkplot
import numpy as np
```
Read in the income data
```python
df = hinc.ReadData()
```
Next, I created a function to evaluate, for a particular value of `log_upper`(the log upper bound of the highest range of incomes), the mean, median, skewnesss, Pearson's median skewness, and the perecentage of incomes at or below the mean:
```python
def describe_inc_dist(log_upper):
    log_sample = hinc2.InterpolateSample(df, log_upper=j)
    incomes = np.power(10, log_sample)

    inc_mean = thinkstats2.Mean(incomes)
    inc_med = thinkstats2.Median(incomes)
    inc_skew = thinkstats2.Skewness(incomes)
    inc_pearskew = thinkstats2.PearsonMedianSkewness(incomes)
    print('log_upper = ', j)
    print('Mean Income: ', inc_mean)
    print('Median Income: ', inc_med)
    print('Skewness: ', inc_skew)
    print('Pearson Median Skewness: ', inc_pearskew)

    cdf = thinkstats2.Cdf(incomes)
    inc_below_mean = cdf.Prob(inc_mean)
    print('Pct. below mean: ', inc_below_mean)  
```
The first block in the function above generates the sample of log10 incomes and from this sample, the actual incomes using `np.power`. The second block collects/prints the mean, median, skewness, and Pearson's median skewness from the sample. The third block creates a cdf from the sample and collects/prints the percentage of incomes at or below the mean. Looping several values of `log_upper` as inputs to the above:
```python
for j in [6.0, 7.0, 8.0]:
    describe_inc_dist(log_upper = j)
```
Provides the following output:
```python
log_upper =  6.0
Mean Income:  74278.7075312
Median Income:  51226.4544789
Skewness:  4.94992024443
Pearson Median Skewness:  0.736125801914
Pct. below mean:  0.660005879567

log_upper =  7.0
Mean Income:  124267.397222
Median Income:  51226.4544789
Skewness:  11.6036902675
Pearson Median Skewness:  0.391564509277
Pct. below mean:  0.856563066521

log_upper =  8.0
Mean Income:  457453.487247
Median Income:  51226.4544789
Skewness:  14.8924598044
Pearson Median Skewness:  0.274790973381
Pct. below mean:  0.978629407634
```
For each level of `log_upper` the mean is larger than the median (which remains constant across the cases), both skewness measures are positive, and the percentage below the mean is greater than 50% -- so the distributions clearly skew right. As one would expect, increasing the value of `log_upper` increases the degree to which the mean is greater than the median as well as the skewness and the percentage of incomes below the mean. Pearson's median skewness, however, decreases as `log_upper` increases, which seems a bit unexpected, but perhaps this measure does not describe the distribution that well?
