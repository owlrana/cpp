// dealing with numbers in c++

#include <iostream>
#include <cmath>

using namespace std;

int main() {

    cout<< -30 + 31.5;
    cout<< 10 % 3;
    
    int five = 4;
    five += 1;

    // raising 2 to the power of 5
    cout<< pow(2,5);

    // gives back the square root of 36.36
    cout<< sqrt(36.36);

    // rounds with normal rounding rules
    cout<< round(4.5);

    // round number to higher/lower value
    cout<< ceil(4.1);
    cout<< floor(4.9);

    // returns back the bigger/smaller number, only 2 arg
    cout<< fmax(3, 10);
    cout<< fmin(3, 2);

}

// you can google C++ functions for more, 
// there are a lot of these things!