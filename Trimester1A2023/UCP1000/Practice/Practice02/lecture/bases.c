#include <stdio.h>

int main(){
    int x;
    printf("Please enter a number:\n");
    scanf("%d", &x);
    printf("Dec: %d, Oct:%o, Hex:%x\n", x, x, x);
    return 0;
}