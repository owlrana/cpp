#include<iostream>

using namespace std;

// void means that this function is not going to return anything
// defining a function make sure you use a distinct name as var & func name cant be same
void sayHi() {
    cout << "Hello User!";
}
// can also prototype the function and define it below main()
void sayHello(string name);

//Function that RETURNS a cube of a number
int cube(int num) {
    int cube = num*num*num;
    return cube;
}

int main()
{
    sayHi();
    sayHello("Rana");
    int num = 5;
    cout << cube(num);
    return 0;
}

// can also define a function below but need a prototype before main!!!
void sayHello(string name) {
    cout << "Hello " << name;
}