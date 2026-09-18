'''
least positive missing number

set arr=[1,2,4]

find min of arr

find max of arr

set total as zero

repeat for n from min to max+1 then


    find total = total +n

find sum of arr


if total!=sum of arr:

    display the difference between total and sum of arr

else then

   display no missing

'''



arr = [1,2,3,4,6]

min_num=min(arr)

max_num=max(arr)

total = 0

for n in range(min_num,max_num+1):

    total = total+n
arr_sum = sum(arr)

if total!=arr_sum:

    print("missing number:",total-arr_sum)

else:

    print("no missing number")