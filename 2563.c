#include <stdio.h>

int paper[100][100] = {0, };

int main() {
    int n, cnt = 0;
    scanf("%d", &n);

    for (int i=0;i<n;i++){
        int l = 0;
        int b = 0;
        scanf("%d %d", &l, &b);
        for (int j=l;j<l+10;j++){
            for (int k=b;k<b+10;k++){
                paper[j][k] = 1;
            }
        }
    }
    for (int i=0;i<100;i++){
        for (int j=0;j<100;j++){
            if (paper[i][j] == 1) cnt++;
        }
    }
    printf("%d", cnt);

    return 0;
}