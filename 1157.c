#include <stdio.h>
#include <string.h>

int alphabet[26] = {0, };

int main() {
    char str[1000001];
    scanf("%s", str);
    int max = -1;
    int max_idx = -1;
    int len = strlen(str);
    for (int i=0; i<len; i++)
        alphabet[str[i] >= 'a' ? str[i] - 'a' : str[i] - 'A']++;

    for (int i=0; i<26; i++) {
        if (alphabet[i] > max) {
            max = alphabet[i];
            max_idx = i;    
        }
        else if (alphabet[i] == max)
            max_idx = -1;
    }
    printf("%c", max_idx == -1 ? '?' : max_idx + 'A');
    return 0;
}