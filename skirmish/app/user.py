#import grid
from pieces import pieces # This imports the pieces class from the pieces module

class user(object):

    def _init_:

        piece = pieces()
# Create ship instances
        carrier = pieces.createPiece(piece, 5)
        battleship = pieces.createPiece(piece, 4) # Here we call the method using the class name and the instance variable
        cruiser = pieces.createPiece(piece, 3)
        sub = pieces.createPiece(piece, 3)
        destroyer = pieces.createPiece(piece, 2)
        
# A grid to play on
        grid = grid()
        grid.createGrid()

    def placePiece(self, x, y):
        grid.placePiece (x, y, piece)

    def getGrid(self):
        return grid

