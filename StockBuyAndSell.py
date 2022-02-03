class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0: return 0
        max_profit=0
        min_buy_day=prices[0]
        for idx in range(len(prices)):
            buy=prices[idx]
            if buy<min_buy_day:
                min_buy_day=buy
            if prices[idx]-min_buy_day > max_profit:
                max_profit=prices[idx]-min_buy_day
        return max_profit
    
                        