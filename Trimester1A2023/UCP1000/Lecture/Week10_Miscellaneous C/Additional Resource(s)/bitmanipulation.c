#include <stdio.h>

int main()
{
    int originalNumber;
    int n;
    int bigNumber;

    //get a number
    printf("enter a number:");
    scanf("%d", &originalNumber);

    //get the number of times it should be doubled
    printf("How many times should it be doubled?\n");
    scanf("%d", &n);

    //bit shift it left to add n number of 0s to the binary
    //this has the effect of doubling the original number n times
    //because each extra bit is one more power of 2
    bigNumber = originalNumber << n;

    printf("%d doubled %d times is %d\n", originalNumber, n, bigNumber);

    return 0;
}