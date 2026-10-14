digits = [1,2,9]

for i in range(len(digits)-1,-1,-1):

    if digits[i] + 1 != 10:

        digits[i]+=1

        print(digits)
        break

    digits[i]=0

    if i==0:
        print([1] + digits)