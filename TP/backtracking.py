ensemble = [1, 2, 3]

#6.1
def sous_ensemble(ensemble: list, choix=None, indice=0):
	n = len(ensemble)

	if choix is None:
		choix = [False]*n

	if indice == n:
		print(ensemble)

	else:
		choix[indice] = True
		sous_ensemble(ensemble, choix, indice+1)
		choix[indice] = False
		sous_ensemble(ensemble, choix, indice+1)

#print(sous_ensemble(ensemble))

#6.3

