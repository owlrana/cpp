# include <iostream>
# include <conio.h>

using namespace std;

int main()
{
    
    // as the while loop in previous case (12_GuessGame) we had to do the loop a finite amount of time
    // we also have a special type of loop in case we already know how many times we want the iteration
    // this is called the for loop

    int length = 10;

    // the brackets () in for loop take 3 different things
    // 1. Initialization, 2. Terminating condition, 3. Updation after the loop body is executed
    for (int i = 0; i < length; i ++) {
        cout << i << ", ";
    }
    // deletes 2 previous output characters, then adds space and then adds 2 lines.
    cout << "\b\b \n\n";

    // i = 10; //  this will result in an error as the scope of i was only until the end of the loop
    
    // range of int data type lies between -2147483648 to 2147483647 
    int array[] = {-2147483648,123,12,1,2147483647};
    
    // calculating the length of our array by dividing size of whole array by the size of single element
    length = sizeof(array)/sizeof(array[0]);
    
    // just to show what is going on, these are the values of SIZE IN BYTES:
    cout << "Size of whole array is: " << sizeof(array) << endl;
    cout << "Size of a single element is: " << sizeof(array[0]) << endl;
    cout << endl;

    for (int i= 0; i < length; i ++) {
        cout << array[i] << ", ";
    }
    cout << "\b\b \n\n"; // just for a cleaner output
    
    return 0;
}