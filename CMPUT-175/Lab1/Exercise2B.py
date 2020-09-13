
def readFile(): # reads file and returns the contents
    f = open('earthquake.txt','r')
    contents = f.readlines()
    f.close
    return contents

def formatContents(li): # formats the contents from the file in order to be written to the new file
    uniqueItems = []
    formatedList = []
    for i in range(len(li)): # splits the list into items at every space and then removes \n then saves all the unique places to a new list
        li[i] = li[i].split(' ')
        li[i][-1] = li[i][-1].rstrip()
        if not li[i][-1] in uniqueItems:
            uniqueItems.append(li[i][-1])
    for f in range(len(uniqueItems)): # adds the items to the finished list
        formatedList.append([uniqueItems[f]])
        temp = []
        for i in range(len(li)): # creates every earthquakes date and size to the list in it's respective place
            if li[i][-1] == uniqueItems[f]:
                temp.append([li[i][1],li[i][0]])
        for item in temp: # adds the temp list to finished list
            formatedList[f].append(item)
    formatedStr = '' 
    for item in formatedList: # formats the list into a str to be written to the file
        formatedStr += str(item) + (2*'\n')
    formatedStr = formatedStr.replace("'","")
    return formatedStr

def writeToFile(completeStr): # writes the contents of the file to new file
    f = open('earthquakefmt.txt', 'w')
    f.write(completeStr)
    f.close

writeToFile(formatContents(readFile()))

'''
Create a Python program that reads the data stored in the provided earthquake.txt,
where each line in the text file contains an earthquake magnitude, the date of the earthquake, the time, 
latitude, longitude, depth, and region, all separated by whitespace.  
Use the data to create lists of earthquake magnitudes and their dates, one for each region. 
Write these lists (in any order) to a new file called earthquakefmt.txt, 
formatted to match the sample output below.

Exercise 2B: Sample Output: 
[ALASKA, [2006/10/19, 2.8], [2006/10/18, 2.6], [2006/10/18, 2.7], [2006/10/18, 2.7], [2006/10/18, 2.8]] 

[HAWAII, [2006/10/19, 2.5], [2006/10/20, 3.1]] 

[PANAMA, [2006/10/18, 5.0]] 

[MISSOURI, [2006/10/18, 3.4]] 

[INDONESIA, [2006/10/20, 4.9]] 

[VANUATU, [2006/10/18, 6.2]] 

[MEXICO, [2006/10/20, 2.8], [2006/10/18, 3.3]]
'''