#include <iostream>
#include <string>
using namespace std;

int typestr(int x, int y, int z) {
    int sum = 0;
    
    string a = to_string(x) + to_string(y);
    
    return stoi(a) - z;
}

int main()
{
    int x, y, z;
    cin >> x >> y >> z;
    cout << x + y - z << endl;
	cout << typestr(x, y, z) << endl;

    return 0;

}