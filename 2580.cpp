//
// Created by 박정무 on 2021/06/20.
//

#include <iostream>
#include <vector>

using namespace std;

int arr[9][9];
int s;
vector<pair<int,int>> v;

bool check(int x, int y, int num){
    for(int i=0;i<9;i++){
        if(arr[y][i] == num) return false;
        if(arr[i][x] == num) return false;
    }

    int tx = x / 3;
    int ty = y / 3;

    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if(arr[ty*3+j][tx*3+i] == num) return false;
        }
    }

    return true;
}

void solve(int index){

    if(index == s){

        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                cout<<arr[i][j]<<" ";
            }
            cout<<"\n";
        }

        exit(0);

    }

    int x = v[index].first;
    int y = v[index].second;

    for(int i=1;i<10;i++){
        if(check(x,y,i)){
            arr[y][x] = i;
            solve(index + 1);
            arr[y][x] = 0;
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            cin>>arr[i][j];
            if(arr[i][j] == 0) v.push_back(make_pair(j,i));
        }
    }

    s = v.size();

    solve(0);
}
