#include <iostream>
#include <vector>
#include <algorithm> 
using namespace std;


bool canMake(const vector<long long>& v, long long length, int n) {
    long long count = 0;
    for (long long lan : v) {
        count += lan / length; 
    }
    return count >= n;
}

int main() {
    int k, n;
    cin >> k >> n;

    vector<long long> v(k);
    for (int i = 0; i < k; i++) {
        cin >> v[i];
    }

    long long left = 1; 
    long long right = *max_element(v.begin(), v.end()); 
    long long answer = 0;

    while (left <= right) {
        long long mid = (left + right) / 2; 

        if (canMake(v, mid, n)) {
            answer = mid;   
            left = mid + 1; 
        }
        else {
            right = mid - 1; 
        }
    }

    cout << answer << endl;
    return 0;
}


