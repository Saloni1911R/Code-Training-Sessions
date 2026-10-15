class Solution {
public:
    int strStr(string haystack, string needle) {
        int n1 = haystack.size();
        int n2 = needle.size();

        for(int i = 0;i<n1;i++){
            if(haystack[i]==needle[0]){
                int a = 0;
                int b = i;
                while(b<n1 && a<n1 && haystack[b]==needle[a]){
                    a++;
                    b++;
                }
                if(a==n2){
                    return i;
                }
            }
        }
        return -1;
    }
};