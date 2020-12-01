// Functions in  C++
// Functions are like containers where you can store
// the code to be reused again

#include <iostream>

using namespace std;

void sayHi(string name, int age)
{
    cout<<"hello" << name << " of age "<< age <<endl;
}

// This is function prototype (signature)
void sayBye(string name, int age);

int main() {

    string name;
    cout<< "Please enter your name: ";
    getline(cin, name);
    sayHi(name, 21);

    int five_cube = 5;
    five_cube = cube(five_cube);

    return 0;
}

double cube (double n)
{
    return n * n * n;
}