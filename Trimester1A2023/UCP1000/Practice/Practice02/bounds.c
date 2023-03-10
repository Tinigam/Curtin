#include <stdio.h>
#include "powers.h"

int intBounds(int low, int high, int value);
int doubleBounds(double low, double high, double value);
int charBounds(char low, char high, char value);


int main(){
    int input;
    printf("Please enter a number between 1 and 31:\n");
    scanf("%d", &input);
    if BETWEEN(1, input, 31){
        int i;
        for (i = 1; i <= input; i++) {
            printf("%d\n", powers());
        }
    }else{
        printf("Error! please try again:\n");
        main();
    }
    /* printf("%d\n", intBounds(0, 10, 4));
    printf("%d\n", doubleBounds(0, 10, 4));
    printf("%d\n", charBounds('a', 'c', 'b'));*/
    return 0;
}

int intBounds(int low, int high, int value) {
    if BETWEEN(low, value, high) {
        return TRUE;
    }else{
        return FALSE;
    }
}

int doubleBounds(double low, double high, double value) {
    if BETWEEN(low, value, high) {
        return TRUE;
    }else{
        return FALSE;
    }
}

int charBounds(char low, char high, char value) {
    if BETWEEN(low, value, high) {
        return TRUE;
    }else{
        return FALSE;
    }
}