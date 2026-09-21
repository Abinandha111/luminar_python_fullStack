'''
arr = [3,4,5,8,1,7,6]
k=3


'''

arr = [3,4,5,8,1,7,6]
k=3


window_sum=sum(arr[:k])

max_sum=window_sum


for i in range(k,len(arr)):

    window_sum=window_sum-arr[i-k]+arr[i]

    if window_sum>max_sum:

        max_sum=window_sum

print(max_sum)
