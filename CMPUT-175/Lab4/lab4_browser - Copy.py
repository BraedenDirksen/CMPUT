#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

def getAction():
    '''
    repeatedly asks for input from user until input is '=', '<' or '>'
    Inputs: choice
    Returns: choice
    '''
    choice = input('Enter = to enter a URL, < to go back, > to go forward, q to quit: ')
    while choice != '=' and choice != '<' and choice != '>' and choice.lower() != 'q':
        print(choice, 'is not a Invalid entry.')
        choice = input('Enter = to enter a URL, < to go back, > to go forward, q to quit: ')
    return choice.lower()



def goToNewSite(current, pages):
    '''
    removes everything ahead of the current position them appends new site and moves the index to that site
    Inputs: current, pages
    Returns: current, pages
    ''' 
    if current + 1 < len(pages):
        pages = pages[:(current + 1)]
    pages.append(input("URL: "))
    return current + 1, pages

def goBack(current, pages):
    '''
    lowers the index by one if there is a site behind it
    Inputs: current, pages
    Returns: current
    '''    
    if current - 1 < 0:
        print("Cannot go backwards")
        return current
    else:
        return current - 1

def goForward(current, pages):
    '''
    increases the index by one if there is a site ahead of it
    Inputs: current, pages
    Returns: current
    '''
    if current + 1 >= len(pages):
        print("Cannot go forward")
        return current
    else:
        return current + 1

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex, websites = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    
        
if __name__ == "__main__":
    main()
    