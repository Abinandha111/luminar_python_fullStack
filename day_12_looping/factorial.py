"""
factorial of a number

read number
set factorial=1

repeat for i in range(1,number+1):
    set factorial=factorial*i
display factorial

"""
number=int(input("Enter a number:"))

factorial=1

for i in range(1,number+1):

    factorial=factorial*i

print(factorial)