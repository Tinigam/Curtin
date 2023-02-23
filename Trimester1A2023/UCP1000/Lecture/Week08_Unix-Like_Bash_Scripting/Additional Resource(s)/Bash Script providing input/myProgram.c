#include <stdio.h>

int main(int argc, char* argv[])
{
    if(argc == 2)
    {
        printf("The argument is: %s\n", argv[1]);
    }

    printf("waiting for the user to type something\n");
    int userInput;
    scanf("%d", &userInput);
    printf("The user input is: %d\n", userInput);

    return 0;
}