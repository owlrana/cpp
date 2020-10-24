
// working with strings and other string functions

#include <iostream>

using namespace std;

int main() {
    
    string phrase = "whats good?\n";

    cout<<"Rahul Rana\n";
    cout<<"whats good\n"<<endl;
    cout<<"whaaa?"<<endl;

    cout<<phrase.length();
    cout<<phrase[1];
    cout<<phrase[3];
    phrase[3] = 'Z';
    cout<<phrase[3];

    // you can also pass parameter into find 
    // to find a set of char in given string
    // ("", 0) means that STARTING FROM 0 index value
    cout<<phrase.find("good", 0);

    // this will grab 5 chars starting from 8th index
    cout<<phrase.substr(8, 5);
    string phrase_sub = phrase.substr(8, 3);
    cout<<phrase_sub;
}