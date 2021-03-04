//
// Created by 박정무 on 2021/03/04.
//

#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin>>t;

    int arr[t];

    for(int i=0;i<t;i++){
        cin>>arr[i];
    }

    sort(arr,arr+t);

    if(t > 1){
        cout<<arr[0] * arr[t-1];
    }else{
        cout<<arr[0] * arr[0];
    }
}
