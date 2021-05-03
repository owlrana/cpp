// https://leetcode.com/problems/number-of-different-integers-in-a-string/

# include <iostream>
# include <algorithm>
# include <cstring>
# include <vector>

using namespace std;

int main ()
{
    string word = "2t534241200048821186703855206305519741412814322625714669955759026901002406955031068784h534241200048821186703855206305519741412814322625714669955759026901002406955031068784g534241200048821186703855206305519741412814322625714669955759026901002406955031068784i534241200048821186703855206305519741412814322625714669955759026901002406955031068784au29q9d4o3ui7xiewh4tikuki1zzq7ebe42asjfb9qi04bqskgagdqdw2k21hu98kczsdblci19744r";
    long double size = word.size();
    float tenth = 0.1;
    long double number = 0;
    vector<int> numlist;

    for (int i = size-1; i >= 0; i--)
    {   

        if (isdigit(word[i]))
        {
            number = number + (int(word[i])-48)*tenth*10;
            tenth = tenth * 10;
        }
        else if (isdigit(word[i+1]))
        {
            numlist.push_back(number);
            number = 0;
            tenth = 0.1; 
        }
    }
    
    cout << endl << "THE VECTOR OF ARRAYS:" << endl;
    for (auto x: numlist)
        cout << x << ", ";
    cout << endl;

    // sorting the vector
    sort(numlist.begin(), numlist.end());

    vector <int> uniquelist;
    // removing duplicate elements
    numlist.erase( unique( numlist.begin(), numlist.end() ), numlist.end() );

    cout << endl << "AFTER REMOVING DUPLICATE ELEMENTS: " << endl;
    for (auto x: numlist)
        cout << x << ", ";
    cout << endl;

    cout << numlist.size();

    return 0;
}