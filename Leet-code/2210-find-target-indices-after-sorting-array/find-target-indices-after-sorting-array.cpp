class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        int i = 0;
        vector<int> res;
        sort(nums.begin(),nums.end());
        while(i< nums.size()){
            if(nums[i] == target){
                res.push_back(i);
            }
            i++;
        }
        return res;
    }
};