#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string text;
    while (true) {
        getline(cin, text);

        if (text == "EOI") {
            break;
        }

        string lowercaseText = text;
        transform(lowercaseText.begin(), lowercaseText.end(), lowercaseText.begin(), ::tolower);

        if (lowercaseText.find("nemo") != string::npos) {
            cout << "Found";
        }
        else {
            cout << "Missing";
        }
        cout << endl;
    }

    return 0;
}