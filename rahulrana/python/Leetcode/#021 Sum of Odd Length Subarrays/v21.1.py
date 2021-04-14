# Using formula from GFG for sum of odd lenght subarray
# basis for even length sum in v21.2

def OddLengthSum(arr):
 
    # Stores the sum
    Sum = 0
 
    # Size of array
    l = len(arr)
 
    # Traverse the given array arr[]
    for i in range(l):
     
        # Add to the sum for each
        # contribution of the arr[i]
        Sum += ((((i + 1) *
                  (l - i) +
                 1) // 2) * arr[i])
    
    # Return the final sum
    return Sum
 
# Driver code 
 
# Given array arr[]
arr = [ 1, 5, 3, 1, 2 ]
 
# Function call
print(OddLengthSum(arr))