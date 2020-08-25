arrNowList=[6,7,9,4,3,1,0]
def bubbles(arrNowList):
    for j in range(0,(len(arrNowList)-1),1):
        for i in range (0,(len(arrNowList)-1-j),1):
            print ("index", i, "value", arrNowList[i])
            print("comparing", arrNowList[i], arrNowList[i+1])
            if arrNowList[i]>arrNowList[i+1]:
                arrNowList[i],arrNowList[i+1]=arrNowList[i+1],arrNowList[i]
                print(arrNowList[i],arrNowList[i+1])
                #print()
    return arrNowList
print(bubbles(arrNowList))