#include <stdio.h>
#include "hello.h"
#include "numbers.h"

int main()
{
    hello();

    int numberOne, numberTwo, answer;
    printf("Please type two numbers\n");

    scanf("%d %d", &numberOne, &numberTwo);

    answer = addNumbers(numberOne, numberTwo);

    printf("the answer is: %d\n", answer);

    return 0;
}
