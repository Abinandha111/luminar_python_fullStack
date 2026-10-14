class Solution:
    def singleNumber(self, nums):
        result=0
        for i in nums:
            result = result^i

        return result

solution_instance = Solution()
print(solution_instance.singleNumber([4,1,2,1,2]))  # Output: 4