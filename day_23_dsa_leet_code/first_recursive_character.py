'''
first recursive character

set s as leetcode

create an empty list as lst

repeat for char from s:

    check if char not in lst:

        add char to lst

    else:
     
        display char

        exit

'''


s="leetcode"

lst=[]

for char in s:

    if char not in lst:

        lst.append(char)

    else:

        print("First Recursive Character is",char)

        break

