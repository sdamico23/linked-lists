#Lab #9
#Due Date: 03/01/2019, 11:59PM
########################################
#                                      
# Name: Steve D'Amico
# Collaboration Statement:  I worked alone.            
#  
########################################


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    def getVal(self):
        return self.value
    def getNext(self):
        return self.next
    def setValue(self, newVal):
        self.value = newVal
    def setNext(self,newNext):
        self.next = newNext
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        

                          
class OrderedLinkedList:
    '''
        >>> x=OrderedLinkedList()
        >>> x.pop()
        'List is empty'
        >>> x.add(-6)
        >>> x.add(8)
        >>> x.add(3)
        >>> x.add(7)
        >>> print(x)
        Head:Node(8)
        Tail:Node(-6)
        List:8 7 3 -6
        >>> len(x)
        4
        >>> x.pop()
        -6
        >>> print(x)
        Head:Node(8)
        Tail:Node(3)
        List:8 7 3
    '''
    def __init__(self):
    	#You can add a count attribute for len
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def add(self, value):
        #write your code here
        add_node=Node(value)
        current = self.head
        if self.head is None: 
            self.head = add_node
            self.tail=add_node
            self.count +=1
            return
        elif self.head.getVal() <= add_node.getVal():
            add_node.setNext(self.head)
            self.head=add_node
        else: 
            current=self.head
            while (current.getNext() is not None and current.getNext().getVal() >add_node.getVal()):
                current = current.getNext()
            add_node.setNext(current.getNext())
            current.setNext(add_node)
        self.count += 1
        temp = self.head
        while (temp.getNext() is not None): 
            temp = temp.getNext()
        self.tail = temp
    def pop(self):
        #write your code here

        if self.isEmpty():
            return 'List is empty'
        if self.head== self.tail:
            val = self.head.getVal()
            self.head =None
            self.tail = None
            return val
        prev = self.head
        while prev.getNext() is not self.tail: 
            prev = prev.getNext()
        val = self.tail.getVal()
        self.tail = prev
        self.tail.setNext(None)
        self.count -=1
        return val

    def isEmpty(self):
        #write your code here
        return self.head ==None


    def __len__(self):
        return self.count

x=OrderedLinkedList()
x.pop()
x.add(-6)
x.add(8)
x.add(3)
x.add(7)
print(x)
print(x.pop())        #write your code here




