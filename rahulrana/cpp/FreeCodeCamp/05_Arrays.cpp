// to store multiple elements of the same type

#include<iostream>

using namespace std;

int main()
{
    int luckyNums[] = {4, 8, 15, 16, 23, 42}; //  an array of int type elements

    int index = 0;
    cout << luckyNums[index]; // starts with 0, returns the element in a particular index
    luckyNums[0] = 0; // can also modify the indices
    cout << luckyNums[index];

    // a lot of times you wouldn't know what you want to store, so you can just initialize array with size
    char unknownArray[20]; // can store 20 elements, out of which first 2 are 0 and 19
    unknownArray[19] = 'A';
    unknownArray[20] = 'Z';
    cout << unknownArray;

    // can also give no value at all
    int unknown[10];
    unknown[9] = 1;
    for (int i = 0; i < 10; i ++){
        if (i != 9){
            unknown[i] = 0;
        }
        cout << unknown[i] << endl;
    }

    return 0;
}