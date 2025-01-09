#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

	int exam[10000];

    int num;
    cin >> num;
	int number = 0;
	for (int i = 666; i < 10000000; i++) {
		string str = to_string(i);
		if (str.find("666") != string::npos) {
			exam[number] = i;
			number++;
		}
		if (number == num) {
			break;
		}
	}

	cout << exam[num - 1] << endl;

    return 0;
}