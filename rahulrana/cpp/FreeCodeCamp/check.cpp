// file to check a couple of things

#include<iostream>

using namespace std;

int main()
{   
    string nameInput;
    cout << "Enter the name of your character = ";
    cin >> nameInput;
    string characterName = nameInput;
    int age;
    age = 176;

    cout << "There once was a man named " << characterName << endl;
    cout << "He was " << age << " years old" << endl;
    cout << "He liked the name " << characterName << endl;
    cout << "But he didn't like being " << age << endl;

    return 0;
}
