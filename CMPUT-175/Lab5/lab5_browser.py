#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: Braeden Dirksen
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    prompts user for a choice then if choice is =,<,> or q it returns 
    the choice if not it raises an execption
    Inputs: None
    Returns: choice
    '''
    #delete pass and write your code here
    choice = input('Enter = to enter a URL, < to go back, > to go forward, q to quit: ')
    if choice == '=' or choice == '<' or choice == '>' or choice == 'q':
        return choice
    else:
        raise Exception('Invalid Entry')

def goToNewSite(current, bck, fwd):
    '''
    adds the current to the back stack and resets the forward 
    stack then returns a new current
    Inputs: current, bck, fwd
    Returns: new current
    '''   
    #delete pass and write your code here
    bck.push(current)
    fwd.clear()
    return input("URL: ")
    
def goBack(current, bck, fwd):
    '''
    moves current to fwd, moves bck to current, returns error. if gets error 
    removes the pushed current and returns current as well as printing error
    Inputs: current, bck, fwd
    Returns: bck.pop()
    '''    
    #delete pass and write your code here
    fwd.push(current)
    try:
        return bck.pop()
    except Exception as error:
        print(error)
        fwd.pop()
        return current


def goForward(current, bck, fwd):
    '''
    moves current to bck, moves fwd to current, returns error. if gets error 
    removes the pushed current and returns current as well as printing error
    Inputs: current, bck, fwd
    Returns: fwd.pop()
    '''    
    #delete pass and write your code here
    bck.push(current)
    try:
        return fwd.pop()
    except Exception as error:
        print(error)
        bck.pop()
        return current


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            else:
                quit = True
            #TO DO: add code for the other valid actions ('<', '>', 'q')
            #HINT: LOOK AT LAB 4
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    