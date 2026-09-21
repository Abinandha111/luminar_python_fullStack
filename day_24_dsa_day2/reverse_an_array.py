"""
reverse a given list without using reverse and slicing

"""

arr = [1,2,3,4,5]

reverse=[]

for i in range(0,len(arr)):

    popped_element=arr.pop()

    reverse.append(popped_element)

print(reverse)




arr = [10,50,20,30]
arr.sort()
left=0

right=len(arr)-1

while left<right:

    (arr[left],arr[right])=(arr[right],arr[left])

    left = left +1

    right = right - 1

print(arr)