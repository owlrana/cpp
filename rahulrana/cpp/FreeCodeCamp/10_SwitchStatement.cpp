// Program to convert day number into week by using Switch Statements

# include <iostream>

using namespace std;

string getDayOfWeek(int dayNum) {
    string dayName;

    // can use if else but that will be very inefficient.
    // if we need to check the same variable for multiple values, it is perfect for Switch Statement
    // look how clean this code looks with switch()
    switch (dayNum) {
        case 0:
            dayName = "Sunday";
            break; // if you want to check for only one condition, use break;
        case 1:
            dayName = "Monday";
            break; // not having break, then all cases will be checked!!
        case 2:
            dayName = "Tuesday";
            break;
        case 3:
            dayName = "Wednesday";
            break;
        case 4:
            dayName = "Thursday";
            break;
        case 5:
            dayName = "Friday";
            break;
        case 6:
            dayName = "Saturday";
            break;
    
        default: // if the user inputs something that is not thought of in our cases...
            dayName = "INVALID DAY NUMBER!!!";
    }
    return dayName;
}

int main()
{
    int dayNum;
    cout << "Enter the day number: ";
    cin >> dayNum;

    cout << "This day is: " << getDayOfWeek(dayNum);

    return 0;
}