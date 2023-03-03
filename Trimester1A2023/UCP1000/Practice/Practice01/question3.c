#include <stdio.h>

int factorial (int);

int main (void) {
    int input, result;
    printf("Please enter an integer\n");
    scanf("%d", &input);
    if (input >= 0) {
        result = factorial(input);
        printf("The factorial of %d is %d\n", input, result);
    } else {
        printf("You entered a negtive number!");
    }
    return 0;
}

int factorial (int num){
    int result = 1;
    while (num > 1) {
        result = result * num--;
    }
    return result;
}