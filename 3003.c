#include <stdio.h>
int main(){int c[6]={1,1,2,2,2,8};for(int i=0;i<6;i++){printf("%d ",c[i]-(getc(stdin)-48));getc(stdin);}} 