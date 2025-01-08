#include <iostream>
using namespace std;

int main() {
    int N, first; 
    cin >> N >> first; 

    if (N > 5) {
        cout << "Love is open door" << endl; 
        return 0;
    }

    for (int i = 1; i < N; i++) {
        first = 1 - first;
        cout << first << endl;
    }

    return 0;
}