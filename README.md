# Minesweeper-Game
The game is a Minesweeper-like implementation where players dig tiles to avoid hidden bombs. The goal is to uncover all safe tiles without triggering any bombs.

The step by step description:

Initialization: The game starts by initializing a board with a specified dimension size and number of bombs.
Board Creation: A board is created with dimensions and bombs placed randomly.
Assigning Values: Values are assigned to each cell indicating the number of neighboring bombs.
Game Loop: The game enters a loop until either all safe cells are uncovered or a bomb is hit.
Player Input: Players input coordinates to dig, represented as row and column numbers.
Digging: The game reveals the contents of the selected cell. If it's a bomb, the game ends; otherwise, it continues.
Recursive Digging: If the selected cell has no neighboring bombs, adjacent cells are automatically dug.
Game Over: If a bomb is hit, the game ends and displays the final state of the board.
Victory: If all safe cells are uncovered without hitting a bomb, the player wins.
End of Game: The game concludes with either a victory or a defeat message.


DEMO:

![image](https://github.com/arshasuresh03/Minesweeper-Game/assets/160167081/3961ae54-ea4d-4a8b-8bef-fd7e341ed680)

![image](https://github.com/arshasuresh03/Minesweeper-Game/assets/160167081/cfce5156-873d-4605-847e-45e780532f00)

![image](https://github.com/arshasuresh03/Minesweeper-Game/assets/160167081/339b96a9-16dd-41ba-bd99-3e09a6e9d1a2)

![image](https://github.com/arshasuresh03/Minesweeper-Game/assets/160167081/ee6cda0b-542b-4019-a59e-c4ec0d6b59d1)
