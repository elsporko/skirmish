from unit import Unit

class pieces(object):

    def createPiece(self, size):
        piece_list = []
        for u in range (size):
            part = Unit()
            piece_list.append(part)
        return piece_list

