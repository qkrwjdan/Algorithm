#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }

int item[101];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	// 입력받기
	int n; cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> item[i];
	}

	// 입력받은 수 정렬
	sort(item, item + n);

	// 원소간 차이의 최대공약수 찾기
	int diff = item[1] - item[0];
	for (int i = 1; i < n-1; i++) {
		diff = gcd(item[i + 1] - item[i], diff);
	}

	// 최대공약수의 약수 출력 
	vector<int> ans;
	for (int i = 1; i*i <= diff; i++) {
		if (diff % i == 0) {
			ans.push_back(i);
			if ((diff/i != i)) {
				ans.push_back(diff / i);
			}
		}
	}

	sort(ans.begin(), ans.end());

	for (int i = 0; i < ans.size(); i++) {
		if (ans[i] != 1) cout << ans[i]<<" ";
	}

	return 0;
}
