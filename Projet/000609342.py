# Plateau initial
board = [[1, 7, 2, 7, 2, 0], # joueur 1 (a, b, c, d, e, f)
	[0, 3, 4, 2, 2, 5]] #  joueur 2 (g, h, i, j, k, l)

class Game:

	def __init__(self, board=None):
		self.board = board
		if self.board is None:
			self.board = self.init_board()

	def init_board(self) -> list[list]:
		return [[4]*6, [4]*6]

	def play(self, board: list[list], player: int, cell: int) -> int:
		next_cell = cell
		next_plate = player
		opponent = 1 if player == 0 else 0
		seeds_removed = 0

		while board[player][cell] > 0:
			next_cell += 1
			if next_cell >= len(board[player]):
				next_cell = 0
				next_plate = 1 if next_plate == 0 else 0

			board[next_plate][next_cell] += 1
			board[player][cell] -= 1

		if board[opponent].count(0) == len(board[opponent]):
			raise ValueError("Interdiction d'affamé l'adversaire ! Coup Interdit")

		while board[next_plate][next_cell] in (2, 3):
			seeds_removed += board[next_plate][next_cell]
			board[next_plate][next_cell] = 0
			next_cell -= 1

		return seeds_removed

	def is_end(self, board: list[list], player: int) -> bool:
		return True if board[player].count(0) == len(board[player]) else False

game = Game(board)
board = game.board
#print(game.play(board, 0, 3))
#print(game.is_end(board, 0))

# Algorithme MinMax
class MinMax:

	def __init__(self, game: Game, depth: int) -> None:
		self.game = game
		self.depth = depth
		self.board = game.board

	def isEmpty(self, player: int, cell: int) -> bool:
		return self.board[player][cell] == 0

	def final_score(self):
		print(self.board[0], self.board[1])
		return  sum(self.board[0]) - sum(self.board[1])

	def enum(self, board, player: int) -> list[tuple[list[int], int]]:
		

	#def suggest(board, player: int, depth: int) -> int:
	# TODO
ai = MinMax(game, 4)
game.play(board, 0, 3)
game.play(board, 1, 1)
game.play(board, 0, 5)
game.play(board, 1, 2)

print(ai.final_score())
#def main():


#if __name__ == "__main__":
	#main()
