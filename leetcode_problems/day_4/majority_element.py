nums = [3,2,3]

for i in nums:
    count = nums.count(i)
    if count > len(nums)//2:
        print(i)
        break


    