class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int b = 0;
        int s = 1;
        int result = 0;

        while (s < size(prices)) {
            if (prices[b] >= prices[s]) {
                b = s;
            };

            if (prices[b] < prices[s]) {
                result = max(result, prices[s] - prices[b]);
            };

            s = s + 1;
        };

        return result;
    };
};
