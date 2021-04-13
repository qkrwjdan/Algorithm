# Algorithm
코딩테스트 대비 알고리즘 문제풀이 준비

----------------------------------
# 메모장

## DFS
```c++
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
```

## BFS
```c++
void bfs(int start, vector<int> graph[],bool check[]){
    queue<int> q;

    q.push(start);
    check[start] = true;

    while(!q.empty()){
        int node = q.front();
        q.pop();
        cout<<node<<" ";
        for(int i=0;i<graph[node].size();i++){
            if(check[graph[node][i]] == false){
                q.push(graph[node][i]);
                check[graph[node][i]] = true;
            }
        }
    }
}
```

## 이거 왜 이런거죠?
```c++
for(int i=0;i<t;i++) {
        for (int j = 0; j < t; j++) {
            cout<<v[i][j]<<" \n" [j == t - 1];
        }
    }
```
