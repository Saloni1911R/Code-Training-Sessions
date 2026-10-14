class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        int n = strs.size();
        string f = strs[0];
        string l = strs[n-1];
        string ans="";

        int i = 0;
        while(i<f.size() && i<l.size()){
            if(f[i]==l[i]){
                ans+=f[i];
            }
            else{
                break;
            }
            i++;
        }
        return ans;
    }
};