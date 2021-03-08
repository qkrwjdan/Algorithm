//
// Created by 박정무 on 2021/03/08.
//

#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin>>t;
    int arr[t];
    int dp[t];

    for(int i=0;i<t;i++){
        cin>> arr[i];
    }

    for(int i=0;i<t;i++){
        dp[i] = 0;
        for(int j=0;j<i;j++){

            if(arr[j] < arr[i]){
                dp[i] = max(dp[i],dp[j]);

            }
        }
        dp[i]++;
    }

    int ans = 0;
    for(int i=0;i<t;i++){
        ans = max(ans,dp[i]);
    }

    cout<<ans;
}
