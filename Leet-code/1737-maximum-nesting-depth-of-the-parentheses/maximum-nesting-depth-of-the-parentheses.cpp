class Solution {
public:
    int maxDepth(string s) {
        int curr = 0;
        int maxpar = 0;
        for(char str:s){
            if(str == '('){
                curr += 1;
                if(curr > maxpar){
                    maxpar = curr;
                }
            }
            else if(str == ')'){
                curr -= 1;
            }
        }
        return maxpar;
    }
};