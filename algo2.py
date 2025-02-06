from algo1 import Node, UnorderedList

L = UnorderedList()
L.add(5)
L.add(4)
L.add(3)
print(L.lenght())

M = L
M.add(2)
print(L.lenght())

print( M is L)

def ajout(liste):
	liste.add(1)

ajout(M)
print(M.lenght())

print(L.search(1))


# COPY
import copy
N = copy.copy(M)
O = copy.deepcopy(M)

print( N is M)
print(O is M)

noeud = N.head
noeud = noeud.getNext()
print(noeud.getData())

L.addAfter(noeud, 7)
print(L.lenght())
print(M.lenght())
print(N.lenght())
print(O.lenght())


# Liste bidirectionnelle
class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None
		self.previous = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getPrevious(self):
		return self.previous

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

	def setPrevious(self, newprevious):
		self.previous = newprevious

class UnorderedList:
	def __init__(self):
		self.head = None
		self.count = 0

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)

		if self.head != None:
			self.head.setPrevious(temp)

		self.head = temp
		self.count += 1

	def addAfter(self, base, item):
		temp = Node(item)
		temp.setPrevious(base)
		temp.setNext(base.getNext())

		if base.getNext() != None:
			base.getNext().setPrevious(temp)

		base.setNext(temp)
		self.count += 1

	def length(self):
		return self.count

	def search(self, item):
		current = self.head
		found = False

		while current != None and not found:
			if current.getData() == item:
				found = True

			else:
				current = current.getNext()
		return found

	def remove(self, base):
		previous = base.getPrevious()

		if base.getNext() != None:
			base.getNext().setPrevious(previous)
		if preivous != None:
			preivous.setNext(base.getNext())
		else:
			self.head = base.getNext()

		self.count += 1


# Liste circulaire
class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

class UnorderedList:
	def __init__(self):
		self.head = Node(-1)
		self.head.setNext(self.head)
		self.count = 0

	def isEmpty(self):
		return self.head.getNext() == self.head

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head.getNext())
		self.head.setNext(temp)
		self.count += 1

	def addAfter(self, base, item):
		temp = Node(item)
		temp.setNext(base.getNext())
		base.setNext(temp)
		self.count += 1

	def length(self):
		return self.count

	def search(self, item):
		current = self.head.getNext()
		found = False

		while current != self.head and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self, base):
		previous = self.head
		current = self.head.getNext()
		found = False

		while current != self.head and not found:
			if current is base:
				found = True
			else:
				previous = current
				current = current.getNext()

		if found:
			preivous.setNext(base.getNext())
			self.count += 1


# Pile 1
class Stack1:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item) # .insert(0, item)

	def pop(self):
		return self.items.pop() # .pop(0)

	def top(self):
		return self.items[len(self.items)-1] # [0]

	def size(self):
		return len(self.items)


# Pile 2
class Stack2:
	def __init__(self):
		self.head = None
		self.n = 0

	def isEmpty(self):
		return self.head == Node

	def top(self):
		return self.head.getData()

	def size(self):
		return self.n

	def push(self, item):
		p = Node(item)
		p.setNext(self.head)
		self.head = p
		self.n += 1

	def pop(self):
		res = self.head.getData()
		self.head = self.head.getNext()
		self.n -= 1
		return res
