# include <iostream>

using namespace std;

int power(int baseNum, int powNum) {

    int result = 1;

    for (int i = 0; i < powNum; i++) {
        result = result * baseNum;
    }

    return result;
}

int main()
{
    int num, pow;
    cout << "Enter the number: ";
    cin >> num;
    cout << "\nEnter the power you want: ";
    cin >> pow;

    cout<< power(num, pow);

    return 0;
}