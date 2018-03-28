[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

First, import the needed modules:
```python
import thinkstats2
import thinkplot
import random
```
I wrote a function to generate a list of *n* random numbers from `random.random` (with the usual comments about improving documentation and error handling here):
```python
def rand_list(n):
    rands = [random.random() for _ in range(n)]
    return rands
```
Then I generated 1000 numbers from `random.random` using `rand_list`and constructed their pmf and cdf:
```python
rands = rand_list(1000)
pmf = thinkstats2.Pmf(rands)
cdf = thinkstats2.Cdf(rands)
```
The following plots the pmf and cdf of these generated numbers:
```python
thinkplot.Pmf(pmf)
thinkplot.Show(xlabel = 'x', ylabel = 'pmf')

thinkplot.Cdf(cdf)
thinkplot.Show(xlabel = 'x', ylabel = 'cdf')
```
The pmf shows that the 1000 numbers generated from `random.random` occur on the interval \[0,1) with equal probability of 1/1000, providing evidence that the distribution is uniform on the interval.

<!---
Temporary placeholder image
-->

![](https://image.ibb.co/ftrPAS/pmf_Q3.png)

The cdf is approximately a straight line, also providing evidence that the distribution is uniform on the interval \[0,1).

<!---
Temporary placeholder image
-->

![](https://image.ibb.co/btuEc7/cdf_Q3.png)
