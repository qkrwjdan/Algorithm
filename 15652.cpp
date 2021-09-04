//
// Created by 박정무 on 2021/08/29.
//

#include <iostream>
using namespace std;

int N,M;
int arr[8] = {1,1,1,1,1,1,1,1};

void dfs(int dim){
    if(dim == M){
        for(int i=0;i<M;i++){
            cout<<arr[i]<<" ";
        }
        cout<<"\n";
        return;
    }

    for(int i=1;i<N+1;i++){
        arr[dim] = i;
        if(arr[dim-1] <= arr[dim])
            dfs(dim+1);
    }

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>N>>M;

    dfs(0);

}
