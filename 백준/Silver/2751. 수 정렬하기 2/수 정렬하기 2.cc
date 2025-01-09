#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    //string exam[1000000];
    int num;
    cin >> num;
    vector <int> exam(num);
    for (int i = 0; i < num; i++) {
        cin >> exam[i];
    }

    sort(exam.begin(), exam.end());
    
    for (int i = 0; i < num; i++) {
        if (i > 0 && exam[i] == exam[i - 1]) {
            continue;
        }
        cout << exam[i] << '\n';
    }

    return 0;
}
