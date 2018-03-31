[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

Import the needed modules
```python
import first
import hypothesis
import thinkplot
import thinkstats2
import numpy as np
```
Write the class `DiffMeansResample` inheriting from `hypothesis.DiffMeansPermute` and overriding the function `RunModel` below:
```python
class DiffMeansResample(hypothesis.DiffMeansPermute):

    def RunModel(self):
        group1 = np.random.choice(self.pool, self.n, replace=True)
        group2 = np.random.choice(self.pool, self.m, replace=True)
        return group1, group2
```
Read in the pregnancy data and test the difference in means, using the above, for pregnancy length `prglngth` and birth weight `totalwgt_lb` between first and other babies:
```python
live, firsts, others = first.MakeFrames()

data1 = firsts.prglngth.values, others.prglngth.values
ht1 = DiffMeansResample(data1)
p_prglngth = ht1.PValue()

data2 = firsts.totalwgt_lb.dropna().values, others.totalwgt_lb.dropna().values
ht2 = DiffMeansResample(data2)
p_totalwgt_lb = ht2.PValue()
```
The p-values from testing the difference in means for `prglngth` and `totalwgt_lb` between first and other babies are:
```python
p_prglngth
```
```python
0.168
```
```python
p_totalwgt_lb
```
```python
0
```
Compared to those reported in the text for `DiffMeansPermute` (0.17 for `prglngth` and 0 for `totalwgt_lb`), using resampling to compare the means for these measures between the two groups is not really different.
