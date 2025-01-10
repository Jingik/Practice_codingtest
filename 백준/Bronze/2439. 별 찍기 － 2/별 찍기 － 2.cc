#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int Count = 0;

	while (true) {
		Count++;

		for (int i = 0; i < n - Count; i++) {
			cout << " ";
		}
		for (int i = 0; i < Count; i++) {
			cout << "*";
		}
		cout << endl;
		if (Count == n) {
			break;
		}
	}

	return 0;
}
