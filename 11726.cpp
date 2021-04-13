//
// Created by 박정무 on 2021/04/13.
//

#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin>>t;
    int dp[t+1];

    dp[1] = 1;
    dp[2] = 2;

    for(int i=3;i<t+1;i++){
        dp[i] = (dp[i-2] + dp[i-1]) % 10007;
//        dp[i] = dp[i-2] + dp[i-1];
    }

    cout<<dp[t];
    return 0;
}
