class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
            
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous
    
    def setNext(self,newNext):
        self.next = newNext
        
    def setPrevious(self,newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0        
           
    def search(self, item):
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        # TODO:
        new_node = DLinkedListNode(item,self.__head,None)
        if self.__head != None:
            self.__head.setPrevious(new_node)
        if self.__tail == None:
            self.__tail = new_node
        self.__head = new_node
        self.__size += 1

    def remove(self, item): 
        # TODO:
        if self.search(item):
            index = self.index(item)
            '''
            current = self.__head
            for _ in range(index):
                current = current.getNext()
            if current.getPrevious() == None:
                self.__head = current.getNext()
                self.__size -= 1
            elif current.getNext() == None:
                self.__tail = current.getPrevious()
                self.__tail.setNext(None)
                self.__size -= 1
            else:
                self.pop(index)
            '''
            self.pop(index)

    def append(self, item):
         # TODO: 
        new_node = DLinkedListNode(item,None,self.__tail)
        if self.__size >= 1:
            self.__tail.setNext(new_node)
        if self.__size == 0:
            self.__head = new_node
        self.__tail = new_node
        self.__size += 1
        
    def insert(self, pos, item):
        # TODO:
        assert type(pos) == int, 'pos is not int'
        assert pos >= 0, "pos is less then 0"

        current = self.__head
        for _ in range(pos):
            current = current.getNext()
        
        if current.getNext() == None:
            self.append(item)
        elif current.getPrevious() == None:
            self.add(item)
        else:
            new_node = DLinkedListNode(item,current.getNext(),current.getPrevious())
            current.getPrevious().setNext(new_node)
            current.getNext().setPrevious(new_node)
            self.__size += 1
        
    def pop1(self):
        # TODO:
        removed = self.__tail
        if self.__size > 0:
            self.__tail = self.__tail.getPrevious()
            if self.__size == 1:
                self.__head == None
            elif self.__size > 1:
                self.__tail.setNext(None)   
            self.__size -= 1
            return removed.getData()
    
    def pop(self, pos=None):
        # TODO:
        # Hint - incorporate pop1 when no pos argument is given
        if pos == None:
            return self.pop1()
        else:
            assert pos >= 0 and pos <= self.__size
            current = self.__head
            for _ in range(pos):
                current = current.getNext()
            if current.getNext() == None:
                self.pop1()
            elif current.getPrevious() == None:
                current.getNext().setPrevious(None)
                self.__head = current.getNext()
                self.__size -= 1
            else:
                current.getPrevious().setNext(current.getNext())
                current.getNext().setPrevious(current.getPrevious())
                self.__size -= 1
            return current.getData()

    def searchLarger(self, item):
        # TODO:
        current = self.__head
        cont = True
        i = 0
        while i <= self.__size and cont:
            if current.getData() > item:
                cont = False
            else:
                current = current.getNext()
                i += 1
        if current != None:
            return i
        else:
            return -1

    def getSize(self):
        # TODO:    
        return self.__size

    def getItem(self, pos):
        # TODO: 
        assert pos <= self.__size, "pos not in list"
        if pos < 0:
            pos = self.__size + pos - 1
        current = self.__head
        for _ in range(pos):
            current = current.getNext()
        return current.getData()
        
    def __str__(self):
        # TODO: 
        current = self.__head.getNext()
        string = str(self.__head.getData())
        while current != None:
            string += ' '
            string += str(current.getData())
            current = current.getNext()
        return string
            
def test():
                  
    linked_list = DLinkedList()
                    
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"
        
        
    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.getItem(0) == "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test" 
                    
    int_list2 = DLinkedList()
                    
    for i in range(0, 10):
        int_list2.add(i)            

    int_list2.remove(1)      
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
     

    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
           
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
      
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
    
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"    
                    
    int_list = DLinkedList()
                    
    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"                   
                    
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"            
            
    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
    
    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)   
        
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
            
            
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")

                
if __name__ == '__main__':
    test()
