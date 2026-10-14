class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=0
        
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        for i in range(pos,len(nums)):
            nums[i]=0

nums = [0, 1, 0, 3, 12]
solution_instance = Solution()
solution_instance.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]