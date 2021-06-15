//
// Created by 박정무 on 2021/06/15.
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve(vector<string> v, int x, int y, int size){
    char tmp = v[y][x];

    if(size == 1){
        cout<<tmp;
        return ;
    }

    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            if (tmp != v[y+i][x+j]){
                cout<<"(";
                size /= 2;
                solve(v,x,y,size);
                solve(v,x+size,y,size);
                solve(v,x,y+size,size);
                solve(v,x+size,y+size,size);
                cout<<")";
                return;
            }
        }
    }
    cout<<tmp;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin>>n;

    vector<string> v;

    for(int i=0;i<n;i++) {
        string s;
        cin >> s;
        v.push_back(s);
    }

    solve(v,0,0,n);
}
