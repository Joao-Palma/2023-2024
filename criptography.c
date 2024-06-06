#include <string.h>

#include <stdlib.h>

#include "stdio.h"

int calc_remainder(int val, int mod) {
    while (val >= mod){
        val -= mod;
    }
    return val;
}

long long int calc_potency(int val, int exp) {
    long long int res = 1;

    if (exp != 0) {
        for (exp; exp != 0; exp--) res *= val;
    }

    return res;

} 

long long int calc_publickey(long int p, long int q) {
    long long int n = p*q;
    return n; 
}

long long int calc_otherkey(long int p, long int q) {
    long long int n = (p-1)*(q-1);
    return n; 
}

int calc_congroence(int value, long long int mod) {}

char* dec_to_bin(long long int) {    // 35 bits number
    char* number[35];
    int i = 35;
    for (i; i >= 0; i--) {
        if (int < coisa) {
            number[i] = 1;
            int -= coisa;
        }
        else number[i] = 0;
    }
    return number;
}

int main(){
    int exp = 34;
    int val = 3;
    long long int res = calc_potency(val,exp);
    printf("\n%lld\n",res);
    return 0;
}
