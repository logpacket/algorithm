#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i =0; i<T;i++) {
        int K;
        cin >> K;
        vector<int> files(K+1);
        vector<int> sum(K+1);
        vector<vector<int>> dp(K+1, vector<int>(K+1, 0));

        for (int j = 1; j <= K; j++) {
            cin >> files[j];
            sum[j] = sum[j-1] + files[j];
        }

        for (int d = 1; d < K; d++) {
            for (int tx = 1; tx + d <= K; tx++) {
                int ty = tx + d;
                dp[tx][ty] = 2147483647;
                for (int mid = tx; mid < ty; mid++) {
                    dp[tx][ty] = min(dp[tx][ty], dp[tx][mid] + dp[mid+1][ty] + sum[ty] - sum[tx-1]);
                }
            }
        }
        cout << dp[1][K] << endl;
    }
    return 0;
}