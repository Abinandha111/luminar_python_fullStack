
"""
read num

set is_prime=True

repeat for i in range(2,num):
    if num%i==0:
        set is_prime=False
        break
display is_prime
"""


num=int(input("Enter a number:"))

is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
print(is_prime)


