class Solution {
public:
    string removeOuterParentheses(string s) {
        string res = "";
        int count = 0;
        int start = 0;
        int i = 0;
        for(char ch:s){
            if(ch == '('){
                count++;
               
            }
            else {
                count--;
               
            }
            if(count == 0){
                res+=s.substr(start+1,i-start-1);
                start = i + 1;
            }
            i++;
        }
        return res;
        
    }
};