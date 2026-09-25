# numbers = [1, 2, 3, 4, 5, 6]

# left = 0

# right = len(numbers) - 1

# while left<right:

#     print(numbers[left],numbers[right])

#     left = left + 1

#     right = right - 1



# numbers = [1, 2, 3, 4, 6]
# target = 7


# left = 0 

# right = len(numbers) - 1


# while left<right:

#     cur_sum = numbers[left] + numbers[right]

#     if cur_sum==target:

#         print(numbers[left],numbers[right])
#         left+=1
#         right-=1
        
        
#     elif cur_sum>target:

#         right-=1

#     elif cur_sum<target:

#         left+=1




# numbers = [-7, -3, 5, 2, 9]

# closest = numbers[0]

# for i in numbers:

#     if abs(i)<abs(closest):

#         closest=i

# print(closest)



# numbers = [-7, -3, 5, 2, -2, 9]

# closest = numbers[0]

# for i in numbers:

#     if abs(i) < abs(closest) or (abs(i) == abs(closest) and i > closest):

#         closest=i

# print(closest)





# arr = [1,2,3,4,6]

# missing = 1

# while missing in arr:
#     missing += 1

# print(missing)



# arr = [1, 2, 5, 6]

# min_num = min(arr)
# max_num = max(arr)

# for n in range(min_num, max_num + 1):
#     if n not in arr:
#         print(n)