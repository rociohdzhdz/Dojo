#Biggie Size Function that changes all positive numbers in the list to Big
def Biggie(List1):
    ListN1=[]
    for x in range(0,len(List1),1):
        if List1[x]>0:
            ListN1.append("Big")
        else:
            ListN1.append(List1[x])
    return ListN1
print(Biggie([-1,4,5,6,-7]))

#Count Positives****************
def CountPos(List2):
    ListN2=[]
    CountP=0
    for y in range(0,len(List2),1):
        if List2[y]>0:
            CountP+=1
            if y==len(List2):
                ListN2.append(CountP)
        else:
            ListN2.append(List2[y])
    return ListN2
print(CountPos([-2,-3.-4.-6,3,2,1]))

#SumTotal
def SumTotal(List3):
    Sum=0
    for st in range(0,len(List3),1):
        Sum+=List3[st]
    return Sum
print(SumTotal([6,7,8,2,4]))

#Average
def Avg(List4):
    S=0
    for a in range(0,len(List4),1):
        S+=List4[a]
    return S/len(List4)
print(Avg([2,3,4,5]))

#Length
def length(List5):
    return len(List5)
print(length([9,8,7,6,5,4]))

#Minimum
def Minimum(List6):
    if len(List6)>0:
        Mi=List6[0]
        for w in range(1,len(List6),1):
            if Mi>List6[w]:
                Mi=List6[w]
            else:
                Mi=Mi
        return Mi
    else:
        Mi=False
        return Mi
print(Minimum([37,2,9,-4]))

#Maximum
def Maximum(List7):
    if len(List7)>0:
        Ma=List7[0]
        for m in range(1,len(List7),1):
            if Ma<List7[m]:
                Ma=List7[m]
            else:
                Ma=Ma
        return Ma
    else:
        Ma=False
        return Ma
print(Maximum([37,2,9,-4]))

#Ultimate analysis
def ultimatea(List8):
    res={
        'SumTot':None,
        'max':None,
        'min':None,
        'avg':None,
        'length':0
    }
    if len(List8)==0:
        return res
    else:
        res['SumTot']=0
        res['max']=List8[0]
        res['min']=List8[0]
    for r in List8:
        if r>res['max']:
            res['max']=r
        elif r<res['min']:
            res['min']= r
        res['SumTot']+= r
        res['length']+= 1
    res['avg']=res['SumTot']/length(List8)

    return res
print(ultimatea([30,2,1,-9]))

#Reverse
def reverse(List9):
    half = int(len(List9) / 2)
    for re in range(half):
        List9[re] , List9[len(List9) - 1 - re] = List9[len(List9) - 1 - re], List9[re]
    return List9

print(reverse([37, 2, 1, -9, 5]))
