/*Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.*/
class Solution {
    public:
        int numIdenticalPairs(vector < int > & nums) {
            int good = 0;
            for (int i = 0; i < nums.size(); i++)
                for (int j = i; j < nums.size(); j++) {
                    if (nums[i] == nums[j] && i < j)
                        good++;
                }
            return good;
        }
};