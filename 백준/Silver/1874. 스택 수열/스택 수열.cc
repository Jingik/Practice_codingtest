#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    stack<int> st; 
    vector<char> operations; 
    int current = 1; 

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;

        while (current <= num) {
            st.push(current);
            operations.push_back('+'); 
            current++;
        }

        if (st.top() == num) {
            st.pop();
            operations.push_back('-'); 
        }
        else {
            cout << "NO" << endl;
            return 0;
        }
    }

    for (char op : operations) {
        cout << op << '\n';
    }

    return 0;
}
