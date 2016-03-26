from com.max.chess.dao.Player import Player
from com.max.chess.dao.Game import Game

def playGame():
    player1 = Player("Player1")
    #player1.display()
    player2 = Player("Player2")
    #player2.display()
    game = Game(player1, player2)
    game.current_position()

if __name__ == "__main__":
    playGame()