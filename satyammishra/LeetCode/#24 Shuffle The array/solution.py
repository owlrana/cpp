class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        list_1 = []
        for i in range(n):
            list_1.append(nums[i])
            list_1.append(nums[i+n])
        return list_1