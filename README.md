# RL-Upper-Confidence-Bound
Finding out the best version (ad with the highest conversion rate) out of given ads

The deparment of marketing prepared different versions of an ad showing off 
their new SUV model and plan to put it on a social network. But they are not
sure which ad to put on the social network. They want to put an ad that will
get the maximum clicks, so that most users buy the SUV. SO they need to put an
ad that will lead to best conversion rate. So let's assume this car company hires
me to find the best strategy to find out the version of ad which is the best
for the user, i.e, the ad with highest conversion rate, the CTR(Click Through Rate).
 
In the dataset used, each row represents a user on the social network
each column represents a version of ad. 0 means the user didn't click the ad, 
and 1 obviously means the user did click it for more info.

## Plot for random selection
So this random selection algo randomly selected an ad in each round and generated a reward. It's quite difficult to tell
which ad was the most successful one, since random results are obtained after each iteration of this simple algorithm.
![alt text](https://i.imgur.com/pB63yOQ.png)

## Plot for results UCB algo
Based on the given dataset, using UCB the results are clear cut and it turns out that ad #5 is the one with highest conversion rate. 
![alt text](https://i.imgur.com/rRIcUqu.png)
