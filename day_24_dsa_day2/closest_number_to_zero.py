"""
arr = [-2,-1,1,2,3]


"""



nums = [-2,-1,1,2,3]   

closest = nums[0]

for num in nums:

    if abs(num) < abs(closest):

        closest=num


if closest < 0 and abs(closest) in nums:

    print(abs(closest))

else:

    print(closest)