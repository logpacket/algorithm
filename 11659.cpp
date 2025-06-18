#include <iostream>

int arr[100001];
int main() {
  std::ios_base::sync_with_stdio(false);
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  int N, M;
  std::cin >> N >> M;
  for (int i = 0; i < N; i++) {
    std::cin >> arr[i];
    arr[i] += (i > 0 ? arr[i - 1] : 0);
  }
  for (int _ = 0; _ < M; _++) {
    int i, j;
    std::cin >> i >> j;
    std::cout << arr[j - 1] - (i > 1 ? arr[i - 2] : 0) << '\n';
  }
}