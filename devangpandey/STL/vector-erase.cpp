#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> v(n);

    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    int x,y;
    for (int i = 0; i < 2; i++)
    {
        x=0,y=0;
        if (i < 1)
        {
            cin >> x;
            x=x-1;
            v.erase(v.begin() + x);
        }
        else
        {
            cin >> x >> y;
            x=x-1;
            y=y-1;
            v.erase(v.begin()+x,v.begin()+y);
        }
    }

    cout<<v.size()<<"\n";
    for(int z:v){
        cout<<z<<" ";
    }

    return 0;
}
