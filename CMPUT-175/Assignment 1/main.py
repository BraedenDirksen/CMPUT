def checkShelves():
    f = open('onshelves.txt','r')
    rawData = f.readlines()
    f.close()
    for index in range(len(rawData)):
        rawData[index] = rawData[index].strip()
        rawData[index] = rawData[index].split('#')
    

    print(rawData)



checkShelves()
input()