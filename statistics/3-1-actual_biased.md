[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

First, import the necessary modules:
```python
import nsfg
import thinkstats2
import thinkplot
import probability
```

Read in the NSFG repsondent data and construct the pmf of the variable `numkddh` of the number of children under age 18 in each respondent's household:
```python
p = nsfg.ReadFemResp()
act_pmf = thinkstats2.Pmf(p.numkdhh, label='actual')
print(act_pmf)
```
```python
Pmf({0: 0.466178202276593, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.08713855815779145, 4: 0.025644380478869556, 5: 0.01072877142483318})
```

Now, the biased pmf for the variable `numkddh':
```python
bias_pmf = probability.BiasPmf(act_pmf, label='observed')
print(bias_pmf)
```
```python
Pmf({0: 0.0, 1: 0.20899335717935616, 2: 0.38323965252938175, 3: 0.25523760858456823, 4: 0.10015329586101177, 5: 0.052376085845682166})
```
We see that in the biased pmf that no households have zero children and more households with 2-5 children, which is depicted more clearly in the plots of the two pmfs:
```python
thinkplot.Pmfs([act_pmf, bias_pmf])
thinkplot.show(xlabel='No. of Children', ylabel='pmf')
```
<!---
Temporary placeholder for this image
-->
![alt text](https://image.ibb.co/kkaT4n/pmfs_Q2.png)

Calculating the means of each pmf below, we see that the mean number of children per household is more than twice as large in the biased pmf compared to the actual pmf:
```python
print('Mean number of children, actual: ', act_pmf.Mean())
print('Mean number of children, biased: ', bias_pmf.Mean())
```
```python
Mean number of children, actual:  1.024205155043831
Mean number of children, biased:  2.403679100664282
```
