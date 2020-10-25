// Switch case to show day of week by number

#include <iostream>

using namespace std;

string weekName (int num) {

    string dayname;

    switch(num) {
        case 1:
            dayname = "Monday";
            break;
        case 2:
            dayname = "Tuesday";
            break;
        case 3:
            dayname = "Wednesday";
            break;
        case 4:
            dayname = "Thursday";
            break;
        case 5:
            dayname = "Friday";
            break;
        case  6:
            dayname = "Saturday";
            break;
        case 7:
            dayname = "Sunday";
            break;
        
        default:
            printf("INVALID INPUT");
    }
}

int main() {

    int num;

    cout<< "Enter the day number: ";
    cin>> num;

    cout<< weekName(num);

    return 0;
}