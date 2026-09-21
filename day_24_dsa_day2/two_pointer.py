"""
arr = [1,3,5,7,2,6,4]

target = 11

set left as 0

set right as len(arr)-1

repeat while left<right 

    calculate cur_sum=arr[left]

    chk cur_sum == target then
       display arr[left] and arr[right]

    chk cur_sum > target then

       update right as right - 1

    chk cur_sum < target then

      update left as left + 1


"""

arr = [1,3,5,7,2,6,4]

arr.sort()

target = 11

left=0

right=len(arr)-1

while(left<right):

    cur_sum = arr[left] + arr[right]

    if cur_sum == target:

        print(arr[left],arr[right])

        break

    elif cur_sum > target:

        right = right - 1

    elif cur_sum < target:

        left = left + 1





