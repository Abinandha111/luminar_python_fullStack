prices=[7,1,5,3,6,4]

nextBuy=0
nextHold=0

currentBuy=0
currentHold=0
for i in range(len(prices)-1,-1,-1):
    currentBuy = max(-prices[i]+nextHold,nextBuy)
    currentHold = max(prices[i],nextHold)

    nextBuy = currentBuy
    nextHold = currentHold
print(currentBuy)