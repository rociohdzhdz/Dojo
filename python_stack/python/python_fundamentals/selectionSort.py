
def selection(arrNowList):
    for i in range (0,(len(arrNowList)-1),1):
        midx=i
        for j in range(i+1, len(arrNowList)):
            if arrNowList[midx]>arrNowList[j]:
                midx=j
                #print(midx)
        arrtemp=arrNowList[i]
        arrNowList[i]=arrNowList[midx]
        arrNowList[midx]=arrtemp
    return arrNowList
print(selection([6,7,9,4,3,1,0]))