'''
first non_recursive character and return its index

set s as loveleetcode

repeat for each char from s:

    chk if count of char in s == 1 then

         display index of char then

         break
        

'''


s="loveleetcode"

for char in s:

    if s.count(char)==1:

        print(s.index(char))

        break

else:

    print(-1)