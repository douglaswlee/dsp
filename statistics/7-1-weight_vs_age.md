[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

Import the needed modules
```python
import thinkstats2
import thinkplot
import first
import numpy as np
```
Read in the pregnancy data for live births, first babies, and other babies:
```python
live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
```
A scatterplot of birth weight vs. mother's age at birth doesn't strongly demonstrate a relationship between the two variables:
```python
thinkplot.LEGEND = False
thinkplot.Scatter(live.agepreg, live.totalwgt_lb)
thinkplot.Show(xlabel = 'Mother\'s age', ylabel = 'Birth weight')
```
![](https://image.ibb.co/iutgS7/scatter_Q7.png)
Calculate both Pearson's and Spearman's Rank Correlation:
```python
rho = thinkstats2.Corr(live.agepreg, live.totalwgt_lb)
rho_s = thinkstats2.SpearmanCorr(live.agepreg, live.totalwgt_lb)
print('Pearson\'s Correlation, Mother\'s age and Birth weight: ', rho)
print('Spearman\'s Rank Correlation, Mother\'s age and Birth weight: ', rho_s)
```
```python
Pearson's Correlation, Mother's age and Birth weight:  0.0688339703541
Spearman's Rank Correlation, Mother's age and Birth weight:  0.0946100410966
```
The extremely low values also indicate a weak linear relationship between the mother's age at birth and birt hweight.
  
Finally, let's look at the 25th, 50th, and 75th percentiles of the cdfs of birth weigh across the range of ages:
```python
thinkplot.LEGEND = True
bins = np.arange(10, 45, 2.5)
indices = np.digitize(live.agepreg, bins)
groups = live.groupby(indices)
ages = [group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]
for percent in [75, 50, 25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(ages, weights, label = label)
thinkplot.Show(xlabel = 'Mother\'s age', ylabel = 'Birth weight')
```
![](https://image.ibb.co/nuUrun/percentiles_Q7.png)
There appears to be a weak linear relationship between birth weight and mother's age for ages in the range from roughly 14 to 26 years, but not elsewhere across the full range of ages.
