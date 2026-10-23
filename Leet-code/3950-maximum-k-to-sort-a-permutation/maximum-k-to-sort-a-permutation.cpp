#include <vector>
#include <algorithm>

class Solution {
public:
    int sortPermutation(std::vector<int>& nums) {
        int ans = -1; // -1 represents all bits set to 1 in two's complement representation
        
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != i) {
                ans &= nums[i];
            }
        }
        
        // If the array is already sorted, ans remains -1, so we return 0.
        // Otherwise, return the computed bitwise AND configuration.
        return (ans == -1) ? 0 : ans;
    }
};
