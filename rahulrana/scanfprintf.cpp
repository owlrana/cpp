// To read though scanf and printf (If u need to read millions of numbers, this is the fastest option)
// cout cin is slow compared to scanf and printf

#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int intgr;
    long lngintgr;
    char chr;
    float flt;
    double lngflt;

    scanf("%d %ld %c %f %lf", &intgr, &lngintgr, &chr, &flt, &lngflt);
    printf("%d \n", intgr);
    printf("%ld \n", lngintgr);
    printf("%c \n", chr);
    printf("%.2f \n", flt);
    printf("%lf \n", lngflt);
    
    return 0;
}