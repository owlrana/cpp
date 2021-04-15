# include <iostream>

using namespace std;

int main()
{
    bool isMale = true;

    // if the expression in () is true, {} gets called otheerwise nope
    if(isMale) {
        cout << "You are a male!";
    }

    // "!isMale" is also the same as "not isMale"
    if(!isMale) {
        cout << "You are a male!";
    } else {
        cout<< "You are not male";
    }
    
    bool isTall = false;

    // "and" is the same as "&&" operator
    if (isMale and !isTall) {
        cout << "You are a short male!";
    }

    // "or" is the same as "||" operator
    if (isMale or isTall) {
        cout << "You are either tall or male...";
    }

    if(isMale and isTall) {
        cout << " WOW YOU ARE MALE AND TALL!";
    } else if (isMale and not isTall) {
        cout << "MM YOU ARE MALE BUT NOT TALL...";
    } else if (!isMale and isTall) {
        cout << "YOU ARE TALL BUT NOT A MALE...";
    } else {
        cout << "YOU ARE NEITHER MALE NOR TALL MAN...";
    }

    return 0;
}