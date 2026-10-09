
nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        result = nums[i] + nums[j]
        if result == target:
            print("The indices of the two numbers are:", [i, j])

