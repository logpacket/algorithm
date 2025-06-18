#include <stdio.h>
#include <string.h>

int main(){
    char s[101];
    char stack[101];
    char stack_size = 0;

    scanf("%s", s);
    int str_size = strlen(s);
    

    for (int i = 0; i < str_size; i++) {
        if (str_size % 2 == 1 && i == (str_size / 2))
            continue;
        if (stack_size > 0 && stack[stack_size - 1] == s[i])
            stack_size--;
        else
            stack[stack_size++] = s[i];
    }

    printf("%d\n", stack_size ? 0 : 1);
    return 0;
}