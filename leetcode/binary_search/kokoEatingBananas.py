import math 

def calculate_hours(piles, n):
    hours = 0
    for bananas in piles:
        hours += math.ceil(bananas / n)
    return hours

def minEatingSpeed(piles, h):
    """
    In this example, (max hours/per pile) required by koko to eat each of the piles is equal to the maximum of the piles.
    For example, if piles list has maximum element 11 then it will take koko maximum of 1 hour to finish each pile if koko
    eats 11 bananas/per hour. 
    However, we have to find the solution where Koko could eat minimum number of bananas per hour to finish all the piles in 
    given amount of time i.e. 'h' hours.  
    Lets use binary search ranging from 1 to max of piles to find the minimum where koko can finish all the piles in the given 
    amount of time. 
    """
    low, high = 1, max(piles)
    while(low <= high):
        mid = (low + high) // 2
        total_hours = calculate_hours(piles, mid)
        if(total_hours <= h):
            high = mid - 1
        else:
            low = mid + 1
    return low

#piles = [3, 6, 7, 11]
#h = 8
piles = [30,11,23,4,20] 
h = 5
print(minEatingSpeed(piles, h))
