#----------------------------------------------------
# Assignemnt #2
# 
# Author: Braeden Dirksen
# Collaborators:
# References: Lab 3 NumTicTacToe
#----------------------------------------------------
class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        ''' 
        self.winner = None
        self.board = []
        self.size = 3
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
        try:
            if self.board[row][col] == 0:
                return True
            else:
                return False
        except IndexError:
            return False
    def update(self, row, col, mark):
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
            self.board[row][col] = mark
            return True
        else:
            return False

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
        
    def isNum(self):
        return True

class ClassicTicTacToe:
    def __init__(self):
        '''
        Initializes an empty classic Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''     
        self.winner = None
        self.board = []
        self.size = 3
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
        try:
            if self.board[row][col] == 0:
                return True
            else:
                return False
        except IndexError:
            return False
    def update(self, row, col, mark):
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
            self.board[row][col] = mark
            return True
        else:
            return False

    def isWinner(self):
        for row in self.board:
            c = [[],[],[]]
            x = 0
            o = 0
            for item in row:
                if item == 'X':
                    x+=1
                elif item == 'O':
                    o+=1
            if x == 3 or o == 3:
                return True
                

            c[0].append(row[0])
            c[1].append(row[1])
            c[2].append(row[2])

        for row in c:
            x = 0
            o = 0
            for item in row:
                if item == 'X':
                    x+=1
                elif item == 'O':
                    o+=1
            if x == 3 or o == 3:
                return True
            
        
        d1 = [self.board[0][0],self.board[1][1],self.board[2][2]]
        d2 = [self.board[0][2],self.board[1][1],self.board[2][0]]

        if d1[0] == d1[1] and d1[1] == d1[2]:
            x = 0
            o = 0
            for item in d1:
                if item == 'X':
                    x+=1
                elif item == 'O':
                    o+=1
            if x == 3 or o == 3:
                return True
        if d2[0] == d2[1] and d2[1] == d2[2]:
            x = 0
            o = 0
            for item in d2:
                if item == 'X':
                    x+=1
                elif item == 'O':
                    o+=1
            if x == 3 or o == 3:
                return True

        return False
            
                    
    def boardFull(self):
        full = True
        for row in self.board:
            for item in row:
                if item == 0:
                    full = False
        return full
    def isNum(self):
        return False

class MetaTicTacToe:
    def __init__(self, configFile):
        self.board = []
        self.size = 3
        self.config = open(configFile,'r').read()
        self.config = self.config.split('\n')
        for i in range(len(self.config)):
            self.config[i] = self.config[i].split(' ')
        
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if self.config[i][j] == 'c':
                    row.append(ClassicTicTacToe())
                else:
                    row.append(NumTicTacToe())
            self.board.append(row)
        
    def drawBoard(self):
        displayList = []
        for row in self.board:
            for item in row:
                if item == 'X' or item == 'O' or item == 'D':
                    displayList.append(item)
                elif item.isNum():
                    displayList.append('N')
                else:
                    displayList.append('C')
        
        print('    0   1   2 ')
        print(' 0  '+ displayList[0] +' | '+ displayList[1] +' | '+ displayList[2] +' ')
        print('   -----------')
        print(' 1  '+ displayList[3] +' | '+ displayList[4] +' | '+ displayList[5] +' ')
        print('   -----------')
        print(' 2  '+ displayList[6] +' | '+ displayList[7] +' | '+ displayList[8] +' ')
        
    def squareIsEmpty(self, row, col):
        if self.board[row][col] != 'X' and self.board[row][col] != 'O' and self.board[row][col] != 'D':
            return False
        else:
            return True
    def update(self, row, col, mark):
        if not self.squareIsEmpty(row,col):
            self.board[row][col] = mark
            return True
        else:
            return False

    def isWinner(self):
        for row in self.board:
            c = [[],[],[]]
            x = 0
            o = 0
            for item in row:
                if item == 'X':
                    x+=1
                elif item == 'O':
                    o+=1
            if x == 3 or o == 3:
                return True
                

            c[0].append(row[0])
            c[1].append(row[1])
            c[2].append(row[2])

        for row in c:
            x = 0
            o = 0
            for item in row:
                if item == 'X':
                    x+=1
                elif item == 'O':
                    o+=1
            if x == 3 or o == 3:
                return True
            
        
        d1 = [self.board[0][0],self.board[1][1],self.board[2][2]]
        d2 = [self.board[0][2],self.board[1][1],self.board[2][0]]

        if d1[0] == d1[1] and d1[1] == d1[2]:
            x = 0
            o = 0
            for item in d1:
                if item == 'X':
                    x+=1
                elif item == 'O':
                    o+=1
            if x == 3 or o == 3:
                return True
        if d2[0] == d2[1] and d2[1] == d2[2]:
            x = 0
            o = 0
            for item in d2:
                if item == 'X':
                    x+=1
                elif item == 'O':
                    o+=1
            if x == 3 or o == 3:
                return True

        return False

    def boardFull(self):

        for row in self.board:
            for item in row:
                if item != 'X' and item != 'O' and item != 'D':
                    return False
        return True

    def getLocalBoard(self, row, col):
        if self.board[row][col] != 'X' and self.board[row][col] != 'O' and self.board[row][col] != 'D':
            return self.board[row][col]
        else:
            return None


if __name__ == "__main__":
    numTTT = NumTicTacToe()

    #-- tests for classicTicTacToe --#

    classicTTT = ClassicTicTacToe()
    classicTTT.drawBoard()
    print('is there winner?',classicTTT.isWinner())
    print('1,1 empty?',classicTTT.squareIsEmpty(1,1))
    print('full board?',classicTTT.boardFull())
    classicTTT.update(1,1,"X")
    print('1,1 empty?',classicTTT.squareIsEmpty(1,1))
    classicTTT.drawBoard()
    print('is there winner?',classicTTT.isWinner())
    classicTTT.update(0,1,"X")
    classicTTT.update(2,0,"X")
    classicTTT.drawBoard()
    print('is there winner?',classicTTT.isWinner())

    #-- tests for MetaTicTacToe --#
    print('--------------------------------------------------------')

    metaTTT = MetaTicTacToe('MetaTTTconfig.txt')
    print('is there winner?',metaTTT.isWinner())
    metaTTT.drawBoard()
    metaTTT.update(0,0,"X")
    metaTTT.update(1,1,"X")
    metaTTT.update(2,2,"X")
    print('is there winner?',metaTTT.isWinner())
    metaTTT.drawBoard()
    print(metaTTT.getLocalBoard(1,1),'1,1')
    print(metaTTT.getLocalBoard(1,0),'1,0')

