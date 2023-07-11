class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = int(1e18)
        profit = 0
        for i in range(len(prices)):
            if (prices[i] < min):
                min = prices[i]
            if (prices[i] - min > profit):
                profit = prices[i] - min

        return profit        


"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""