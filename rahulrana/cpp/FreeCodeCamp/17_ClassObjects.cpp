// Classes and Objects are very important in c++
# include <iostream>

using namespace std;

/*
int main()
{
    // storing information in normal variables in right data types 
    string name = "Rana";
    double pi = 3.14;
    char favouriteLetter = 'G';

    // but, at times there are a lot of REAL WORLD entities that can't be represented by these
    // primitive data types
    // Eg, Phone: Name, Model, RAM, Processor, ROM etc.
    // Here is where Class comes in, you can create a Blueprint of any datatype you want to use it
    // thus, you can create your own data type that you want in cpp, ANYTHING YOU LIKE!

    return 0;
}
*/

// class is a blueprint for a new data type
// class, followed by Name (starts with capital Letter) and also ends with ";", in contrast to functions
class Book {
    public: // these are attributes that can be accessed outside the class definition
        string title;
        string author;
        int pages;
        // you can think of more but this is just for a simple example
}; // now we can use this blueprint to be created in our main function as AN OBJECT of our Class

int main()
{
    Book book1; // we created object (variable) of our Book class
    book1.title = "Harry Potter"; // we have assigned the book1 titled as Harry Potter
    book1.author = "JK Rowling"; // now author
    book1.pages = 500; // now the number of pages

    // we can also retrieve the information of our book1 object
    cout << book1.title <<endl;
    cout << book1.author <<endl;
    cout << book1.pages <<endl;

    // another object and storing the different values    
    Book book2;
    book2.title = "Lord of the Rings"; // we have assigned the book1 titled as Harry Potter
    book2.author = "Tolkein"; // now author
    book2.pages = 700; // now the number of pages

    // retrieving the information of our book2 object
    cout << book2.title <<endl;
    cout << book2.author <<endl;
    cout << book2.pages <<endl;

    return 0;
}