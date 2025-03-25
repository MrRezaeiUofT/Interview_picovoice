'''
Question:

The probability of rain on a given calendar day in Vancouver is p[i],
where i is the day's index. For example, p[0] is the probability of 
rain on January 1 st , and p[10] is the probability of precipitation 
on January 11 th . Assume the year has 365 days (i.e., p has 365 elements).
What is the chance it rains more than n (e.g., 100) days in Vancouver? Write
a function that accepts p (probabilities of rain on a given calendar day)
and n as input arguments and returns the possibility of raining at least
n days. def prob_rain_more_than_n(p: Sequence[float], n: int) -> float: pass

Answer:
We can use dynamic programming to build a solution,
using a 2D array to track the probability of having exactly j rainy days after i days.
For each day,we can consider both scenarios: rain or no rain, updating probabilities accordingly.
Ultimately we return the sum of all probabilities exceeding the threshold n days. 
'''

from typing import Sequence

def prob_rain_more_than_n(p: Sequence[float], n: int) -> float:

    n_d = len(p)
    
    # Initialize dp array
    dp = [[0 for _ in range(n_d + 1)] for _ in range(n_d + 1)]
    
    # Edge case: probability of 0 rainy days after 0 days is 1
    dp[0][0] = 1
    

    for d in range(1, n_d + 1):
        rp = p[d - 1]  # Probability of rain on current day
        
        # Probability of having j rainy days
        for j in range(0, d + 1):
            if j == 0:
                # Probability of having 0 rainy days
                dp[d][j] = dp[d - 1][j] * (1 - rp)
            else:
                dp[d][j] = dp[d - 1][j] * (1 - rp) + dp[d - 1][j - 1] * rp
    

    prob_n = sum(dp[n_d][j] for j in range(n + 1, n_d + 1))
    
    return prob_n
