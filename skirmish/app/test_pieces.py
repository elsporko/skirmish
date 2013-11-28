#!/usr/local/bin/python
#-*- coding:utf-8 -*-

import unittest
from pieces import pieces # This imports the pieces class from the pieces module
import pprint

#pp = pprint.PrettyPrint(indent=4)

class test_pieces(unittest.TestCase):

    def setUp(self):

    def test_createPiece(self):
        piece = pieces()                          # This creates the instance of pieces

        #carrier = pieces.createPiece(piece, 5)
        #battleship = pieces.createPiece(piece, 4) # Here we call the method using the class name and the instance variable
        #cruiser = pieces.createPiece(piece, 3)
        #sub = pieces.createPiece(piece, 3)
        #destroyer = pieces.createPiece(piece, 2)
    
        
if __name__ == '__main__':
    unittest.main()

