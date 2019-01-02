#**********************************************************#
#*  name	:动态规划算法								  *#
#* 	author	:张祥春										  *#
#* 	create time	:2018/05/08								  *#
#* 	modify time	:2018/05/08								  *#
#* 	introduction:动态规划算法练习						  *#
#*				 dynamic programming algorithm			  *#
#**********************************************************#
#背包问题————————————————————————————————————————————————————————————
#动态规划算法
def dynamic(dicThing, intLen):
    dicTemp = dict(dicThing)
    listBest_thing = list()
    i = 0
    for item_key, item_value in dicTemp.items():
        listBest_thing.append(list())
        for j in range(0, intLen - 1):
            if listBest_thing[i-1][j] > (listBest_thing[i-1][j+1-item_key] + item_value):
                listBest_thing[i].append(listBest_thing[i-1][j])
            else:
                listBest_thing[i].append(listBest_thing[i-1][j+1-item_key] + item_value)
                


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

#定义原始数据的散列表
dicThing = {"guitar": [1, 1500], "sounder": [4, 3000], "notebook": [3, 2000], "iphone": [1, 2000]}
intBag_len = 4
listBest_thing = dynamic(dicThing, intBag_len)