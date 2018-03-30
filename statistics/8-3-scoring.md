[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

Import the needed modules
```python
import thinkstats2
import thinkplot
import estimation
import math
import numpy as np
```
To simulate a game, I wrote the following function:
```python
def SimulateGame(lam):
    t = 0
    goals = 0

    while True:
        x = np.random.exponential(1.0/lam, 1)
        t += x
        if t < 1:
            goals += 1
        else:
            break
    return goals
```
I also wrote a function to simulate many games, collect the estimates and the mean error/RMSE, and plot the sampling distribution with the 90% confidence interval:
```python
def EstimateGoals(lam, m):
    def VertLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

    lams = []
    for _ in range(m):
        goals = SimulateGame(lam)
        lams.append(goals)

    print('RMSE of Goals: ', estimation.RMSE(lams, lam))
    print('Mean Error of Goals: ', estimation.MeanError(lams, lam))

    cdf = thinkstats2.Cdf(lams)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    VertLine(ci[0])
    VertLine(ci[1])
    
    thinkplot.Cdf(cdf)
    thinkplot.Show()
```
Running the above with `lam = 2` at different values of *m*, results in the following RMSE and mean errors for estimating `lam`:  

|m|RMSE|MeanError|
|:---|---|---|
|100| 1.396 | -0.03 |
|1000| 1.417 | 0.01 |
|10000| 1.421 | -0.0089 |
|100000| 1.415 | 0.0014 |

While RMSE from this method of estimation remains around 1.4 regardless of *m*, the absolute value of Mean Error decreases with *m*, so there is some evidence the method is unbiased.

Keeping *m* at 1000 and increasing the value of `lam` tends to increase the RMSE:

|lam|RMSE|
|:---|---|
|2| 1.417 |
|3| 1.684 |
|4| 1.998 |
|5| 2.172 |
|8| 2.845 |

Comparing the sampling distribution and 90% confidence intervals for goals when `lam = 2` to when `lam = 5` below, we observe the wider range of possible values for the estimate and the wider confidence interval for the latter (both contain the actual value of `lam` for the given experiment):

![](https://image.ibb.co/fnaHH7/sampling2_Q10.png)

![](https://image.ibb.co/fyPcH7/sampling5_Q10.png)
