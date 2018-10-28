shardsList = [0]
xpList = [50]
for i in range (1,5):
    shardsList.append(1300)
    xpList.append(200+i*100)
for i in range(1,7):
    shardsList.append(2400)
    xpList.append(800+i*100)
for i in range(1,7):
    shardsList.append(3200)
    xpList.append(1600+i*100)
for i in range(1,8):
    shardsList.append(3200)
    xpList.append(2400+i*100)
xpList.append(6800)
shardsList.append(9700)
print(xpList)
print(shardsList)
heroLevel = int(input("Input current hero level"))
desiredLevel = int(input("Input desired hero level"))
xpTotal = (sum(xpList[heroLevel:desiredLevel]))
shardsEarned = sum(shardsList[heroLevel:desiredLevel])
print(xpTotal, " XP required.")
print(shardsEarned, " shards earned.")
print(xpTotal/100, " accounts required.")
print(xpTotal/600, " hours.")