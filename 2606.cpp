//
// Created by 박정무 on 2021/03/06.
//

#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

int DfsFind(int start, vector<int> graph[], bool check[]){
    stack<int> s;
    int node = 0;
    s.push(start);

    int cnt = 0;

    while(!s.empty()){
        node = s.top();
        s.pop();

        if(check[node]) continue;

//        cout<<node<<" ";
        check[node] = true;
        cnt++;

        for(int i=0;i<graph[node].size();i++){
            if(!check[graph[node][i]]){
                s.push(graph[node][i]);
            }
        }
    }

    return cnt;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m; cin>>n>>m;

    vector<int> graph[n+1];
    bool check[n+1];

    fill_n(check,n+1,false);

    while(m--){
        int a,b; cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for(int i=1;i<n+1;i++){
        sort(graph[i].begin(),graph[i].end(),less<int>());
    }

    cout<<DfsFind(1,graph, check)-1;

}
