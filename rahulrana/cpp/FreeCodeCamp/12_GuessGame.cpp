# include <iostream>
# include <conio.h>

using namespace std;

int main()
{
    int secretNum = 7, chances = 5;
    int guess;

    // game for the user to guess what the secret number is
    while(secretNum != guess and chances > 0) {
        cout << "Enter your guess! ";
        cin >> guess;
        chances--;
    }

    // give the user a second chance if he/she hasn't yet guessed it
    if (secretNum != guess) {
        cout << "YOU GET ANOTHER CHANCE!";
        chances = 5;
        do {
            cout << "Enter your guess! ";
            cin >> guess;
            chances--;
        } while(chances >0 and secretNum != guess);
    }

    // printout if the user won or not
    if (secretNum == guess) {
        cout << "You Win!!";
    } else {
        cout << "You lose!";
    }

    // just some pause until the user presses any key
    getch();
    return 0;
}