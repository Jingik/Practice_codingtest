#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

bool compare(const string& a, const string& b) {
    if (a.length() == b.length()) {
        return a < b;
    }
    return a.length() < b.length();
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int num;
    cin >> num;

    vector<string> words(num);
    for (int i = 0; i < num; i++) {
        cin >> words[i];
    }

	set<string> unique_words(words.begin(), words.end());
	words.assign(unique_words.begin(), unique_words.end());

    sort(words.begin(), words.end(), compare);

    for (const string& word : words) {
        cout << word << endl;
    }

    return 0;
}
