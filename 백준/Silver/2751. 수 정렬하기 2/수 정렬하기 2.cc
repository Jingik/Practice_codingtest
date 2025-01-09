#include <iostream>
#include <vector>
using namespace std;

const int OFFSET = 1000000; 

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 

    int N;
    cin >> N;

    vector<bool> presence(2000001, false);

    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;
        presence[num + OFFSET] = true; 
    }


    for (int i = 0; i <= 2000000; i++) {
        if (presence[i]) {
            cout << i - OFFSET << '\n'; 
        }
    }

    return 0;
}
