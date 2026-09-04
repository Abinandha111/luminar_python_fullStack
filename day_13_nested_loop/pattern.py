""" 1)

* * *
* * *
* * *
* * *
"""

# for i in range(1,5):
#     for j in range(1,4):
#         print("*",end=" ")
#     print()

""" 2)

* * * * *
* * * * *
* * * * *
* * * * *
"""

# for i in range(1,5):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()


""" 3)

$ $ $ $ $ $ $
$ $ $ $ $ $ $
$ $ $ $ $ $ $
$ $ $ $ $ $ $
"""

# for row in range(1,5):
#     for col in range(1,8):
#         print("$",end="\t")
#     print()


""" 4)

1 2 3 4
1 2 3 4
1 2 3 4
"""

# for row in range(1,4):
#     for col in range(1,5):
#         print(col,end="\t")
#     print()



""" 5)

1 2 3 4 5 6 7 
1 2 3 4 5 6 7
1 2 3 4 5 6 7
"""

# for row in range(1,4):
#     for col in range(1,8):
#         print(col,end="\t")
#     print()

""" 6)

O E O E O E 
O E O E O E
O E O E O E
O E O E O E
"""

# for row in range(1,5):
#     for col in range(1,6):
#         if col%2==0:
#             print("E",end="\t")
#         else:
#             print("O",end="\t")
#     print()

""" 7)

* 2 * 4 
* 2 * 4
* 2 * 4
* 2 * 4
"""

# for row in range(1,5):
#     for col in range(1,5):
#         if col%2!=0:
#             print("*",end="\t")
#         else:
#             print(col,end="\t")
#     print()


""" 8)

1 E 1 E 1 E
2 E 2 E 2 E
3 E 3 E 3 E
"""

# for row in range(1,4):
#     for col in range(1,7):
#         if col%2!=0:
#             print(row,end="\t")
#         else:
#             print("E",end="\t")
#     print()


""" 9)

# # # # #
#
#
#
"""

for row in range(1,5):
    for col in range(1,6):
        if row==1 or col==1:
            print("#",end=" ")
    print()

