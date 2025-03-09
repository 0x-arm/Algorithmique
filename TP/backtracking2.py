def distincts(v: list, i=0, j=1, k=2):

	if v[i] + v[j] + v[k] == 0:
		return True

	else:
		if k+1 < len(v) and j+1 < len(v) and i+1 < len(v):
			distincts(v, i, j, k+1)
			distincts(v, i, j+1, k)
			distincts(v, i+1, j, k)



v = [1, 2, 3, 4, -3, 8]
print(distincts(v))
