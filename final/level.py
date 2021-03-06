import pygame
from variables import *

class Level(object):
    """ Class for the level """
    wall_list = None
    enemy_sprites = None
    treasure_list = None
 
    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.treasure_list = pygame.sprite.Group()
 
        self.maze=[
        ["XXXXXXXXXXXXXXXXXXXXXXXXX",
        "X  T    X   P   X    T  X",
        "X  XXXX X XXXXX X XXXX  X",
        "X  X    X XXTXX X    X  X",
        "X  X XX           XX X  X",
        "X  X X      E      X X  X",
        "X T       XXXX        T X",
        "XX XXXXXX  TT  XXXXXXX XX",
        "XT    E   XXXX   E     TX",
        "X  XXXXXXXXXXXXXXXXXXX  X",
        "X  XT   XT    TX    TX  X",
        "X  XXX  XX XX XX   XXX  X",
        "X   E               E   X",
        "XXXXXXXXX      XXXXXXXXXX",
        "XX   TXXXXXTTXXXXXXT   XX",
        "XT     X  X  X  XX     TX",
        "XXXXX  XT X  X TXX  XXXXX",
        "XT     X        XX     TX",
        "XX E     T XX T     E  XX",
        "XX     XXXXXXXXXX      XX",
        "X     XXT XTTX TXX      X",
        "XT XXXXX  X  X  XXXXXX TX",
        "X  E      X  X      E   X",
        "X     T    E     T      X",
        "XXXXXXXXXXXXGXXXXXXXXXXXX",],

        ["XXXXXXXXXXXXXXXXXXXXXXXXX",
        "XT X      X     XP     TX",
        "X    EXXXXXXXX  XXXXX XXX",
        "X  XXX      X     X X   X",
        "X     E XXX T X X X XXX X",
        "XXXXXXXXX X X X X      EX",
        "XT          X    XXXXXXXX",
        "XXXXXXXX X  XTXX XT     X",
        "X     TX  X  X X    TX  X",
        "X XTX X  X     XXXXXXX TX",
        "X  XX  X XTX  X   X  XXXX",
        "X    E   XTX     E     XX",
        "XXX XXXXXX XXXXXX   XX  X",
        "X   XT X        XXXXTX  X",
        "X XXXX XXXXXXXX    X XXTX",
        "X       E    XXXXX   E  X",
        "XX XXXXXXXXX X   X XXXXXX",
        "X   XX  X    XXX X XX  TX",
        "X X    X  XXXX   X    XXX",
        "XX  XX  X E  X XXXXXX  XX",
        "XT  XXX TX XX  X    XX XX",
        "X X     XX X      XXTX  X",
        "X XXXXX   XXXXX XXXX XX X",
        "X     TXX    E  X    E  X",
        "XXXXXXXXXXXXGXXXXXXXXXXXX",],

        ["XXXXXXXXXXXXXXXXXXXXXXXXX",
        "X  T   E     E     T    X",
        "X XXXXX  XX  XXXXXXXXXXXX",
        "X XX  X  XT       T     X",
        "X X   X    X XXXX   XXX X",
        "X XX  XXXXXXXX  XXXXTXXTX",
        "X X      X    E   XX XX X",
        "X XXXXXX X XXXXXX    XX X",
        "X      X X XP  XX XXXXX X",
        "XXXXX  X X XXX XX X  TX X",
        "X      X X E   X  X X X X",
        "XXXXX  X X TXXXX  X XXX X",
        "X    T X XXX X X  X  XX X",
        "X XXXXXX      E   XXTXX X",
        "X X      TXXXXXXXXX  XX X",
        "X X  XXXX XX        E   X",
        "X X    TX  XT XXXXXXXXX X",
        "X XXXXXXX X   X  XX  XX X",
        "X    E     X   E      XTX",
        "XTXXX  XX XXXXXXXXXXX X X",
        "XX  X  X  XTX    X TX X X",
        "X  TX  XX X    X X XX XXX",
        "X XXX  XX XXX  X X X  XTG",
        "X      X      EX    X  TX",
        "XXXXXXXXXXXXXXXXXXXXXXXXX"],

        ["XXXXXXXXXXXXXXXGXXXXXXXXX",
        "XT    XX      XTTTX    TX",
        "X  XX  X  X   XX XX  XXXX",
        "X  X   X  XX  X T X EX  X",
        "X  XX      X  XX XX  XX X",
        "X  X E XXXXX   X X    X X",
        "XXXXX  X      XX XX  XX X",
        "XT  X  XXXXXXXXX XX     X",
        "X          X P X       XX",
        "X E   T    X X X   T    X",
        "XXXX  XXXXXX X XXXXX   XX",
        "XXTX  XXX          XX   X",
        "X     XT  X X XXX  XX  XX",
        "XXXX  XXXXXXXXX    XX   X",
        "X  X       E    TXX    XX",
        "XX XXX   XXXXXXXXXX X   X",
        "X      XX  X     XX X EXX",
        "X   E  X   X            X",
        "X  XXXXX    XXXXX      XX",
        "X  X X    X XTTTX  XXXXXX",
        "X  X  XX                X",
        "X  XX  X  XXXX X    XXX X",
        "X               XE  XTX X",
        "XXT XXTXX   XXTX    X   X",
        "XXXXXXXXXXXXXXXXXXXXXXXXX",],

        ["XXXXXXXXXXXXXXXXXXXXXXXXX",
		"XTTX  E  X    E     X   X",
		"X  XXXXX X  XXXXXX  XTX X",
		"X        X  X TXXX  XX  X",
		"X     E TX  X XE       XX",
		"XXXXXX  XX  X  XX E    XX",
		"XT  TX  XX  XX  XX  XX  X",
		"X XX X  XX    X  X  XTX X",
		"X    X    E   XX XT X   X",
		"X  XXX  XXXXX    XXXXXXXX",
		"X         XPXXXXXX      X",
		"X T  XTXX      X    XXXXX",
		"XXXXXXXXXXXXX  XXX  XX TX",
		"XTX  XTXTX  X    X  XX  X",
		"X    X X X  T    E      X",
		"XXX         XXXXXXXXXXXXX",
		"XXXXXXXXXX      XTX  X TX",
		"XX       X  E   X X XXX X",
		"G  XXXX  XT             X",
		"XXXXXX  XXXXXXXXXX  XXXXX",
		"XX   X  XXT T    X      X",
		"XT   X  XXXXXXXX X  XXX X",
		"XX       TX X X        TX",
		"XXTX  E         XXTX    X",
		"XXXXXXXXXXXXXXXXXXXXXXXXX"],]
