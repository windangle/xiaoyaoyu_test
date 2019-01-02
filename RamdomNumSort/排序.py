#**********************************************************#
#*  name	:排序算法									  *#
#* 	author	:张祥春										  *#
#* 	create time	:2018/04/20								  *#
#* 	modify time	:2018/04/26								  *#
#* 	introduction:排序算法练习							  *#
#**********************************************************#
#直接插入排序：Straight Insertion Sort
#二分法插入排序： Binary Sort
#希尔排序：Shell Sort
#直接选择排序：Straight Select Sort
#堆排序：Heap Sort
#交换排序：Swap Sort
#快速排序：Quick Sort
#基数排序：Radix Sort
#归并排序：Merge sort

import random
import time


# 生成随机数素组
def RandomList(intLen, intMax=10000):
    listRandomNum = []
    for index in range(0, intLen - 1):
        listRandomNum.append(random.randrange(1, intMax))
    return (listRandomNum)


# 生成数据
def CreatData(intLen=10000, intRange=10000):
    txt_path = 'D://Test/RamdomNumSort/listRandomNum.txt'
    txtRandomList = open(txt_path, "w")
    listRandomNum = RandomList(intLen, intRange)
    for intRandom in listRandomNum:
        txtRandomList.write('%d,' % (intRandom))
    txtRandomList.write("\n")
    txtRandomList.close()


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
# 用冒泡算法排序一万个数字，耗时8.18625516，8.16953616，8.80700516，8.07070416，8.25285916秒
#listSortNum = Maopao(listRandomNum)
# 用二分法排序一万个数字，耗时0.08628516，0.08446116，0.08528116，0.08223716，0.08848616秒
#listSortNum = BinarySort(listRandomNum)
# 用递归法排序一万个数字，耗时0.02951316，0.04038516，0.02356916，0.02484716，0.02460916秒
#listSortNum = MergeSort(listRandomNum)
# 用字符串排序函数排序一万个数字，耗时0.00272816，0.00284416，0.00276916，0.00277816，0.00299816秒
listRandomNum.sort()
listSortNum = listRandomNum
# ————————————————————————————————————————————————————————————————————————————————————————————————————————
intFinishTime = time.clock()
intTimeLen = intFinishTime - intStartTime
print("%f16" % (intTimeLen))
OutputTxt(listSortNum)