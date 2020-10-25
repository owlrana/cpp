// if statements

#include <iostream>

using namespace std;

int getMax( int num1, int num2, int num3) {
    int result;

    if(num1 >= num2 && num1 >= num3) {
        cout<<"Num1 is greatest";
    } else if (num2 >= num1 && num2 >= num3) {
        cout<<"Num2 is greatest";
    } else {
        cout<<"Num3 is greatest";
    }

    return result;
}

int main() {

    // if statements to run on logic
    bool isMale = true;
    bool isTall = true;

    if (isMale && isTall){
        cout<<"You are a tall male";
    } else if(isMale && !isTall){
        cout<<"You are not a tall male";
    } else if(!isMale && isTall){
        cout<<"You are tall but not male";
    } else {
        cout<< "You are neither male nor tall";
    }
    
    // comparisons using if (max of 2 numbers)
    

    return 0;
}