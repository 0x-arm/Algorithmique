# Constructeur de Node
class Node:

	def __init__(self, initdata): # création du Node
		self.data = initdata # initialiser la donnée du node
		self.next = None # définir le next à None car c'est le seul élément de la liste

	### Getters
	def getData(self): # Récupérer la donnée du Node
		return self.data

	def getNext(self): # Récupérer l'index du Node suivant du Node actuel
		return self.next

	# Setters
	def setData(self, newdata): # Assigner une nouvelle valeur à la donnée actuelle
		self.data = newdata

	def setNext(self, newnext): # Assigner un nouveau Node suivant à pointer
		self.next = newnext


class UnorderedList:

	def __init__(self): # Création d'une liste vide
		self.head = None
		self.count = 0

	def isEmpty(self): # Si la liste est vide
		return self.head == None

	def lenght(self):
		return self.count

	def add(self, item): # Ajout d'un Node au début de la liste
		temp = Node(item) # création du Node temp avec comme donnée item
		temp.setNext(self.head) # attribuation d'un pointeur next vers le premier élément de la liste (ici cela pointe vers None, donc c'est le premier et seul élément de la liste)
		self.head = temp # le premier élément de la liste est le Node temp
		self.count += 1

	def addAfter(self, base, item): # Ajout d'un Node à la suite d'un Node base déjà existant dans la liste
		temp = Node(item) # création du NOde temp
		temp.setNext(base.getNext()) # Attribution d'un pointeur next vers le pointeur d'origine du Node Base (temp pointe vers le pointeur de base pour qu'il se trouve avant ce next et après le Node base)
		base.setNext(temp) # Attribution de temp en tant que Node suivant à pointer au Node base
		self.count += 1

	def search(self, item): # Trouver la valeur dans un Node d'une liste
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, base):
		previous = None
		current = self.head
		found = False
		while current != None and not found:
			if current is base:
				found = True
			else:
				previous = current
				current = current.getNext()
		if found:
			if previous != None:
				previous.setNext(base.getNext())
			else:
				self.head = base.getNext()
