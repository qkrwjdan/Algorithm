//
// Created by 박정무 on 2021/08/28.
//
#include <iostream>

using namespace std;
int n,m;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n>>m;
    int arr[m];

    for(int i=0;i<m;i++){
        arr[i] = 1;
    }

    for(int i=0;i<m;i++){
        cout<<arr[i]<<" ";
    }
    cout<<"\n";

    while(true){
        arr[m-1]++;
        for(int i=1;i<=m;i++){
            if(arr[m-i] > n) {
                if(m-i == 0) exit(0);
                arr[m-i] = 1;
                arr[m-i-1]++;
            }
            else break;
        }

        for(int i=0;i<m;i++){
            cout<<arr[i]<<" ";
        }
        cout<<"\n";
    }

}
