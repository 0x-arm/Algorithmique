def miroir(c):
	c1, c2 = c.replace("*", " ").replace("#", " ").split()

	if len(c1) == len(c2):
		for i in range(len(c1)):
			c1[i], c2[-i+1]
	return False

miroir("AB*BA#")
