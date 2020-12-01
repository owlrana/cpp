// about arrays

#include <iostream>

using namespace std;

int main() {

    int index = 0, lucky_nums[] = {13, 27, 72, 81, 111, 123};

    cout<< "Enter which lucky number you want to access:\n";
    cin>> index;

    lucky_nums[index] = 000;
    cout<< lucky_nums[index];
    
    // we created 20 as size and add later
    int extended_array[20];
    
    return 0;
}