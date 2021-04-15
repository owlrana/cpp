// Pointers are just memort addresses

# include <iostream>

using namespace std;

int main()
{
    // these are just containers (diff data types) to store diff values
    // UNDER THE HOOD:
    /*
        in the below 3 lines, the computer uses memory to store and keep track of these info
        when the variable age is created, it takes value 19 and stores into the phys memory
        same with double and string.
        So for us, 19 is stored in a variable and we dont need to worry about other stuff
        but UNDER THE HOOD, 19 is actually stored in physical memory (imagine in a container)
        So, this container where this value is stored, has a unique memory address
        Thus, when we want to access the variable, our computer goes to the memory address
        while we can just access using the variable name
    */
    int age = 19;
    double gpa = 2.7;
    string name = "Mike";

    // in case you want to go to that memory location YOURSELF, use "&" to refer to memory address:
    // cout << &age << endl; // returns a hexadecimal number where this memory address is
    // THUS, a pointer is the memory address of a variable
    
    // Eg
    cout << "Age: " << &age << endl;
    cout << "GPA: " << &gpa << endl;
    cout << "Name: " << &name << endl;
    
    // You can also create a variable to store the memory address by creating pointer variable
    // it is just a container where we can store memory adresses
    // generally we will be using a memory address of some variable as we can't just arbitratily know
    // where what is...

    int *pAge = &age; // use lowercase p before the variable name to show that this is the pointer variable
    
    // De-Referencing the pointer
    // it is basically an address to the memory location, you can do that by using *pName
    cout << *pAge << ": " << &pAge << endl; // use *pAge to get value and pAge for the memory address
    *pAge = 21; // can also edit by going to the memory address and changing the value it contains
    cout << *pAge << ": " << &pAge << endl; // new value now, but the memory location is the same
    
    // so basically *pVar means go the pVar memory and give me the value it contains
    // &pAge is the same as pAge
    // *&pAge is the same as *pAge

    // pointers data type needs to be of the same type as the variable it contains memory for
    double *pGpa = &gpa;
    string *pName = &name;
    
    // to see the size of the pointer variable
    cout << sizeof(*pAge) << endl; // size of the pointer is the same as that of the data type it contains value for
    
    int ranaAge = 21;
    cout << ranaAge << endl << &ranaAge << endl;

    return 0;
}