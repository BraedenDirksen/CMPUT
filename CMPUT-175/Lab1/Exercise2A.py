def readFile(): # reads file and returns the contents
    f = open('rainfall.txt','r')
    contents = f.readlines()
    f.close
    return contents

def formatContents(contents):
    for i in range(len(contents)):
        contents[i] = contents[i].rstrip()
        contents[i] = contents[i].split(' ')
        contents[i][1] = float(contents[i][1])
        if contents[i][1] <= 70:
            contents[i].append(70)
        elif contents[i][1] <= 80:
            contents[i].append(80)
        elif contents[i][1] <= 90:
            contents[i].append(90)
        elif contents[i][1] <= 100:
            contents[i].append(100)     
    completeStr = ''
    completeStr += '[50-60 mm) [60-70 mm)\n'
    for item in contents:
        if item[2] == 70:
            completeStr += item[0].center(25) + '%5.1f'%(item[1]) + '\n'
    completeStr += '\n[70-80 mm)\n'
    for item in contents:
        if item[2] == 80:
            completeStr += item[0].center(25) + '%5.1f'%(item[1]) + '\n'
    completeStr += '\n[80-90 mm)\n'
    for item in contents:
        if item[2] == 90:
            completeStr += item[0].center(25) + '%5.1f'%(item[1]) + '\n'
    completeStr += '\n[90-100 mm)\n'
    for item in contents:
        if item[2] == 100:
            completeStr += item[0].center(25) + '%5.1f'%(item[1]) + '\n'
    return completeStr

def writeToFile(completeStr): # writes the contents of the file to new file
    f = open('rainfallfmt.txt', 'w')
    f.write(completeStr)
    f.close

writeToFile(formatContents(readFile()))

'''
Exercise 2A: Create a Python program that reads the data stored in the provided rainfall.txt,
where each line in the text file contains the name of a city,
followed by whitespace, followed by the city’s annual rainfall (in mm).  
Process this data so that it is grouped by annual rainfall into the following categories:
[50-60 mm), [60-70 mm), [70-80 mm), [80-90 mm), [90-100 mm], 
and then sorted from lowest to highest rainfall within each category.  
Write this processed data to a new file called rainfallfmt.txt, 
so that under each category the city name is centered in a field that is 25 characters wide and 
is in all uppercase letters.  The city name should be followed by its rainfall, right-aligned in a 
field that is 5 characters wide with 1 digit to the right of the decimal point. 
 
Exercise 2A: Sample Output: 
[50-60 mm) [60-70 mm)
           AKRON           65.6
           ALTON           69.7 
[70-80 mm)
           ALGONA          78.0 
[80-90 mm)           
           BRITT           80.1
          CARROLL          84.7           
           ANKENY          84.8 
... 
'''