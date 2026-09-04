"""

Fibonacci Series

set pre as 0
set current as 1

display pre
display current

repeat for i in range(1,11):
    set next as pre+current
    display next
    set pre as current
    set current as next
"""

pre=0
current=1
print(pre)
print(current)

for i in range(1,11):
    
    next=pre+current
    print(next)
    pre=current
    current=next




