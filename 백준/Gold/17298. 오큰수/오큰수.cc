#include <iostream>
#include <stack>
using namespace std;
 
int arr[1000001];
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
 
    int N;
    cin >> N;
    stack<int> st;
    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;
        arr[i] = num;
        while (1) {
            if (st.empty()) {
                st.push(i);
                break;
            }
            int idx = st.top();
            if (num > arr[idx]) {
                arr[idx] = num;
                st.pop();
            }
            else {
                st.push(i);
                break;
            }
        }
    }
    while (!st.empty()) {
        int idx = st.top();
        arr[idx] = -1;
        st.pop();
    }
    for (int i = 0; i < N; i++) {
        cout << arr[i] << ' ';
    }
    return 0;
}