#include <iostream>

using namespace std;

const int MAX = 100'000'000;
int coins[101] = {
    0,
};
int dp[10001] = {
    0,
};

int find_least_coins(int n, int k) {
  if (k < 0)
    return MAX;
  if (k == 0)
    return 0;
  if (dp[k] != 0)
    return dp[k];
  int min = MAX;
  for (int i = 0; i < n; i++) {
    int result = find_least_coins(n, k - coins[i]) + 1;
    if (min > result) {
      min = result;
    }
  }
  dp[k] = min;
  return min;
}
int main() {
  int n, k;
  cin >> n >> k;

  for (int i = 0; i < n; i++) {
    cin >> coins[i];
  }
  int result = find_least_coins(n, k);
  if (result >= MAX)
    cout << -1;
  else
    cout << result;

  return 0;
}