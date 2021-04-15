#include<iostream>

using namespace std;

int main()
{
    int index = 0;
    // the will loop until the condition in () stays true. Condition is checked first.
    // make sure you have an escape expression in (). Infinite loops can be very dangerous.
    while(index < 5) {
        cout << index++ << ", ";
        cout << index << endl;
    }

    // do while loop FIRST RUNS THE PART OF THE CODE then checks the condition
    // you can also do this by simple while() loop but it is also fine you can use this.
    do {
        cout << index << endl;
        index ++;
    } while (index <= 5); // make sure you put ";" after the while() part!!!

    

}

