class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                gains = (prices[i] - buy)
                if gains > profit:
                    profit = gains
                    
        return profit
            
        