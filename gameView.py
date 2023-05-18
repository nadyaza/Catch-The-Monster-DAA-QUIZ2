import os
import shlex
import sys
import random
import pygame
import finding_shortest
 
# Class for the orange dude
class Player(object):
    
    def __init__(self):
        self.image_surf = pygame.image.load("asset/ninja.png").convert_alpha()
        self.resized = pygame.transform.scale(self.image_surf, (55, 55))
        self.x = 10
        self.y = 643
 
    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0,)
        if dy != 0:
            self.move_single_axis(0, dy,)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.x += dx
        self.y += dy
        self._player_rect = pygame.Rect(self.x, self.y, self.resized.get_width(), self.resized.get_height())
        self._player_rect.center = (self.x, self.y)
 
class Enemy(object):
    
    def __init__(self):
        self.end_rect = pygame.image.load("asset/monster.png").convert_alpha()
        self.resized = pygame.transform.scale(self.end_rect, (55, 55))
        self.x = 950
        self.y = 90

class Wall(object) :
    
    def __init__(self, x, y):
        self.bg = pygame.image.load("asset/rumput.png").convert()
        self.resized = pygame.transform.scale(self.bg, (50, 50))
        self.x = x
        self.y = y
        Walls.append(self)
        
class Road(object) :
    
    def __init__(self, img, x, y):
        self.model = pygame.image.load(img).convert()
        self.resized = pygame.transform.scale(self.model, (50, 50))
        self.x = x
        self.y = y
        Roads.append(self)

class Pos(object) :
    
    def __init__(self, img, x, y, index):
        self.Pos = pygame.image.load(img).convert()
        self.resized = pygame.transform.scale(self.Pos, (50, 50))
        self.x = x
        self.y = y
        self.index = index
        self.question = 1
        Poss.append(self)
        finding_shortest.insertPos(index)
        
def checkWall(player, Walls, maskP) :
    sign = 0
    for wall in Walls:
        maskW = pygame.mask.from_surface(wall.resized)
        offset = (wall.x - player.x, wall.y - player.y)
        if maskP.overlap(maskW, offset):
            sign = 1
        
    return sign

def checkPos(player, Poss, maskP) :
    sign = 0
    for Pos in Poss:
        maskH = pygame.mask.from_surface(Pos.resized)
        offset = (Pos.x - player.x, Pos.y - player.y)
        if maskP.overlap(maskH, offset):
            if(Pos.question == 1) : 
                Route.append(Pos.index)
                sign = finding_shortest.check(Route)
                    
            Pos.question = 0
            break

    return sign
        
def win_page():
    pygame.display.set_caption("Congratulations!")

    FILL = pygame.image.load("asset/win.png")
    SCREEN = pygame.display.set_mode((1000, 800))
    SCREEN.blit(FILL, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        
def lose_page():
    pygame.display.set_caption("Try to get the shortest path!")

    FILL = pygame.image.load("asset/game_over.png")
    SCREEN = pygame.display.set_mode((1000, 800))
    SCREEN.blit(FILL, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
         
# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
 
# Set up the display
pygame.display.set_caption("Try to Catch the Monster with Shortest Path!")
screen = pygame.display.set_mode((1000, 800))
 
clock = pygame.time.Clock()
Walls = []
Roads = []
Poss = []
Route = []
player = Player() # Create the player
enemy = Enemy()
 
# Holds the level layout in a list of strings.
level = [
    "DD1WWWWWWWWWWWWWWWWW",
    "WWTDDDD1WWWNW3DDD1WW",
    "WWWWWWWNWBWNWNWWW2QD",
    "W3SDD1W2DSDSD4WWWWNW",
    "WNWWWTXWWWWWWWWWWWNW",
    "DS1W34W3DDDQDDDDDDS1",
    "WWNWNWYRWWWNWWWWWWWN",
    "WWTD4WW21WW2DDD1WWYR",
    "WWNWWWWWNWWWWWWNWBWN",
    "WYFDDDDDSQDXWYDFDRWN",
    "WWNWWWWWWNWWWWWNWNWN",
    "WWNWWW3DDSDDDQD4WNWN",
    "WWNWWWNWWWWWWNWWWNWN",
    "DDSDDDSDDDQDDFDDD4WN",
    "WWWWWWWWWWZWWNWWWWWN",
    "WWWWWWWWWWWYDSDDDDD4",
]

x = y = 0
index = 'A'
for row in level:
    for col in row:
        if col == "W":
            Wall(x, y)
            finding_shortest.draw('#')
        if col == "D":
            Road("asset/jalan_2.png", x, y) #ini jalan datar
            finding_shortest.draw('*')
        if col == "N":
            Road("asset/jalan_1.png", x, y)
            finding_shortest.draw('*')
        if col == "B":
            Road("asset/buntu_1.png", x, y)
            finding_shortest.draw('!')
        if col == "X":
            Road("asset/buntu_4.png", x, y) #ini harusnya buntu kanan
            finding_shortest.draw('!')
        if col == "Y":
            Road("asset/buntu_3.png", x, y)
            finding_shortest.draw('!')
        if col == "Z":
            Road("asset/buntu_2.png", x, y)
            finding_shortest.draw('!')
        if col == "1":
            Road("asset/belokan_4.png", x, y)
            finding_shortest.draw('1')
        if col == "2":
            Road("asset/belokan_2.png", x, y)
            finding_shortest.draw('2')
        if col == "3":
            Road("asset/belokan_3.png", x, y)
            finding_shortest.draw('3')
        if col == "4":
            Road("asset/belokan_1.png", x, y)
            finding_shortest.draw('4')
        if col == "Q":
            Pos("asset/pertigaan_2.png", x, y, index)
            finding_shortest.draw(index)
            index = chr(ord(index) + 1)
        if col == "R":
            Pos("asset/pertigaan_3.png", x, y, index)
            finding_shortest.draw(index)
            index = chr(ord(index) + 1)
        if col == "S":
            Pos("asset/pertigaan_1.png", x, y, index)
            finding_shortest.draw(index)
            index = chr(ord(index) + 1)
        if col == "T":
            Pos("asset/pertigaan_4.png", x, y, index) #ini pertigaan T hadap kanan
            finding_shortest.draw(index)
            index = chr(ord(index) + 1)
        if col == "F":
            Pos("asset/perempatan.png", x, y, index)
            finding_shortest.draw(index)
            index = chr(ord(index) + 1)
        x += 50
    y += 50
    x = 0

finding_shortest.roadMap() #to draw a map reference
finding_shortest.printG() #print graph
    
running = True
while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
 
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        sign = 0
        player.move(-2, 0)
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(2, 0)
        
        sign = checkPos(player, Poss, maskP)
        if sign == 2:
            print("WIN")
        elif sign == -1 :
            print("LOSE")
            lose_page()

    if key[pygame.K_RIGHT]:
        sign = 0
        player.move(2, 0)
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(-2, 0)
        
        sign = checkPos(player, Poss, maskP)
        if sign == 2:
            print("WIN")
        elif sign == -1 :
            print("LOSE")
            lose_page()
            
    if key[pygame.K_UP]:
        sign = 0
        player.move(0, -2)
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(0, 2)
        
        sign = checkPos(player, Poss, maskP)
        if sign == 2:
            print("WIN")
        elif sign == -1 :
            print("LOSE")
            lose_page()
            
    if key[pygame.K_DOWN]:
        sign = 0
        player.move(0, 2)
        
        sign = checkWall(player, Walls, maskP)
        if sign == 1:
            player.move(0, -2)
        
        sign = checkPos(player, Poss, maskP)
        if sign == 2:
            print("WIN")
        elif sign == -1 :
            print("LOSE")
            lose_page()
 
    maskP = pygame.mask.from_surface(player.resized)
    maskE = pygame.mask.from_surface(enemy.resized)
    
    offset = (enemy.x - player.x, enemy.y - player.y)
    if maskP.overlap(maskE, offset):
        win_page()
            
    # Draw the scene
    for wall in Walls:
         screen.blit(wall.resized, (wall.x, wall.y))
    for road in Roads:
         screen.blit(road.resized, (road.x, road.y))
    for Pos in Poss:
         screen.blit(Pos.resized, (Pos.x, Pos.y))
    screen.blit(enemy.resized, (enemy.x, enemy.y))
    screen.blit(player.resized, (player.x, player.y))
    
    pygame.display.flip()
    clock.tick(360)
 
pygame.quit()
