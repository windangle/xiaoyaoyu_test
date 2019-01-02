#一组数的最大公约数
def commondivisor(listNum):
    intCommon_divisor = listNum[0]
    for item in listNum:
        intCommon_divisor = euclidean(item, intCommon_divisor)
    return intCommon_divisor
#两个数的最大公约数
def euclidean(intA, intB):
    if intA < intB:
        intA, intB = intB, intA
    if (intA % intB) == 0:
        return intB
    else:
        return euclidean(intB, intA-intB)

#
listInt = [12,24,36,88]
print(commondivisor(listInt))