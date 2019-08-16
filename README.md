# nim-game-simulation
A simulation of all the possible game states of nim.

https://en.wikipedia.org/wiki/Nim

The Game of Nim is an ancestral game of strategy played with some objects 
(sticks, stones, coins, etc.) The game is played with 2 players. It begins 
with a number of tokens (i.e. objects) places in a pile or group. The players 
take turns dividing the pile into smaller piles under some conditions:

At each turn, a pile must be split into 2 non-empty piles of different sizes.
The player who does the last possible split wins.

With a program playing a board game against an opponent, the computer builds 
such a tree and each level represents a player. It is a convention to refer 
to the computer player level as "Max" and the human or opponent player as "Min". 
We can mark all nodes by "Max" or "Min" depending upon the level in the tree. 
This way we know if a leaf node is marked as "Max" the computer loses if it gets 
to that stage. However, if a leaf node is on a "Min" level, we know the computer 
would win arriving at that stage.

Built using the Python language.
