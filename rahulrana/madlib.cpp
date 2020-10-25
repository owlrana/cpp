// madlibs game

#include <iostream>
#include <cmath>

using namespace std;

int main() {

    string colour, plural_noun, celebrity;

    cout<< " Enter a colour: ";
    getline(cin, colour);
    cout<< " Enter a Plural Noun: ";
    getline(cin, plural_noun);
    cout<< " Enter a celebrity: ";
    getline(cin, celebrity);
    
    cout<< "Roses are " << colour << endl;
    cout<< plural_noun << " are blue" << endl;
    cout<< "i love " << celebrity << endl;

    return 0;
}