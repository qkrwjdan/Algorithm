//
// Created by 박정무 on 2021/03/06.
//

#include <iostream>
#include <string>
#include <stack>

using namespace std;

void solve(string a){
    stack<char> s;
    for(int i=0;i<a.length();i++){
        if(s.empty()) {
            if(a[i] == ')'){
                cout<<"NO"<<'\n';
                return;
            }
            else{
                s.push(a[i]);
            }
        }
        else{
            if(a[i] == ')'){
                if(s.top() == '('){
                    s.pop();
                }
                else{
                    s.push(a[i]);
                }
            }
            else{ //a[i] == '('
                if(s.top() == ')'){
                    s.pop();
                }
                else{
                    s.push(a[i]);
                }
            }
        }
    }

    if(s.empty()) cout<<"YES"<<'\n';
    else cout<<"NO"<<'\n';
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin>>t;
    while(t--){
        string a; cin>>a;
        solve(a);
    }
}
