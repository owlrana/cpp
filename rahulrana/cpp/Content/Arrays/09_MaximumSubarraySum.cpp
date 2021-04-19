// Give an array, we need to give the maximum sum that any subarray may have
// Eg. of the array {-4, 1, 2, 3, 4, -10}, the max sum is of {1, 2, 3, 4} subarray!

// procedure: 1. Generate sums for all subarrays
//            2. Find the largest sum, return it

# include <iostream>

using namespace std;

int main() 
{   
    int n;
    cin >> n;

    int arr[1000];

    for (int i =0; i<n; i ++) {
        cin >> arr[i];
    }

    int max_sum = 0;
    int curr_sum = 0;

    int left = -50; // to find out which subarray it is
    int right = -50;

    // Generate all subarrays
    for (int i = 0; i < n; i++) { // iteration to decide the starting point of start index i
        for (int j = i; j < n; j++) { // iteration to decide the starting point of start index j
            
            curr_sum = 0; // initialise each time before calculating the sum of a new subarray
            for(int k = i; k <= j; k++) { // prints elements of current subarray from i, to j
                curr_sum += arr[k]; // calculating the sum of all elements in this subarray
            }
            // cout << curr_sum << endl; // Check the sum of all subarrays calculated
            max_sum = max(curr_sum, max_sum); // update the maximum sum
            // assigning the start and end of the subarray which so far has the highest sum
            if (max_sum == curr_sum) { // if the max_sum was caught right now!!
                left = i;
                right = j;
            } // to make this to catch in minimum no. strings in case larger strings also have same sum
            // just keep another variable of no. of strings and if the no. of strings is less, only then do it
        }
    }

    cout << max_sum << endl;

    // subarray can be outputted using loop from i till j (including both)
    for (int i = left; i <= right; i ++) {
        cout << arr[i] << ", ";
    }

    return 0;
}

// this is very time consuming as it has 3 nested loops
// thus we will optimise this next