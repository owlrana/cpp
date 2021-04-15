// Different data types in C++

#include <iostream>
#include <cmath> // if you need to use some math functions like pow() etc.

using namespace std;

int main()
{
    char grade = 'A'; // to store a single character
    string phrase = "Mr. Ranaaklajslkdjaslkjdlkasjdlkjasldkjaslk";
    string hola = "puttar"; // to store a string of characters
    int age = 50; // for whole numbers
    float decimal = 5.5; // can store decimal values
    double gpa = 210.3; // you can store higher decimal numbers in double
    bool isMale = true;

    cout << hola.find("putt", 0); //finds if the given string is in the string, starting from 0 index 
    cout << endl;
    string phr = phrase.substr(4, 2); // returns a substring from 4th index upto 2 characters 
    cout << phr + hola; // joins and returns the strings (concatenate)

    int wnum = 5;
    double dnum = 6.6;

    cout<< wnum ++; // increments after using
    cout<< wnum;
    cout << dnum ++; // even works on doubles
    cout << dnum;

    cout << pow(2, 5); // 2 raised to the power of 5
    cout << sqrt(81.5); // gives back the square root 
    cout << round(7.6); // rounds using basic rools
    cout << ceil(7.6); // returns the next int
    cout << floor(7.6); // returns the base int (lower integer)
    cout << fmax(5,7); // returns the bigger number
    cout << fmin(5,7); // returns the smaller number

    return 0;
}