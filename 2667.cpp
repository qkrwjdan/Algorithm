//
// Created by 박정무 on 2021/03/07.
//

#include <iostream>
#include <vector>
#include <stack>
#include <utility>
#include <algorithm>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;cin>>t;
    int arr[t+2][t+2];
    int checked[t+2][t+2];
    int cnt = 1;

    stack<pair<int,int>> s;
    vector<int> v;

    for(int i=0;i<t+2;i++){
        fill_n(arr[i],t+2,0);
        fill_n(checked[i],t+2,0);
    }

    for(int i=1;i<t+1;i++){
        string a; cin>>a;
        for(int j=0;j<a.size();j++){
            arr[i][j+1] = a[j] - '0';
        }
    }

    for(int i=1;i<t+1;i++){
        for(int j=1;j<t+1;j++){
            if(arr[i][j] == 0) continue;
            else{
                //arr[i][j]가 숫자일 때
                if(checked[i][j] == 0){
                    //방문한 적 없는 곳이라면
                    s.push(make_pair(i,j));
                    int chk = 0;

                    while(!s.empty()){
                        pair<int,int> p = s.top();
                        s.pop();

                        int x = p.first;
                        int y = p.second;

                        if(checked[x][y] != 0) continue;

                        checked[x][y] = cnt;
                        chk++;

                        if(arr[x+1][y] != 0) s.push(make_pair(x+1,y));
                        if(arr[x][y+1] != 0) s.push(make_pair(x,y+1));
                        if(arr[x-1][y] != 0) s.push(make_pair(x-1,y));
                        if(arr[x][y-1] != 0) s.push(make_pair(x,y-1));
                    }
                    v.push_back(chk);
                    chk = 0;
                    cnt++;
                }else{
                    continue;
                }
            }
        }
    }

//    for(int i=0;i<t+2;i++){
//        for(int j=0;j<t+2;j++){
//            cout<<arr[i][j];
//        }
//        cout<<'\n';
//    }
//
//    cout<<"\n";
//
//    for(int i=0;i<t+2;i++){
//        for(int j=0;j<t+2;j++){
//            cout<<checked[i][j];
//        }
//        cout<<'\n';
//    }

    sort(v.begin(),v.end(),less<int>());

    cout<<v.size()<<"\n";

    for(int i=0;i<v.size();i++){
        cout<<v[i]<<"\n";
    }


}
