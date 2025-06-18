#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
  int n;
  cin >> n;

  map<char, int> word_map;

  for (int i = 0; i < n; i++) {
    string s1;
    cin >> s1;
    if (word_map.find(s1[i]) != word_map.end()) {
      word_map[s1[i]] = 0;
    } else
      word_map[s1[i]]++;
  }
  return 0;
}