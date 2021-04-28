# include <iostream>
# include <algorithm>
using namespace std;

int main ()
{
    int size;
    cin >> size;
    int arr[size];
    // taking the input values of array
    for (int i = 0; i < size; i ++)
    {
        cin >> arr[i];
    }

    // taking input of "target"
    int target;
    cin >> target;

    sort(arr, arr + size); // sending memory location to sort

    // computing the pairs
    for (int i = 0; i < size; i ++)
        for (int j = i+1; j < size; j ++)
            if (arr[i] + arr[j] == target)
                cout << arr[i] << " and " << arr[j] << endl;
    return 0;
}

// this takes way too much time, check out v2 for a better code