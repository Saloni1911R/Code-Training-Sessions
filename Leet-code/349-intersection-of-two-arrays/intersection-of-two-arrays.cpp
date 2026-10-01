class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        unordered_map<int, int> hm;

        for(int x : nums1){
            hm[x] = 1;
        }
        for(int x : nums2){
            if(hm[x]!=0 && hm.count(x)==1){
                hm[x] = 0;
                ans.push_back(x);
            }
        }
        return ans;
    }
};