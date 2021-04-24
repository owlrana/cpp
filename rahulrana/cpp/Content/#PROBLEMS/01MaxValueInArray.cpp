# include <iostream>
using namespace std;

int main ()
{
    int size;
    cin >> size;

    int arr[size];

    int max = INT_MIN; // initialising the max element as a very small value
    
    // taking array as the input
    for (int i = 0; i < size; i ++)
    {
        cin >> arr[i];

        // computing the bigger element while taking the input
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    
    cout << "The biggest element in the array is: " << max << endl;

    return 0;
}