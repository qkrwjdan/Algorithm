//
// Created by 박정무 on 2021/03/09.
//

#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

bool compare(pair<int,int> a, pair<int,int> b){
    if(a.first == b.first){
        return a.second < b.second;
    }else{
        return a.first < b.first;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<pair<int,int>> v;

    int t; cin>>t;
    for(int i=0;i<t;i++){
        int a,b; cin>>a>>b;
        v.push_back(make_pair(a,b));
    }

    sort(v.begin(),v.end(),compare);
    int dp[t];
    fill_n(dp,t,0);

    for(int i=0;i<v.size();i++){
//        cout<<v[i].first<<" "<<v[i].second<<"\n";
        for(int j=0;j<i;j++){
            if(v[i].second >= v[j].second){
                dp[i] = max(dp[i],dp[j]);
            }
        }
        dp[i]++;
    }
    int maxNum = 0;
    for(int i=0;i<t;i++){
        maxNum = max(dp[i],maxNum);
    }

    cout<<t-maxNum;



}
