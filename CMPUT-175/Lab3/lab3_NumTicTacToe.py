#----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: 
# Collaborators:
# References:
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass and print out formatted board
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |
        displayList = []
        for row in self.board:
            for item in row:
                if item == 0:
                    displayList.append(' ')
                else:
                    displayList.append(str(item))
        
                
        print('    0   1   2 ')
        print(' 0  '+ displayList[0] +' | '+ displayList[1] +' | '+ displayList[2] +' ')
        print('   -----------')
        print(' 1  '+ displayList[3] +' | '+ displayList[4] +' | '+ displayList[5] +' ')
        print('   -----------')
        print(' 2  '+ displayList[6] +' | '+ displayList[7] +' | '+ displayList[8] +' ')
        


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        # TO DO: delete pass and complete method
        try:
            if self.board[row][col] == 0:
                return True
            else:
                return False
        except IndexError:
            return False

    
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''

        if self.squareIsEmpty(row,col):
            self.board[row][col] = num
            return True
        else:
            return False


    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''

        full = True
        for row in self.board:
            for item in row:
                if item == 0:
                    full = False
        return full
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''

        testV,testV2,testV3 = [],[],[]
        for row in self.board:
            if sum(row) == 15:
                if not 0 in row:
                    return True
            testV.append(row[0])
            testV2.append(row[1])
            testV3.append(row[2])

        testVs = [testV,testV2,testV3]
        for row in testVs:
            if sum(row) == 15:
                if not 0 in row:
                    return True

        if self.board[0][0] + self.board[1][1] + self.board[2][2] == 15 and (not self.board[0][0] == 0 and not self.board[1][1] == 0 and not self.board[2][2] == 0) or self.board[0][2] + self.board[1][1] + self.board[2][0] == 15 and (not self.board[0][2] == 0 and not self.board[1][1] == 0 and not self.board[2][0] == 0):
            return True
        else:
            return False
        

            

if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required
    
    # start by creating empty board and checking the contents of the board attribute
    myBoard = NumTicTacToe()
    print('Contents of board attribute when object first created:')
    print(myBoard.board)
    
    # does the empty board display properly?
    myBoard.drawBoard()

    # assign a number to an empty square and display
    myBoard.update(0,0,5)
    myBoard.drawBoard()
    
    # try to assign a number to a non-empty square. What happens?
    myBoard.update(0,0,9)
    myBoard.drawBoard()
    print(' | not updated since square not empty')
    
    # check if the board has a winner. Should there be a winner after only 1 entry?
    print(myBoard.isWinner(), " | true if winner false if no winner")


    # check if the board is full. Should it be full after only 1 entry?
    print(myBoard.boardFull(), ' | true if board is full false if not full')


    # add values to the board so that any line adds up to 15. Display
    myBoard.update(0,1,1)
    myBoard.update(0,2,9)
    myBoard.drawBoard()
    
    # check if the board has a winner
    print(myBoard.isWinner(), " | true if winner false if no winner")


    # check if the board is full
    print(myBoard.boardFull(), ' | true if board is full false if not full')

    
    # write additional tests, as needed

    print('a test for full board and diagonal winning')
    for i in range(len(myBoard.board)):
        for j in range(len(myBoard.board[i])):
            if i == j:
                myBoard.board[i][j] = 5
            else:
                myBoard.board[i][j] = 4
    myBoard.drawBoard()
    print(myBoard.isWinner(), " | true if winner false if no winner")
    print(myBoard.boardFull(), ' | true if board is full false if not full')


    print(myBoard.update(-5,5,1))
        
    input() # just makes it so program doesn't close after running