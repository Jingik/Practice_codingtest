#include <iostream>
#include <map>
#include <string>

using namespace std;


int main()
{
    map<string, string> Dict = {
        {"SONGDO", "HIGHSCHOOL"},
        {"CODE", "MASTER"},
        {"2023", "0611"},
        {"ALGORITHM", "CONTEST"}
    };

    string input;
    cin >> input;

    cout << Dict[input] << endl;

    return 0;

}