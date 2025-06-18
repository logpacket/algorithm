#include <stdio.h>
#include <string.h>

int map[26] = {
    2, 2, 2,
    3, 3, 3,
    4, 4, 4,
    5, 5, 5,
    6, 6, 6,
    7, 7, 7, 7,
    8, 8, 8,
    9, 9, 9, 9
};

int main(){
    char str[16];
    int sum = 0;

    scanf("%s", str);

    for (int i=0; i <strlen(str); i++)
        sum +=map[str[i] - 'A'] + 1;

    printf("%d", sum);
    return 0;
}