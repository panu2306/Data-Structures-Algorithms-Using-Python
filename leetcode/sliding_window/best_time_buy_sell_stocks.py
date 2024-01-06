"""
Approach-1 : Brute-Force - 
    Time-Complexity = O(n^2)
    Space-Complexity = O(1)
"""
def maxProfit_1(prices):
    max_profit = 0
    current_profit = 0

    for i in range(len(prices)):
        for j in range(len(prices)):
            if(j > i and prices[j] > prices[i]):
                current_profit = prices[j] - prices[i]
            else: 
                continue
            max_profit = max(current_profit, max_profit)
    return max_profit

"""
Approach 2: Sliding Window:
    Time-Complexity = O(n)
    Space-Complexity = O(1)
"""
def maxProfit_2(prices):
    left_index, right_index = 0, 1
    max_profit, current_profit = 0, 0
    while(right_index < len(prices)):
        if(prices[left_index] < prices[right_index]):
            current_profit = prices[right_index] - prices[left_index]
        else:
            left_index = right_index
        right_index += 1
        max_profit = max(current_profit, max_profit)
    return max_profit

prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
print("Maximum Profit using brute-force: ", maxProfit_1(prices))
print("Maximum Profit using sliding window: ", maxProfit_2(prices))
