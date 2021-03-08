//
// Created by 박정무 on 2021/03/08.
//

#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N,M; cin>>M>>N;
    int arr[N+2][M+2];

    vector<int> startPoint;
    queue<pair<int,int>> q;

    for(int i=0;i<N+2;i++){
        fill_n(arr[i],M+2,0);
    }
    fill_n(arr[0],M+2,-1);
    fill_n(arr[N+1],M+2,-1);

    for(int i=0;i<N+2;i++){
        arr[i][0] = -1;
        arr[i][M+1] = -1;
    }

    for(int i=1;i<N+1;i++){
        for(int j=1;j<M+1;j++){
            cin>>arr[i][j];
            if(arr[i][j] == 1){
                q.push(make_pair(i,j));
            }
        }
    }

    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;

        q.pop();

        if (arr[x + 1][y] == 0) {
            q.push(make_pair(x + 1, y));
            arr[x + 1][y] = arr[x][y] + 1;
        }
        if (arr[x][y + 1] == 0) {
            q.push(make_pair(x, y + 1));
            arr[x][y + 1] = arr[x][y] + 1;
        }
        if (arr[x - 1][y] == 0) {
            q.push(make_pair(x - 1, y));
            arr[x - 1][y] = arr[x][y] + 1;
        }
        if (arr[x][y - 1] == 0) {
            q.push(make_pair(x, y - 1));
            arr[x][y - 1] = arr[x][y] + 1;
        }

    }
    int maxvalue = 0;
    int minvalue = 1000;

    for(int i=1;i<N+1;i++){
        for(int j=1;j<M+1;j++){
            if(arr[i][j] == -1) continue;
            maxvalue = max(arr[i][j],maxvalue);
            minvalue = min(arr[i][j],minvalue);
        }
    }

    if(minvalue == 0){
        cout<<"-1";
    }
    else{
        cout<<maxvalue-1;
    }

//    for(int i=0;i<N+2;i++){
//        for(int j=0;j<M+2;j++){
//            cout<<arr[i][j];
//        }
//        cout<<"\n";
//    }
}
