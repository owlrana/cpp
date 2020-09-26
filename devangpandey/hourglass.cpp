#include <bits/stdc++.h>
using namespace std;
int main()
{
    int x;
    cin >> x;
    //TOP
    for (int i = 0; i < x; i++)
        cout << "* ";
    cout << "\n"
         << " ";
    //Middle_U
    int spaces, n;
    n = x - 1;
    while (n > 0)
    {
        spaces++;
        for (int i = 0; i < n; i++)
        {
            cout << "* ";
        }

        cout << "\n";
        if (n > 1)
        {
            for (int j = 0; j < spaces; j++)
                cout << " ";
        }
        n--;
    }
    //MIDDLE_L
    n = 2;
    spaces = spaces - 2;

    while (n < x)
    {
        for (int i = 0; i < spaces; i++)
            cout << " ";
        for (int i = 0; i < n; i++)
            cout << "* ";
        spaces--;
        if (n < x - 1)
            cout << endl;
        n++;
    }
    //BOTTOM
    cout << endl;
    for (int i = 0; i < x; i++)
        cout << "* ";
}