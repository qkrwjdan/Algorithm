//
// Created by 박정무 on 2021/06/23.
//
#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

using namespace std;

vector<char> op_list = {'+','-','*','/'};

int compute(string & ops, vector<int> & v){
    int sum = v[0];
    for(int i=0;i<ops.length();i++){
        switch (ops[i]){
            case '+':
                sum += v[i+1];
                break;
            case '-':
                sum -= v[i+1];
                break;
            case '*':
                sum *= v[i+1];
                break;
            case '/':
                sum /= v[i+1];
                break;
        }
    }
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> v;
    string ops;

    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        v.push_back(t);
    }

    for (int i = 0; i < 4; i++) {
        int t;
        cin >> t;
        for(int j=0;j<t;j++){
            ops += op_list[i];
        }
    }
    sort(ops.begin(), ops.end(),less<>());

    int cnt = 0;
    ll max_num = -1e9;
    ll min_num = 1e9;

    do {
        cnt++;
        ll sum = compute(ops,v);
//        cout << cnt << ops << sum << endl;
        max_num = max(max_num,sum);
        min_num = min(min_num,sum);

    } while (next_permutation(ops.begin(), ops.end()));

    cout<<max_num << "\n" << min_num;
    return 0;
}
