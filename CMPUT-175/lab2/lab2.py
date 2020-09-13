def getInputFile(filename):
    ''' input is filename, if no filename it asks for one. After it checks filename for .txt, 
    if it doesn't have that it repeats the function until user inputs .txt input then returns that'''
    if filename == None:
        filename = input("Enter the input filename:  ")
    if filename[-4:] != ".txt":
        filename = getInputFile(input("Invalid filename extension.  Please re-enter the input filename: "))
    return filename

def decrypt(filename):
    ''' using the filename it gets the key as well as the message from the file then moves letter back 
    by 1 time per the amount of the key, while also looping from a-z and ignoring spaces. 
    returns a str of the decrypted Message'''
    f = open(filename,'r')
    fileData = f.readlines()
    f.close()
    rawMsg = fileData[1].strip()
    key = int(fileData[0].strip())
    key = key%26

    rawList = []
    for letter in rawMsg:
        rawList.append(ord(letter.lower()))

    i = 0
    while i < key:
        for index in range(len(rawList)):
            if rawList[index] == 32:
                pass
            elif rawList[index] > 97:
                rawList[index] -= 1
            else:
                rawList[index] = 122
        i += 1

    decryptedStr = ''
    for number in rawList:
        decryptedStr += chr(number)

    return decryptedStr


print(decrypt(getInputFile(None)).lower())
input()