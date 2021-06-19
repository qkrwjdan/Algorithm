//
// Created by 박정무 on 2021/06/18.
//

#include <iostream>
#include <vector>

using namespace std;

vector<pair<int,int>> v;

int n;
int answer = 0;

bool check(int x, int y){

    for(int i=0;i<v.size();i++) {
        if (x == v[i].first || y == v[i].second) return false;
        if (abs(x - v[i].first) == abs(y-v[i].second)) return false;
    }

    return true;
}

void solve(int x){
    if (x == n){
        answer++;
        return;
    }

    for(int i=0;i<n;i++){
        if(check(x,i)){
            pair<int,int> p = make_pair(x,i);
            v.push_back(p);
            solve(x+1);
            v.erase(v.end()-1);
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n;
    solve(0);
    cout<<answer;
}
