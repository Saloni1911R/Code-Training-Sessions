class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        map<char,int> hm1;
        map<char,int>hm2;
        for(char ch: s){
            hm1[ch]++;
        }
        for(char ch:t){
            hm2[ch]++;
        }
        for(char ch:s){
            if(hm1[ch]!=hm2[ch]){
                return false;
            }
        }return true;
    }
    
};