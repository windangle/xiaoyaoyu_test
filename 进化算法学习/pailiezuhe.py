COUNT = 81
result = item = ["b","w"]
temp = []
for x in range(1,COUNT):
    for y in range(0,len(result)):
        for z in range(0,len(item)):
            temp.append(result[y] + item[z])
    result = temp
    temp = []
    print("Have do %d/81，result's len is %d" %(x, len(result)))
print(len(result))
#print(result)