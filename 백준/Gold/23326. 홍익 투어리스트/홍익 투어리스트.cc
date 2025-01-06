#include<iostream>
#include<set>
using namespace std;
int n, q;
set<int> loc; // 명소
int dohyeon = 1;
void func1(int Q) {
	if (loc.find(Q) != loc.end())
	{
		loc.erase(Q);
	}
	else {
		loc.insert(Q);
	}
}
void func2(int Q) {
	dohyeon = (dohyeon + Q - 1) % n + 1;
}
void func3() {
	
	if (loc.size() == 0)
		cout << -1 << '\n';
	else
	{
		auto a = loc.lower_bound(dohyeon);
		if (a != loc.end()) {
			cout << *a - dohyeon << '\n';
		}
		else
			cout << n - dohyeon  + *loc.begin() << '\n';
	}
}
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> q;
	for (int i = 1; i <= n; i++) {
		int num;
		cin >> num;
		if (num)
			loc.insert(i);
	}

	for (int i = 0; i < q; i++) {
		int num, Q;
		cin >> num;
		if (num == 1) {
			cin >> Q;
			func1(Q);
		}
		else if (num == 2) {
			cin >> Q;
			func2(Q);
		}
		else {
			func3();
		}
	}

	return 0;
}