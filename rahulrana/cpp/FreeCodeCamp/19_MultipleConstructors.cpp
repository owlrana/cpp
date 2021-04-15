// Concstructor is a special function that will be called each time we create an objects
# include <iostream>

using namespace std;

class Book {
    public:
        string title;
        string author;
        int pages;
        
        // name of class and treate it like a function
        /*
        Book () {
            cout << "Creating object" << endl;
        }
        */
       // you can also have the constructor to have values in parameters, and then initialize accordingly
       // thus instead of manually specifying each name, author, page in our code
       // we can just input them during initialisation of our object
       // we can put a in front of our arguments to make it clear these are arguments/
       Book (string aTitle, string aAuthor, int aPages) {
           title = aTitle;
           author = aAuthor;
           pages = aPages;
       }

};

int main()
{
    // initialization of 1st book object
    Book book1("Harry Potter", "JK Rowling", 500);
    
    // initialization of 2nd book object
    Book book2("Lord of the Rings", "Tolkein", 700);

    cout << book1.title << endl;
    cout << book1.author << endl;
    cout << book2.pages << endl;

    // we can still edit these values
    book2.title = "Dwight Schrutez Life";
    cout << book2.title << endl;

    return 0;
}