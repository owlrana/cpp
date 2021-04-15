# include<iostream>
# include<conio.h>

using namespace std;

// function to add two numbers
double add(int num1, int num2) {
    return num1 + num2;
}

// function to subtract two numbers
double subtract(int num1, int num2) {
    return num1 - num2;
}

// function to multiply two numbers
double multiply(int num1, int num2) {
    return num1 * num2;
}

// function to divide two numbers
double divide(int num1, int num2) {
    return num1 / num2;
}

int main()
{
    int num1, num2;
    char op; // to see the operator user wants
    cout << "Enter the first number: ";
    cin >> num1;
    cout << "Enter the operator (+, -, *, /): ";
    cin >> op;
    cout << "Enter the second number: ";
    cin >> num2;

    double result;

    // to see which operator the user has chosen
    if(op == '+') { 
        result = add(num1, num2);
    } else if (op == '-') {
        result = subtract(num1, num2);
    } else if (op == '*') {
        result = multiply(num1, num2);
    } else if (op == '/') {
        result = divide(num1, num2);
    } else {
        cout << "INVALID OPERATOR!";
    }

    cout << result;
    getch();
    return 0;
}