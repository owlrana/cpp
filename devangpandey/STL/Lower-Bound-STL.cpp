#include <bits/stdc++.h>
#include <algorithm>
#include <functional>
#include <iostream>
using namespace std;
typedef long ll;

int main()

{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, query, temp;
    cin >> n;
    vector<int> vec(n);
    for (int i = 0; i < n; i++)
    {
        cin >> vec[i];
    }
    sort(vec.begin(), vec.end());
    cin >> query;

    vector<int>::iterator it,it2;
    for (int i = 0; i < query; i++)
    {
        temp = 0;
        cin >> temp;
        it = lower_bound(vec.begin(), vec.end(), temp);
        if(*it==temp){
            cout<<"Yes "<<it-vec.begin()+1<<endl;
        }
        else{
            cout<<"No "<<it-vec.begin()+1<<endl;
        }
    }
    return 0;
}
