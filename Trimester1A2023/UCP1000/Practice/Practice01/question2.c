#include <stdio.h>

int main (void) {
    int a, b;
    printf("Please enter first integer:\n");
    scanf("%d", &a);
    printf("Please enter second integer:\n");
    scanf("%d", &b);
    if (a % b != 0) {
        printf("not divisible\n");
    }else {
        printf("divisible\n");
    }
    return 0;
}