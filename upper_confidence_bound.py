# Upper Confidence Bound

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implimenting UCB
N = 10000

# No. of ads
d = 10

ads_selected = []

# vector of number of selections of each ad initially containing zeroes
# since none of the ads were selected initially  
# number of times an ad was selected upto round n 
num_of_selections = [0] * d
# the sum of rewards of an ad upto round n
sum_of_rewards = [0] * d
total_reward = 0

# calculating the average reward and confindence interval
# of ad i upto round n
# also finding out number of selections of a particular ad and their rewards 
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if(num_of_selections[i] > 0):
            average_reward = sum_of_rewards[i] / num_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n+1)/num_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound 
            ad = i
    ads_selected.append(ad)
    num_of_selections[ad] += 1
    reward = dataset.values[n, ad]
    sum_of_rewards[ad] += reward
    total_reward += reward
    
# Visualization of results
plt.hist(ads_selected)
plt.title("Histogram of ad selections")
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
