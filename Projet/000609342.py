from copy import deepcopy

########## GAME ##########
def play(board: list[list[int]], player: int, cell: int) -> int:
    """modifie le tableau en suivant les règles du jeu et retourne le nombre de graines récoltées par le joueur à ce tour"""

    recovered = 0 # Nombre de graines récupérées (0 par défaut)
    next_cell, next_plate = cell, player # Initialisation des variables pour la distribution
    seeds = board[player][cell] # Nombre de graines à distribuer
    board[player][cell] = 0 # Vider la case

    # Distribution des graines
    while seeds > 0: # Tant qu'il reste des graines à distribuer
        next_cell += 1 # Avancer d'une case

        if next_cell >= len(board[player]): # Si on dépasse la dernière case
            next_cell = 0 # Retour à la première case
            next_plate = 1 - next_plate # Changement de plateau

        board[next_plate][next_cell] += 1 # Distribution d'une graine
        seeds -= 1 # Décrémenter le nombre de graines restantes

    # Récupération de graines si possible
    if next_plate != player:
        while next_cell >= 0 and board[next_plate][next_cell] in (2, 3): # Tant qu'on peut récupérer des graines
            recovered += board[next_plate][next_cell] # Récupérer les graines
            board[next_plate][next_cell] = 0 # Vider la case
            next_cell -= 1 # Reculer d'une case
            
    # Vérification si coup interdit
    if is_end(board, 1-player): # Si l'adversaire n'a plus de graines
        return -1 # Valeur de coup interdit

    return recovered

def is_end(board: list[list[int]], player: int) -> bool:
    return all(x == 0 for x in board[player]) # Vérifier si le plateau du joueur est vide

########## IA MinMax ##########
def enum(board, player: int, depth: int) -> list[tuple[list[int], int]]:
    """énumère toutes les suites de coups possibles à l'aide du backtracking et retourne une liste de tuples associant une suite de mouvements et le score final pour une profondeur donnée"""

    # Cas de base : profondeur nulle ou fin de jeu
    if depth == 0 or is_end(board, player):
        return [([], 0)]
    
    results = [] # Liste des résultats
    
    # Tester chaque coup possible
    for move in range(6):

        if board[player][move] > 0: # Ignorer les coups nuls
            board_copy = deepcopy(board) # Copie du plateau pour simuler le coup
            score = play(board_copy, player, move) # Jouer le coup

            if score != -1: # Ignorer les coups interdits
                opponent_results = enum(board_copy, 1-player, depth-1) # Enumération des coups suivants possibles pour l'adversaire

                for opponent_moves, opponent_score in opponent_results: # Ajouter les résultats des coups suivants
                    results.append(([move] + opponent_moves, opponent_score + (score if player == 0 else -score))) # Ajouter le coup et le score

    return results

def minmax(board: list[list[int]], player: int, depth: int) -> int:
    """explore l'ensemble des suites de coups possibles en partant du tour d'un des deux joueurs et sélectionne la meilleure sur base de son score"""

    # Cas de base : profondeur nulle ou fin de jeu
    if depth == 0 or is_end(board, player):
        return 0
    
    best_value = None # Meilleure valeur (non connue)

    # Tester chaque coup possible
    for move in range(6):

        if board[player][move] > 0: # Ignorer les coups nuls
            board_copy = deepcopy(board) # Copie du plateau pour simuler le coup
            score = play(board_copy, player, move) # Jouer le coup

            if score != -1: # Ignorer les coups interdits
                value = score - minmax(board_copy, 1-player, depth-1) # Calculer la valeur du coup

                if best_value is None or value > best_value: # Mettre à jour la meilleure valeur si la valeur trouvée est meilleure
                    best_value = value # Mise à jour de la meilleure valeur

    if best_value is None: # Si aucune valeur n'a été trouvée
        best_value = 0 # Meilleure valeur nulle

    return best_value
    
def suggest(board: list[list[int]], player: int, depth: int) -> int:
    """ détermine quel coup rapportera le plus de graines à court terme sur un plateau donné pour un joueur donné et une profondeur donnée"""

    best_move = -1 # Meilleur coup (-1 par défaut, la case la plus proche du plateau adverse)
    best_value = None # Meilleure valeur (non connue)

    # Tester chaque coup possible
    for move in range(6):

        if board[player][move] > 0: # Ignorer les coups nuls
            board_copy = deepcopy(board) # Copie du plateau pour simuler le coup
            score = play(board_copy, player, move) # Jouer le coup

            if score != -1: # Ignorer les coups interdits
                value = score - minmax(board_copy, 1-player, depth-1) # Calculer la valeur du coup
                
                if best_value is None or value > best_value: # Mettre à jour la meilleure valeur si la valeur trouvée est meilleure
                    best_value = value # Mise à jour de la meilleure valeur
                    best_move = move # Mise à jour du meilleur coup associé à la meilleure valeur

    return best_move