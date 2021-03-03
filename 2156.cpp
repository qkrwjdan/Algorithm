//
// Created by 박정무 on 2021/03/02.
//

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    int arr[t];

    for (int i = 0; i < t; i++) {
        cin >> arr[i];
    }

//    for (int i = 0; i < t; i++) {
//        cout << arr[i] << " ";
//    }
//    cout << endl;

    int dp[t][2];

    dp[0][0] = arr[0];
    dp[0][1] = 0;

    dp[1][0] = arr[1];
    dp[1][1] = dp[0][0] + arr[1];

    for(int i=2;i<t;i++){
        //dp[i][0] => i번째 요소를 처음 선택하는 경우
        dp[i][0] = max(dp[i-2][0],dp[i-2][1]) + arr[i];

        //dp[i][1] => i번째 요소를 2번째로 선택하는 경우
        dp[i][1] = dp[i-1][0] + arr[i];

        //세개 이상을 안 고르고 건너뛸 수 있나? -> 세개 이상은 건너뛸 필요가 없다. 중간을 고르면 되그등요
        dp[i][0] = max(dp[i][0],dp[i-1][0]);
        dp[i][1] = max(dp[i-1][1],dp[i][1]);

    }

    int a = max(dp[t-1][0],dp[t-1][1]);
    int b = 0;

    if(t == 1){
        b = 0;
    }else{
        b = max(dp[t-2][0],dp[t-2][1]);
    }

    cout<<max(a,b)<<endl;

    return 0;
}
