class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int a = prices.size();
        int min_price = prices[0];
        int max_profit = 0;
        for(int i = 0;i<a;i++){
            min_price = min(min_price,prices[i]);
            int current_pro = prices[i] - min_price;
            max_profit = max(max_profit,current_pro);
        }
        return max_profit;
    }
};