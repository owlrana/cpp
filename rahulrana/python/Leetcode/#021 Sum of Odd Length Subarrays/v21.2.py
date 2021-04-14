# Even length subarrays

def OddLengthSum(arr):
 
    # Stores the sum
    Sum = 0
 
    # Size of array
    l = len(arr)
 
    # Traverse the given array arr[]
    for i in range(l):
     
        # Add to the sum for each
        # contribution of the arr[i]
        Sum += ((((i) *
                  (l - i + 1) +
                 1) // 2) * arr[i])
     
    # Return the final sum
    return Sum
 
# Driver code 
 
# Given array arr[]
arr = [1,2,3,4,5]
 
# Function call
print(OddLengthSum(arr))