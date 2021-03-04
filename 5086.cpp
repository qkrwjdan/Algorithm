//
// Created by 박정무 on 2021/03/04.
//

#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while(true){
        int a,b; cin>>a>>b;
        if(a == 0 && b == 0) return 0;

        if(a > b){
            if( a % b == 0) cout<<"multiple"<<'\n';
            else cout<<"neither"<<'\n';
        }
        else{
            if( b % a == 0) cout<<"factor"<<'\n';
            else cout<<"neither"<<'\n';
        }
    }
}
