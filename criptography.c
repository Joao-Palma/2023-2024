#include <string.h>

#include <stdlib.h>

#include "stdio.h"

int calc_remainder(int val, int mod) {
    while (val >= mod){
        val -= mod;
    }
    return val;
}

int main(){
    int val = 100, mod = 7;
    int res = calc_remainder(val, mod);
    printf("\n%d\n", res);
    return 0;
}

