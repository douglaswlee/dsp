[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Import the required modules:

```python
import scipy.stats
```

I then wrote functions to convert inches to centimeters and to get the probability of a value drawn from a normal distribution with a particular mean and standard deviation occurs on a given interval (documentation and improved error handling to come):

```python
def in_to_cm(inches):
    return inches * 2.54

def norm_cdf_slice(a, b, mu, sigma):
    F_a = scipy.stats.norm.cdf(a, loc=mu, scale=sigma)
    F_b = scipy.stats.norm.cdf(b, loc=mu, scale=sigma)
    return F_b - F_a
```

Using the mean and standard deviation for height for men in the U.S. given (in cm) and calling the functions above, results in the following output:

```python
mean_ht_cm = 178
sd_ht_cm = 7.7
a = in_to_cm(70)
b = in_to_cm(73)
pct_blue = norm_cdf_slice(a, b, mean_ht_cm, sd_ht_cm)
print('The percentage of blue men is: ', pct_blue)
```
```python
The percentage of blue men is:  0.342746837631
```

So approximately 34.27% of the U.S. male population would be eligible to join Blue Man Group. 
