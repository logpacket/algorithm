#include <stdio.h>

typedef struct {
    int W;
    int V;
} Object;

int main() {
    int n, k;
    scanf("%d %d", &n, &k);

    Object objects[100];

    for (int i = 0; i < n; i++)
        scanf("%d %d", &objects[i].W, &objects[i].V);

    

    return 0;
}