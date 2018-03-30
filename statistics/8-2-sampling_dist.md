[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

Import the necessary modules
```python
import math
import thinkstats2
import thinkplot
import estimation
import numpy as np
```
I then wrote a function to simulate *n* numbers from the exponential distribution 1000 times for a particular value of `lam` and returns the sampling distibution, standard error (RMSE) and confidence interval for the estimate of `lam`:
```python
def Simulate_Sample(lam, n, m=1000):
    means = []
    medians = []

    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1/np.mean(xs)
        means.append(L)

    cdf = thinkstats2.MakeCdfFromList(means)
    stderr = estimation.RMSE(means, lam)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    return cdf, stderr, ci
```
The following block of code then generates samples for `lam = 2` for values of *n* from 10 to 1000 and collects the sampling distribution, standard error, and confidence intervals for each:
```python
thinkstats2.RandomSeed(1)
ns = np.arange(10, 1000, 10)
stderrs = []
cis = []
cdfs = []
for n in ns:
    cdf, stderr, ci = Simulate_Sample(2, n, m=1000)
    cdfs.append(cdf)
    stderrs.append(stderr)
    cis.append(ci)
```
We plot of the sampling distribution when *n* = 10:
```python
thinkplot.Cdf(cdfs[0])
thinkplot.Show(xlabel='x', ylabel='CumProb')
```
![](https://image.ibb.co/du5dPn/sampling_Q9.png)
This distribution shows that simulating the samples of 10 values many times results in the estimates varying such that over 90% of the estimates would be somewhere between 1 and 4.  
Now let's look at the results for sampling errors and confidence intervals for different values of *n*:  

| n |  Error |     C.I.    |
|:---|---|---|
|10   | 0.820 | (1.303, 3.852) |
|100  | 0.213 | (1.715, 2.414) |
|1000 | 0.062 | (1.902, 2.102) |

It appears that increasing *n*, the number of values in each sample, reduces sampling error and tightens the 90% confidence interval of the estimate. Plotting sampling error against n as below illustrates this relationship:
```python
thinkplot.Plot(ns, stderrs)
thinkplot.Show(xlabel='n', ylabel='Standard Error')
```
![](https://image.ibb.co/eTH04n/error_vs_n_Q9.png)
