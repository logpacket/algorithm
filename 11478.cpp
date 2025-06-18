#include <iostream>
#include <set>
#include <string>

using namespace std;

int main() {
    set<string> s;
    string input_str;
    cin >> input_str;

    for (int i = 0; i < input_str.size(); i++) {
        for (int j = i; j < input_str.size(); j++) {
            string sub_str = input_str.substr(i, j - i + 1);
            s.insert(sub_str);
        }
    }

    cout << s.size() << endl;

    return 0;
}