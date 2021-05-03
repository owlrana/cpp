/*
    Very important question and has been asked in a LOT of interview problems
*/

# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;

bool canCowBePlaced(vector<int> stalls, int n, int mid, int cows)
{
    int last_cow_placed = stalls[0];
    int count = 1;
    
    for (int i = 1; i < n; i ++)
    {
        if (stalls[i] - last_cow_placed >= mid)
        {
            last_cow_placed = stalls[i];
            count += 1;

            if (count == cows)
                return true;
        }
    }
    return false;
}

int main ()
{
    vector<int> stalls {79,74,57,22};
    sort(stalls.begin(), stalls.end());
    int n = stalls.size();
    int cows = 4;

    // binary search algorithm
    int start = 0;
    int end = stalls[n-1] - stalls[0];
    int ans = 0;
    
    cout << start << endl;
    while(start <= end)
    {
        int mid = (start + end) / 2;
        cout << "MID is: " << mid << endl;

        bool placeable = canCowBePlaced(stalls, n, mid, cows);
        
        if (placeable)
        {
            ans = mid;
            cout << "ANS is set to: " << ans << endl;
            start = mid + 1;
            cout << "START changed: " << start << ", End: " << end << endl;
        }
        else
        {
            end = mid - 1;
            cout << "END changed: " << end << ", Start: " << start <<endl;
        }
    }
    
    cout << ans << endl;
    
    return ans;
}