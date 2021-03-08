//
// Created by 박정무 on 2021/03/07.
//

#include <iostream>
#include <queue>
#include <utility>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N,M; cin>>N>>M;
    int arr[N+2][M+2];
    bool check[N+2][M+2];
    int cnt[N+2][M+2];

    for(int i=0;i<N+2;i++){
        fill_n(arr[i],M+2,0);
        fill_n(check[i],M+2,false);
        fill_n(cnt[i],M+2,0);
    }

    for(int i=1;i<N+1;i++){
        string s; cin>>s;
        for(int j=0;j<s.length();j++){
            arr[i][j+1] = s[j] - '0';
        }
    }


    queue<pair<int,int>> q;
    q.push(make_pair(1,1));
    cnt[1][1] = 1;

    while(!q.empty()){
        pair<int,int> p = q.front();
        q.pop();
        int x = p.first;
        int y = p.second;

        if(x == N && y == M) break;

        if(check[x][y]) continue;
        check[x][y] = true;

        if(arr[x+1][y] == 1){
            if(!check[x+1][y]){
                q.push(make_pair(x+1,y));
                cnt[x+1][y] = cnt[x][y] + 1;
            }
        }
        if(arr[x][y+1] == 1) {
            if(!check[x][y+1]){
                q.push(make_pair(x,y+1));
                cnt[x][y+1] = cnt[x][y] + 1;

            }
        }
        if(arr[x-1][y] == 1) {
            if(!check[x-1][y]){
                q.push(make_pair(x-1,y));
                cnt[x-1][y] = cnt[x][y] + 1;
            }
        }
        if(arr[x][y-1] == 1) {
            if(!check[x][y-1]){
                q.push(make_pair(x,y-1));
                cnt[x][y-1] = cnt[x][y] + 1;
            }
        }
    }

    cout<<cnt[N][M];


//    for(int i=0;i<N+2;i++){
//        for(int j=0;j<M+2;j++){
//            cout<<arr[i][j];
//        }
//        cout<<'\n';
//    }

}
