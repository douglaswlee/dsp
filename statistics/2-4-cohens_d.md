[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

First, import the necessary modules and read in the data needed for this problem (i.e., the dataframes of live births and first and "other" babies.

```python
import first
import math

live, firsts, others = first.MakeFrames()
```

For the problem itself, we want to see whether first babies are lighter than other babies. Looking at the means of `totalwgt_lb` for both groups provides some evidence this may be the case:

```python
print(firsts.totalwgt_lb.mean())
print(others.totalwgt_lb.mean())
```
```python
7.20109443044
7.32585561497
```

Before calculating the effect size to see if there is any meaning to the difference in mean total weight, a short digression. The example given in the text concerns a field (`prglngth`) that does not have any null values, in either `firsts` or `others`:

```python
firsts.prglngth.isnull().sum()
```
```python
0
```

```python
others.prglngth.isnull().sum()
```
```python
0
```

However, for the field this problem concerns (`totalwgt_lb`), the circumstances are quite different:

```python
firsts.totalwgt_lb.isnull().sum()
```
```python
50
```

```python
others.totalwgt_lb.isnull().sum()
```
```python
60
```

I wasn't exactly sure how the `CohenEffectSize` function in `thinkstats2` accounts for missing values and I wanted to write my own function, so I did as follows below. Note I am using a [different formula](https://en.wikipedia.org/wiki/Effect_size#Cohen's_d). Obviously, my function also does not perform any thorough error handling at present:

```python
def cohens_d(g1, g2):
    n1 = g1.size - g1.isnull().sum()
    n2 = g2.size - g2.isnull().sum()
    if n1 == 0 or n2 == 0:
        return None
    else:
        v_pooled = math.sqrt(((n1-1)*g1.var() + (n2-1)*g2.var())/(n1+n2-2))
        d = (g1.mean() - g2.mean())/v_pooled
        return d
```

Below demonstrates calls to the above function for `prglngth` and `totalwgt_lb` and their output:

```python
d_totalwgt_lb = cohens_d(firsts.totalwgt_lb, others.totalwgt_lb)
d_prglngth = cohens_d(firsts.prglngth, others.prglngth)

print('Cohen\'s d for total weight: ', d_totalwgt_lb)
print('Cohen\'s d fro pregnancy length: ', d_prglngth)
```
```python
Cohen's d for total weight:  -0.0886723696847
Cohen's d fro pregnancy length:  0.0288790518999
```

We see that Cohen's *d* for `totalwgt_lb` (total weight) suggests that first babies are lighter than others by approximately -0.089 standard deviations. The magnitude of this effect is nearly three times that associated with the difference in `prglngth` (pregnancy length) and occurs in the opposite direction (as first babies appear to require a very slightly longer pregnancy length than others).
