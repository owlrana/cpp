// Concstructor is a special function that will be called each time we create an objects
# include <iostream>

using namespace std;

class Book {
    public:
        string title;
        string author;
        int pages;
        
        Book () {
            title = "NO TITLE";
            author = "NO AUTHOR";
            pages = 0;
        }

        Book (string aTitle, string aAuthor, int aPages) {
           title = aTitle;
           author = aAuthor;
           pages = aPages;
       }

};

int main()
{
    Book book1("Harry Potter", "JK Rowling", 500);
    
    Book book2("Lord of the Rings", "Tolkein", 700);

    cout << book1.title << endl;
    cout << book1.author << endl;
    cout << book2.pages << endl;

    // initializing without any arguments and checking which constructor is being called
    Book book3;
    
    // checking 
    cout << book3.title << endl;
    
    
    return 0;
}