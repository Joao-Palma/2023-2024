#include <string.h>

#include <stdlib.h>

#include "stdio.h"

#define MAX_BIN 35

int calc_remainder(int val, int mod) {
    while (val >= mod) val -= mod;
    return val;
}

long long int calc_potency(int val, int exp) {
    long long int res = 1;

    if (exp != 0) 
        for (exp; exp != 0; exp--) res *= val;

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

int calc_congroence(int value, long long int mod) {

}

char* dec_to_bin(long long int) {    // 35 bits number
    char* number[MAX_BIN];
    int i = MAX_BIN;
    long long int pot;

    for (i; i > 0; i--) {
        pot = calc_potency( 2, i);
        if (int < pot) {
            number[i] = 1;
            int -= pot;
        }
        else number[i] = 0;
    }
    return number;
}

int main(){
    
    long long int val = 19319;
    int i = MAX_BIN;
    char* bin = dec_to_bin(val);
    
    for (i, i > 0, i--) print("%c",val[i]);

    return 0;
}
