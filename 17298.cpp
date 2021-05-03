//
// Created by 박정무 on 2021/05/03.
//

#include <iostream>
#include <stack>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    stack<int> s;

    int n;cin>>n;
    int Ai[n];
    for(int i=0;i<n;i++){
        cin>>Ai[i];
    }

    int res[n];
    fill_n(res,n,-1);

    for (int i = 0; i < n; i++) {
        while (!s.empty() && Ai[s.top()] < Ai[i]) {
            res[s.top()] = Ai[i];
            s.pop();
        }
        s.push(i);
    }

    for(int i=0;i<n;i++){
        cout<<res[i]<<" ";
    }
    cout<<"\n";
}
