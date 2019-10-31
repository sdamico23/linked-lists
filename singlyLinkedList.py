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

class SinglyLinkedList:
	def __init__(self, head=None):
		self.head = head
		self.tail = None



	def add(self,value):
		newNode = Node(value)
		newNode.setNext(self.head)
		self.head = newNode
	def size(self):
		current = self.head
		count =0
		while current:
			count += 1
			current = current.getNext()
		return count
	def delete(self, value):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.getVal() == value:
				found = True
			else: 
				previous = current
				current = current.getVal()
		if current is None:
			raise ValueError("Value not in list")
		if previous is None:
			self.head = current.getNext()
		else: 
			previous.setNext(current.GetVal())

	def isEmpty(self):

		return self.head ==None

	def pop(self):

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

x=SinglyLinkedList()
x.pop()
x.add(-6)
x.add(8)
x.add(3)
x.add(7)
print(x)
print(x.pop())
