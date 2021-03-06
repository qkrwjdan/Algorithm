//
// Created by 박정무 on 2021/03/05.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>


using namespace std;


void dfs(int start, vector<int> graph[],bool check[]){

    stack<int> s;
    int node = 0;
    s.push(start);

    while(!s.empty()){
        node = s.top();
        s.pop();

        if(check[node]){
            continue;
        }

        cout<<node<<" ";
        check[node] = true;

        for(int i=0;i<graph[node].size();i++){
            if(!check[graph[node][i]] ){
                s.push(graph[node][i]);
            }
        }
    }
}

void bfs(int start, vector<int> graph[], bool check[]){
    queue<int> q;

    q.push(start);
    check[start] = true;

    while(!q.empty()){
        int tmp = q.front();
        q.pop();
        cout<<tmp<<" ";
        for(int i=0;i<graph[tmp].size();i++){
            if(check[graph[tmp][i]] == false){
                q.push(graph[tmp][i]);
                check[graph[tmp][i]] = true;
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m,v;
    cin>>n>>m>>v;

    vector<int> graph[n+1];
    bool check[n+1];

    fill_n(check,n+1,false);

    for(int i=0;i<m;i++){
        int a, b;
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

//    for(int i=1;i<n+1;i++){
//        for(int j=0;j<graph[i].size();j++){
//            cout<<graph[i][j]<<" ";
//        }
//        cout<<"\n";
//    }

    for(int i=1;i<n+1;i++){
        sort(graph[i].begin(),graph[i].end(),greater<int>());
    }

    dfs(v,graph,check);
    cout<<"\n";

    fill_n(check,n+1,false);

    for(int i=1;i<n+1;i++){
        sort(graph[i].begin(),graph[i].end(),less<int>());
    }

    bfs(v,graph,check);
}
