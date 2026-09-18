arr = [1,2,3,5,4,6,7,9]

arr.sort()

l=0


while l<len(arr)-1:

    r=l+1

    difference = arr[r] - arr[l]

    if difference!=1:

        print(arr[l]+1)

        break


    l=l+1