"""
Armstrong number

read num
set digit_count=len(str(num))
set result=0

repeat while num!=0:
    set digit=num%10
    set result=result+digit**digit_count
    set num=num//10
display result

"""
num=int(input("Enter a number:"))

digit_count=len(str(num))

result=0

while num!=0:
    digit = num % 10
    result = result+digit**digit_count
    num = num//10

print(result)

