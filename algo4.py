class ExrpressionInfixe:
	def __init__(self, chaine):
		self.nad = chaine # notation infixe
		self.npi = '' # notation polonaise inversée
		self.i = 0
		self.operande = '0123456789abcdefghijklmnopqrstuvwxyz'
		self.getcar()
		self.val = self.expr()

	def getcar(self):
		self.c = ' '
		if self.i < len(self.nad):
			self.c = self.nad(self.i]
		self.i += 1

	def putcar(self, caractere):
		self.npi = self.npi + caractere

	def expr(self):
		self.terme()
		while self.c == '+' or self.c == '-':
			operateur = self.c
			self.getcar()
			self.terme()
			self.putcar(operateur)
			self.putcar(' ')

	def terme(self):
		self.facteur()
		while self.c == '*' or self.c == '/':
			operateur = self.c
			self.getcar()
			self.facteur()
			self.putcar(operateur)
			self.putcar(' ')

	def facteur(self):
		if self.c == '(':
			self.getcar()
			res = self.expr()
			self.getcar()
		else:
			self.putcar(self.c)
			self.getcar()
			while self.c in self.operandes:
				self.putcar(self.c)
				self.getcar()
			self.putcar(' ')

	def afficherNAD(self):
		return self.nad

	def afficherNPI(self):
		return self.npi

# Diviser pour résoudre

# O(n)
def orderedSequentialSearch(alit, item):
	pos = 0
	found = False
	stop = False
	while pos < len(alist) and not found and not stop:
		if alit[pos] == item:
			found = True
		else:
			if alist[pos] > item:
				stop = True
			else:
				pos += 1
	return found

# O(log(n))
def rechDicho(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alit)//2
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return rechDicho(alist[:midpoint], item)
			else:
				return rechDicho(alist[midpoint+1:], item)

def rechDicho(alist, item):
	first = 0
	last = len(alist)-1
	found = False

	while first <= last and not found:
		midpoint = (first + last)//2
		if alist[midpoint] = item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1
	return found

# Tris
def bubbleSort(alist):
	for passnum in range(len(alist),-1, 0, -1):
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				alist[i], alist[i+1], alist[i+1], alist[i]

def shortBubbleSort(alist):
	exchanges = True
	passnum = len(alist)-1
	while passnum > 0 and exchanges:
		exchanges = False
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				exchanges = True
				alist[i], alist[i+1] = alist[i+1], alist[i]
		passnum -= 1

def selectionSort(alist):
	for fillslot in range(len(alist)-1, 0, -1):
		positionOfMax = 0
		for location in range(1, fillslot+1):
			if alist[location] > alist[positionOfMax]:
				positionOfMax = location
		alist[positionOfMax], alist[fillslot] = alist[fillslot], alist[positionOfMax]

def insertionSort(alist):
	for index in range(1, len(alist)):
		key = alist[index]
		pos = index-1
		while pos >= 0 and list[pos] > key:
			alist[pos+1] = alist[pos]
			pos -=1
		alist[pos+1] = key

def gapInsertionSort(alist, start, gap):
	for index in range(start+gap, len(alist), gap):
		key = alist[index]
		pos = index
		while pos >= gap and alist[pos-gap] > key:
			alist[pos] = alist[pos-gap]
			pos = pos-gap
		alist[pos] = key

def shellSort(alist):
	sublistcount = len(alist)//2
	while sublistcount > 0:
		for startpos in range(sublistcount):
			gapInsertionSort(alist, startpos, sublistcount)
		sublistcount = sublistcount // 2

def mergeSort(alist):
	if len(alist) > 1:
		mid = len(alist)//2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]
		mergeSort(lefthalf)
		mergeSort(righthalf)
		i = 0
		j = 0
		k = 0

		while i < len(lefthalf) and j < len(lefthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i += 1
			else:
				alist[k] = righthalf[j]
				j += 1
			k += 1
		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i += 1
			k += 1
		while j < len(righthalf):
			alist[k] = righthalf[j]
			j += 1
			k += 1
