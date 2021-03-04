//
// Created by 박정무 on 2021/03/04.
//

#include <iostream>

using namespace std;

typedef long long ll;

ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; } // 최대공약수
ll lcm(ll a, ll b) { return a * b / gcd(a, b); } // 최소공배수

int main(){

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll a,b;cin>>a>>b;
    cout<<gcd(a,b)<<"\n";
    cout<<lcm(a,b);

}
