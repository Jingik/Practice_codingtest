#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    while (true) {
        string text;

        getline(cin, text);
        if (text == "EOI") {
            break;
        }

        transform(text.begin(), text.end(), text.begin(), ::tolower);

		if (text.find("nemo") != string::npos) {
			cout << "Found" << endl;
		}
		else {
			cout << "Missing" << endl;
		}
    }
    return 0;
}