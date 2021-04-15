#include <iostream>

using namespace std;

class Chef {
    public:
        void makeChicken () {
            cout << "THe chef makes chicken." << endl;
        }
        void makeSalad () {
            cout << "THe chef makes salad." << endl;
        }
        void makeSpecialDish () {
            cout << "THe chef makes bbq ribs." << endl;
        }
};

// you can inherit the public properties of an already defined class to increase reusability of code
class ItalianChef : public Chef {
    public:
        void makePasta () {
            cout << "The chef makes pasta" << endl;
        }
        // this is function overriding, in which an inherited function's class is re-defined
        void makeSpecialDish() {
            cout << "The chef makes chicken parm" << endl;
        }
};

// function overloading is different than function overriding
// overloading of a function can occur without inheritance whereas overriding only occurs
// after inherited class' function is re-defined

int main() 
{
    Chef chef;
    chef.makeChicken();
    chef.makeSpecialDish();

    ItalianChef italianChef;
    italianChef.makeChicken(); // the make chicken is used from inherited public segment of chef class
    italianChef.makeSpecialDish(); // the special dish for our italian chef is special

    return 0;
}

// note: changing the makeChicken() function once in Chef class, it will change in all class definitions 
// which are inheriting this class