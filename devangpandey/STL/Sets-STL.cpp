#include <cmath>
#include <cstdio>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, x, y;
    cin >> n;
    set<int> s;
    set<int>::iterator it;
    for (int i = 0; i < n; i++)
    {
        cin >> x >> y;
        if (x == 1)
        {
            s.insert(y);
        }
        else if (x == 2)
        {
            s.erase(y);
        }
        else
        {
            it = s.find(y);
            if (it == s.end())
                cout << "No\n";
            else
                cout << "Yes\n";
        }
    }
    return 0;
}
