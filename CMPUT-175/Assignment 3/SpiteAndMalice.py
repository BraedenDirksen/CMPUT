#----------------------------------------------------
# Assignemnt #3
# 
# Author: Braeden Dirksen
# Collaborators:
# References: stack.py from lab 5
#----------------------------------------------------

class Card:
    def __init__(self,value,face):
        values = [-1,0,1,2,3,4,5,6,7,8,9]
        assert value in values, 'value is invalid'
        self.value = value
        self.face = face
    
    def assign(self,value):
        assert face == '*', 'invalid card type for assignment'
        self.value = value

    def getValue(self):
        return self.value

    def __str__(self):
        return '[' + self.face + ']'
    
    def __repr__(self):
        pass

class PlayStack:
    def __init__(self,size):
        self.cards = []
        self.size = size

    def push(self, item):
        assert self.size() >= self.size, 'stack is full'
        self.cards.append(item)

    def pop(self):
        assert self.isEmpty(), 'stack is already empty'
        return self.cards.pop()

    def peekValue(self):
        assert self.isEmpty(), "stack has no items"
        return self.cards[-1].getValue()

    def peekFace(self):
        assert self.isEmpty(), "stack has no items"
        return str(self.cards[-1])

    def isEmpty(self):
        return self.cards == []
    
    def size(self):
        return len(self.cards)

    def show(self):
        print(self.items)

    def playCard(self,card):
        error = True
        faceList = []
        if isinstance(card, Card) and card.getValue() == self.peekValue() + 1:
            if card.getValue() == 0:
                if self.isEmpty():
                    error = False
                    self.push(card)
            elif card.getValue() == 9:
                error = False
                for i in range(self.size):
                    faceList.append(str(self.cards.pop()))
            else:
                error = False
                self.push(card)
        if error:
            raise Exception('Error: Card rejected')
        return '|', str(faceList), '|'

    def __str__(self):
        self.cards.sort()
        string = '|'
        for i in range(len(self.cards)):
            string += str(self.cards[i])
        string += '|'
        print(str)

class Hand:
    def __init__(self):
        self.__hand = []
        self.maxSize = 5
        self.size = 0
    def sort(self):
        for i in range(1,len(self.__hand)):
            if self.__hand[i].getValue() < self.__hand[i-1].getValue():
                for j in range(i):
                    if self.__hand[i].getValue() < self.__hand[j].getValue():
                        self.__hand[i].assign(self.__hand[j].getValue()), self.__hand[j].assign(self.__hand[i].getValue())
    def pop(self,i = -1):
        return self.__hand.pop(i)
    def index(self,v):
        if not v in [-1,0,1,2,3,4,5,6,7,8,9]:
            raise Exception('invalid value')
        for i in range(len(self.__hand)):
            if self.__hand[i].getValue() == v:
                return i
        return -1
    def check0(self):
        for i in range(len(self.__hand)):
            if self.__hand[i].getValue() == 0:
                return i
        return -1

    def size(self):
        return self.size
        
    def add(self,cardList):
        if len(self.__hand) == self.maxSize:
            raise Exception('hand is already full')
        else:
            for item in cardList:
                self.__hand.append(item)
    def convString(self):
        pass