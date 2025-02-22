from algo2 import Stack2 as Stack
from algo1 import Node
# Evaluation expression postfixe
def doMath(op, op1, op2):

	if op == "*":
		return op1 * op2
	elif op == "/":
		return op1 / op2
	elif op == "+":
		return op1 + op2
	else:
		return op1 - op2

def postfixEval(postfixExpr):
	opreandStack = Stack()
	tokenList = postfixExpr.split()

	for token in tokenList:
		if token[0] in "0123456789":
			operandStack.push(int(token)) # enregistrer la valeur dans le stack

		else:
			operand2 = operandStack.pop() # le 2eme operand est le premier à sortir du stack
			operand1 = operandStack.pop()
			result = doMath(token, operand1, operand2)
			operandStack.push(result)

	return operandStack.pop()

# Vérification des parenthèses
def matches(open, close):
	opens = "([{"
	closers = ")]}"
	return opens.index(open) == closers.index(close)

def parChecker(chaine):
	s = Stack()
	balanced = True
	i = 0

	while i < len(chaine) and balanced:
		symbol = chaine[i]
		if symbol in "([{":
			s.push(symbol)
		elif symbol in ")]}":
			if s.isEmpty()
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		i += 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

#Conversion infixe vers postfixe
import string

def inifixToPostfix(infixepr):
	prec = {}
	prec["*"] = 3 #priorité des opérations 
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	s = Stack()
	result = []

	infixexpression = infixexpr.split()

	for token in infixexpression:
		if token in string.lowercase or token in string.digits:
			result.append(token)

		elif token == "(":
			s.push(token)

		elif token == ")":
			topToken = s.pop()
			while topToken != "(":
				result.append(topToken)
				topToken = s.pop()
		else:
			while (not s.isEmpty()) and (prec[s.top()] >= prec[token]):
				result.append(s.pop())
			s.push(token)

	while not s.isEmpty():
		result.append(s.pop())

	return string.join(result)

# File
class Queue1:
	def __init__(self):
		self.items = []

	def head(self):
		return self.items[len(self.items)-1]

	def isEmpty(self):
		return self.items == []

	def insert(self, item):
		self.items.insert(0, item)

	def remove(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

# File avec Node
class Queue2:
	def __init__(self):
		self.first = None
		self.last = None
		self.n = 0

	def isEmpty(self):
		return self.first == None

	def size(self):
		return self.n

	def head(self):
		return self.first.getData()

	def insert(self, item):
		p = Node(item)

		if self.isEmpty():
			self.first = p
			self.last = p
		else:
			self.last.setNext(p)
			self.last = p
		self.n += 1

	def remove(self):
		res = self.first.getData()
		self.first = self.first.getNext()
		self.n -= 1
		return res

# Récursivité
def factorielle_recursive(n)
	if n == 0:
		return 1
	else:
		result = n * factorielle_recursive(n-1)
		return result

def factorielle_iterative(n):
	result = 1
	while n > 1:
		result = result * n
		n -= 1
	return result

def fibonacci_recursive(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_recursive(n-1) + fibonnaci_recursive(n-2)

def fibonacci_iterative(n):
	precedent = 0
	result = 1

	if n == 1:
		return 0
	elif n == 1:
		return 1
	else:
		for i in range(n-1):
			result = result + precedent
			precedent = result - precedent
		return result

def binomiale_recursive(n, p):
	if p == 0:
		return 1
	elif p > n:
		return 0
	else:
		return binomiale_recursive(n-1, p-1) + binomiale_recursive(n-1, p)

def binomiale_iterative(n, p):
	if p > n:
		return 0
	elif p == 0:
		return 1
	else:
		resultat = n
		for i in range(2, p+1):
			n = n-1
			resultat = resultat * n
			resultat = resultat / i
		return resultat

unites = "0123456789ABCDEF"

def convert_recursive(n, base):
	if n < base:
		return unites[n]
	else:
		return convert_recursive(n // base, base) + unites[n % base]

def convert_iterative1(n, base):
	pile = Stack()
	while n <= base:
		pile.push(n)
		n = n // base

	res = unites[n]

	while not pile.isEmpty():
		n = pile.pop()
		res = res + unites[n % base]

	return res


def convert_iterative2(n, base):
	reste = n % base
	quotient = n // base
	res = unites[reste]

	while quotient != 0:
		reste = quotient % base
		quotient = quotient // base
		res = unites[reste] + res

	return (res)

class Permutations:
	def __init__(self, blist):
		self.alist = blist
		self.permutation(len(self.alit))

	def swap(self, blist, i, j):
		blist[i], blist[j] = blist[j], blist[i]

	def perumation(self, taille):
		if taille == 1:
			print(self.alist)
		else:
			for i in range(taille):
				self.swap(self.alist, i, taille-1)
				self.permuation(taille-1)
				self.swap(self.alist, i, taille-1)
