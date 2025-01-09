// 01_09.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

bool compare(const string& a, const string& b) {
    if (a.length() == b.length()) {
        return a < b;
    }
    return a.length() < b.length();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num;
    cin >> num;

    string exam[20000];
    for (int i = 0; i < num; i++) {
        cin >> exam[i];
    }
    sort(exam, exam + num, compare);
    
    for (int i = 0; i < num; i++) {
        if (i == 0 || exam[i] != exam[i - 1]) {
            cout << exam[i] << '\n';
        }
    }
    return 0;
}
