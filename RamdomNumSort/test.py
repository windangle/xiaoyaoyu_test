import random
import time

# 排序结果输出
def OutputTxt(list):
    txt_path = 'D://Test/RamdomNumSort/listNum.txt'
    txtList = open(txt_path, "w")
    for intItom in list:
        txtList.write('%s,' % (intItom))
    txtList.close()


# 冒泡排序
def Maopao(list):
    for i in range(0, len(list) - 2):
        for j in range(i + 1, len(list) - 1):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list
def Maopao(list):
    for itemi in list[:-1]:
        i = 0
        for itemj in list[i+1:]:
            j = i + 1
            if itemi > itemj:
                list[i], list[j] = list[j], list[i]
            j += 1
        i += 1
    return list


# 递归法排序
def MergeSort(list):
    intLen = len(list)
    if intLen < 2:
        return list
    intMid = int(intLen / 2)
    intMidItem = list[intMid]
    listSmall = []
    listLarge = []
    for intItem in list[:intMid - 1] + list[intMid + 1:]:
        if intItem < intMidItem:
            listSmall.append(intItem)
        else:
            listLarge.append(intItem)
    return MergeSort(listSmall) + [intMidItem] + MergeSort(listLarge)


# 二分法在有序列表中查找插入位置
def BinarySearch(list, intSearch):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = int((low + high) / 2)
        intMid = list[mid]
        if intMid == intSearch:
            return mid
        if intMid > intSearch:
            high = mid
        else:
            low = mid = mid + 1
    if list[mid] > intSearch:
        return mid
    else:
        return mid + 1


# 二分法排序
def BinarySort(list):
    if list[0] < list[1]:
        listSortNum = [list[0], list[1]]
    else:
        listSortNum = [list[1], list[0]]
    for item in list[2:]:
        intSearchItem = BinarySearch(listSortNum, item)
        listSortNum.insert(intSearchItem, item)
    return listSortNum

#————————程序主体————————
txt_path = 'D://Test/RamdomNumSort/listRandomNum.txt'
txtRandomList = open(txt_path, "r")
strRandomList = txtRandomList.readline()
strRandomNum = strRandomList.split(',')
txtRandomList.close()
listRandomNum = []
for strItem in strRandomNum:
    listRandomNum.append(int(strItem))
intStartTime = time.clock()
# ————————————————————————————————————————————————————————————————————————————————————————————————————————
# 用冒泡算法排序一万个数字，耗时 209056.97861316 秒
# listSortNum = Maopao(listRandomNum)
# 用二分法排序100万个数字，耗时 379.31703516 秒
#listSortNum = BinarySort(listRandomNum)
# 用递归法排序100万个数字，耗时 5.23203716, 5.79696616, 5.78935616, 5.56801416, 6.27461216 秒
#listSortNum = MergeSort(listRandomNum)
# 用字符串排序函数排序100万个数字，耗时 0.72679816, 0.94117216, 0.91381816, 0.78649616, 0.86126616 秒
listRandomNum.sort()
listSortNum = listRandomNum
# ————————————————————————————————————————————————————————————————————————————————————————————————————————
intFinishTime = time.clock()
intTimeLen = intFinishTime - intStartTime
print("%f16" % (intTimeLen))
OutputTxt(listSortNum)