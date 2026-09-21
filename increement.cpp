#include<iostream>
using namespace std;

int main(){
   int arr[]={2,2,3,4,4};
   int x = 5;
   int y = 6;
   if(x++ == y && ++x > y){
    cout << x << endl;
   }
   else{
    cout << x << endl;
   }
}