////
//// Created by 박정무 on 2021/08/22.
////

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int people[21][21];
int n;
int min_diff = 1e9;
vector<int> start_team;
vector<int> link_team;

void dfs(int x){

    if((start_team.size() == n/2) && (link_team.size() == n/2)){
        int start_ability = 0;
        int link_ability = 0;

        for(int i=0;i<start_team.size();i++) {
            for(int j=0;j<start_team.size();j++){
                start_ability += people[start_team[i]][start_team[j]];
            }
        }

        for(int i=0;i<link_team.size();i++) {
            for(int j=0;j<link_team.size();j++) {
                link_ability += people[link_team[i]][link_team[j]];
            }
        }

        int diff = abs(start_ability - link_ability);
        min_diff = min(min_diff,diff);
        return;
    }

    if(x > n) return;

    start_team.push_back(x);
    dfs(x+1);
    start_team.pop_back();

    link_team.push_back(x);
    dfs(x+1);
    link_team.pop_back();

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n;

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>people[i][j];
        }
    }

    dfs(0);
    cout<<min_diff;
    return 0;
}
