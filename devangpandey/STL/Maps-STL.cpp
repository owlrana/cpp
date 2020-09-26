#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int main()
{
    map<string, int> s;
    int q, x, marks;
    map<string, int>::iterator it;
    string name;
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        cin >> x;

        if (x == 1)
        {
            cin >> name >> marks;
            it = s.find(name);
            if (it == s.end())
                s.insert(make_pair(name, marks));
            else
                it->second += marks;
        }
        else if (x == 2)
        {
            cin >> name;
            s.erase(name);
        }
        else
        {
            cin >> name;
            it = s.find(name);
            if (it == s.end())
                cout << "0" << endl;
            else
                cout << it->second << endl;
        }
    }
    return 0;
}
