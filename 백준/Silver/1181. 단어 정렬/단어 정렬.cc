#include <iostream>
#include <string>
#include <algorithm> 
using namespace std;


bool compare(const string &a, const string &b) {
    if (a.length() != b.length()) {
        return a.length() < b.length(); 
    }
    return a < b;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 

    int N;
    cin >> N;

    string words[20000]; 

    for (int i = 0; i < N; i++) {
        cin >> words[i];
    }

    sort(words, words + N, compare);

    for (int i = 0; i < N; i++) {
        if (i == 0 || words[i] != words[i - 1]) { 
            cout << words[i] << '\n';
        }
    }

    return 0;
}
