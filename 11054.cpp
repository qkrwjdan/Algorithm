//
// Created by 박정무 on 2021/03/09.
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

    int dp[t][2];

    for(int i=0;i<t;i++){
        dp[i][0] = 0;
        for(int j=0;j<i;j++){
            if(arr[i] > arr[j]){
                dp[i][0] = max(dp[i][0],dp[j][0]);
            }
        }
        dp[i][0]++;
    }

    for(int i=t-1;i>=0;i--){
        dp[i][1] = 0;
        for(int j=t-1;j>=i;j--){
            if(arr[i] > arr[j]){
                dp[i][1] = max(dp[i][1],dp[j][1]);
            }
        }
        dp[i][1]++;
    }

//    for(int i=0;i<t;i++){
//        cout<<arr[i]<<" ";
//    }
//    cout<<"\n";
//
//    for(int i=0;i<t;i++){
//        cout<<dp[i][0]<<" ";
//    }
//    cout<<"\n";
//
//    for(int i=0;i<t;i++){
//        cout<<dp[i][1]<<" ";
//    }
//    cout<<"\n";

    int ans = 0;

    for(int i=0;i<t;i++){
        ans = max(ans,dp[i][0] + dp[i][1]);
    }

    cout<<ans-1;

}
