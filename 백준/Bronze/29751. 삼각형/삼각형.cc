#include <iostream>
#include <iomanip>

using namespace std;

float squart(float x, float y) {
    return x * y / 2;
}

int main()
{
    float x, y;
    cin >> x >> y;
	cout << fixed << setprecision(1) << squart(x, y);
    return 0;
    //cout << "Hello World!\n";
}
