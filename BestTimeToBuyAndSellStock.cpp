class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int min_price = INT_MAX;
        int max_profit = 0;

        for (int price : prices)
        {
            if (price < min_price)
            {
                min_price = price; // Update minimum price
            }
            else if (price - min_price > max_profit)
            {
                max_profit = price - min_price; // Update max profit
            }
        }
        return max_profit;
    }
};