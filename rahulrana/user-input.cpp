// Getting input from the user in C++

#include <iostream>

using namespace std;

int main() {

    int age;
    cout << "Enter your age: ";
    cin >> age;

    cout<< "You are "<< age <<" years old!";
    return 0;

    // get a string of text instead of a char
    string name;
    cout<<"Enter your name";
    getline(cin, name);

    cout<< "You are "<< name << ", hi!";
}   