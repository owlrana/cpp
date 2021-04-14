#include<iostream>

using namespace std;

int main()
{
    double num1, num2; // declaring both variables of same data type in a single line
    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter second number: ";
    cin >> num2;

    cout << "After Adding both: " << num1 + num2 << endl;
    cout << "After Subtracting both: " << num1 - num2 << endl;
    cout << "After Multiplying both: " << num1 * num2 << endl;
    cout << "After Dividing both: " << int(num1 / num2) << endl; 

    return 0;

}