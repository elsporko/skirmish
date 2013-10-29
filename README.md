skirmish
========

An experiment with varying technologies

About
-----
Skirmish is a sandbox application created as an excuse to play with the centrifuge messaging service (https://github.com/FZambia/centrifuge).

The application is similar to the game 'Battleship' where each player has a grid on which to place several 'battleship' pieces which extend over several grid points along the axis. Players take turns calling out grid coordinates which either 'hit' or 'miss' the opponent's ship. When a ship is has been completely hit it is considered 'sunk'. The object of the game is to sink the opponent's entire fleet.

Skirmish adds a little bit to the basic game in that it can be played by more than two players at once with the added twist that on their turn players can either volley a shot at an opponent OR request intelligence from other players about another. Players can make 1 attack move or 2 intelligence moves. For example if A, B, C and D are playing the game and it is A's turn then A can either attack any player or ask C and/or D what they know about hit/miss activities on B's grid for specific locations.


