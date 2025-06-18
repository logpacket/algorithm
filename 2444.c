#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    for(int i=1; i<=(n * 2 - 1); i++) {
        for(int j=0; j<(n * 2 -1); j++) {
            if(i < n) {
                if(j < n - i) printf(" ");
                else if (j >= n + i - 1) continue;
                else printf("*");
            } else {
                if(j < i - n) printf(" ");
                else if (j >= 3 * n - i - 1) continue;
                else printf("*");
            }
        }
        printf("\n");
    }
    return 0;
}