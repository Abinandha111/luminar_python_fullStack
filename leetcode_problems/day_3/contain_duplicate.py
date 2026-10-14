class Solution:
    def containsDuplicate(self, nums):
        lst=[]
        for i in nums:
            if i in lst:
                
                return True
            else:

                lst.append(i)
        return False

solution_instance = Solution()
print(solution_instance.containsDuplicate([1, 2, 3, 4, 5]))  
print(solution_instance.containsDuplicate([1, 2, 3, 1]))  
