#include <stdio.h>

void secondsToTime(int totalSeconds, int* hours, int* minutes, int* seconds)
{
    //3600 seconds in an hour
    *hours = totalSeconds / 3600;
    //minutes is the number of seconds left over divided by 60
    *minutes = totalSeconds % 3600 / 60;
    seconds is the number of seconds left over after the minutes calculation
    *seconds = totalSeconds % 3600 % 60;
}

int main()
{
    int totalSeconds = 3725;
    int hours, minutes, seconds;
    
    //pass our variables by reference so that the function can modify them.
    secondsToTime(&hours, &minutes, &seconds);


    printf("%d seconds is: %d:%d:%d\n", hours, minutes, seconds);

    return 0;
}