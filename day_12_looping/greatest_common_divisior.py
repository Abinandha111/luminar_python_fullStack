num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))

gcd=1

small_num=min(num1,num2)

for i in range(2,small_num+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)
