#include <stdio.h>

int powers() {
    static int n = 2;
    int result = n;
    n *= 2;
    return result;
}