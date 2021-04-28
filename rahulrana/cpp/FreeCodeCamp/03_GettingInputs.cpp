#include<iostream>

using namespace std;

int main()
{
    string age;
    cout << "Enter your age: ";
    // cin >> age; // do not use cin, as this removes spaces, use ONLY for chars
    getline(cin, age); //  use this for a string of text always

    cout << "You are " << age << " years old.";

    return 0;
}