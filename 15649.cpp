//
// Created by 박정무 on 2021/03/03.
//

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

//    cout << n << " " << m << endl;

    vector<int> v;

    for(int i=0;i<n;i++){
        v.push_back(i+1);
    }

    string beforeStr;
    string nowStr;

    do{
        for(int i=0;i<m;i++){
            nowStr += to_string(v[i]);
        }

//        cout<<"beforeStr : "<<beforeStr<<endl;
//        cout<<"nowStr : "<<nowStr<<endl;

        if(nowStr != beforeStr){
            for(int i=0;i<m;i++){
                cout<<nowStr[i]<<" ";
            }
            cout<<"\n";
            beforeStr = nowStr;
        }

        nowStr = "";
    }while(next_permutation(v.begin(), v.end()));
}
