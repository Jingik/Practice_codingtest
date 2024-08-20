#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<double> vec(N);
    int Max_num = 0;
    double result = 0;

    for (int i = 0; i < N; i++){
        cin >> vec[i];
        if (Max_num < vec[i])
            Max_num = vec[i];
    }

    for (int i = 0; i < N; i++){
        result += (vec[i] / Max_num) * 100;
    }

    cout << result / N << endl;

    return 0;
}
