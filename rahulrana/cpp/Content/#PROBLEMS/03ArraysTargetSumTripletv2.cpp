# include <iostream>
# include <algorithm>
using namespace std;

int main ()
{
    int size;
    cin >> size;

    // take array as the input now
    int arr[size];
    for (int i = 0; i < size; i ++)
        cin >> arr[i];

    int target;
    cin >> target;

    // sort the array
    sort(arr, arr+size);

    for(int i = 0; i < size-2; i ++)
    {
        int p1 = i+1;
        int p2 = size-1;
        while(p1 < p2)
        {
            if (arr[i] + arr[p1] + arr[p2] == target)
            {
                cout << arr[i] << ", " << arr[p1] << " and " << arr[p2] << endl;
                p1++;
                p2--;
            }
            else if (arr[i] + arr[p1] + arr[p2] < target)
            {
                p1++;
            }
            else
            {
                p2--;
            }
        }
    }
    return 0;
}