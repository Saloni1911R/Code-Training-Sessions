class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        map<int,int> hm;
        map<int,int> hm2;
        vector<int> ans;
        for(int i = 0; i < nums1.size(); i++){
            hm[nums1[i]]++; 
        }
        for(int j = 0; j < nums2.size();j++){
            hm2[nums2[j]]++;
        }
        for(auto [key, value] : hm){
            if(hm2.find(key) != hm2.end()){
                ans.push_back(key);
            }
        }
        return ans;
    }
};