#include "calc.h"
#include <stdio.h>

float squarePlusCube(float n);

int main (){
    float input, result;
    scanf("%f", &input);
    result = squarePlusCube(input);
    printf("%f", result);
    return 0;
}

float squarePlusCube(float n) {
    return square(n) + cube(n);
}