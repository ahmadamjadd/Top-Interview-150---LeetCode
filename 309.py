class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def calculate_max_profit(day, state):
            if day >= len(prices):
                return 0
                
            if (day, state) in memo:
                return memo[(day, state)]
                
            if state == "FREE":
                profit_if_buy = -prices[day] + calculate_max_profit(day + 1, "HOLDING")
                profit_if_rest = 0 + calculate_max_profit(day + 1, "FREE")
                best_profit = max(profit_if_buy, profit_if_rest)

            elif state == "HOLDING":
                profit_if_sell = prices[day] + calculate_max_profit(day + 1, "COOLDOWN")
                profit_if_rest = 0 + calculate_max_profit(day + 1, "HOLDING")
                best_profit = max(profit_if_sell, profit_if_rest)

            elif state == "COOLDOWN":
                best_profit = 0 + calculate_max_profit(day + 1, "FREE")

            memo[(day, state)] = best_profit
            
            return best_profit

        return calculate_max_profit(0, "FREE")
