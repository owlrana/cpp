# include <iostream>

using namespace std;

int getMax(int num1, int num2, int num3) {

    int result;

    if (num1 >= num2 and num1 >= num3) {
        result = num1;
    } else if (num2 >= num1 and num2 >= num3) {
        result = num2;
    } else {
        result = num3;
    }

    return result;
}

int main()
{
    int num1, num2, num3;
    cout << "Enter first number: " << endl;
    cin >> num1;
    cout << "Now enter second number: " << endl;
    cin >> num2;
    cout << "Now enter the third number: " << endl;
    cin >> num3;

    cout << getMax(num1, num2, num3) << " is the bigger number!.\n";

    return 0;
}