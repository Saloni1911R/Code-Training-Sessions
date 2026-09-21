#include<iostream>
using namespace std;

int main(){
   int arr[]={2,2,3,4,4};
   int unique=0;

    for (int i=0; i<5; i++){
    unique=unique^arr[i];

    }

cout<<unique;

}