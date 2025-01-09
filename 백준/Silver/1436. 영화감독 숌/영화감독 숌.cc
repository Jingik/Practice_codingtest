#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num;
    cin >> num;

    int count = 0; // 찾은 숫자의 개수
    int current = 666; // 첫 번째 숫자 시작

    while (true) {
        string str = to_string(current);
        if (str.find("666") != string::npos) {
            count++; // "666" 포함된 숫자를 찾으면 증가
        }

        // 찾은 숫자가 입력 개수와 같다면 출력하고 종료
        if (count == num) {
            cout << current << endl;
            break;
        }

        current++; // 다음 숫자로 이동
    }

    return 0;
}
