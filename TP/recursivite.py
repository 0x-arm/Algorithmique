#5.1
def invert_input(n):
	if n != 0:
		v = int(input())
		ret = invert_input(n-1)
		print(v)

#invert_input(8)

#5.2
def pair_impair(n):

	if n != 0:
		v = int(input())

		if v % 2 == 0:
			print(v, "pair")
			pair_impair(n-1)
		else:
			pair_impair(n-1)
			print(v, "impair")

#pair_impair(8)

#5.3
