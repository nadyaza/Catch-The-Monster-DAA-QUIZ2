# Catch-The-monster-DAA-Quiz2
Group Members:
1. Dilla Wahdana	5025211060
2. Nadya Zuhria A	5025211058
3. Wardatul Amalia S	5025211006


In this project, we made a game that asked the player to move the ninja towards the monsters via the shortest path. However, we do not indicate which path is the shortest path. There are many branching roads to get to the monsters that can be chosen by the player. If the path that the player finally goes through is the shortest path, then the player wins. Meanwhile, if the path is not the shortest path, a game over sign will appear. To determine the shortest path, we use Dijkstra's algorithm which is one of the algorithms taught in DAA
 
Explanation of Code Dijkstra

Dijkstra's Algorithm:
1. Create a set of unvisited vertices and initialize the distance of all vertices to infinity except the source vertex, which is set to 0.

While the set of unvisited vertices is not empty, do the following:

a. Choose the vertex with the minimum distance from the set of unvisited vertices and mark it as visited.

b. For each neighbor of the current vertex that is still unvisited, calculate the tentative distance by adding the distance from the current vertex to the neighbor to the current vertex's distance.

2. If the tentative distance is less than the neighbor's current distance, update the neighbor's distance with the tentative distance.
3. Once all vertices have been visited or if the destination vertex has been visited, stop the algorithm.
4. The shortest path from the source vertex to the destination vertex can be reconstructed by backtracking from the destination vertex to the source vertex using the recorded shortest distances and predecessors.

Note: Dijkstra's algorithm assumes non-negative edge weights and finds the shortest path in terms of the sum of edge weights.



```
def shortest_path(graph, start, finish, route):
    length = {}   # stores the shortest distance from the starting point to each point in the
    prev = {}  # saves the previous point connected with each point
    stack = []   # the stack variable is used to sort points by distance
```

Inside shortest_path function, we also initialize the distance of all points with an infinite value, except for the starting point which has a value of 0. This is done to ensure that the shortest distance from the starting point to each point is not yet known.
```
    for vertex in graph:
        length[vertex] = float('inf')
    length[start] = 0
```

Then, adds the starting point to the stack
   ```
   heapq.heappush(stack, (length[start], start))
```

Iterating using the stack: As long as the stack is not empty, iterates to take the point with the shortest distance from the stack
   ```
   while stack:
        current_distance, current_node = heapq.heappop(stack)
   ```

If the current shortest distance is greater than the existing distance, skip this point
```
        if current_distance > length[current_node]:
            continue
```

        When it reaches the end point, stop the algorithm
        ```
        if current_node == finish:
            break
        ```

        Iterate through the neighbors of the current point
        ```
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
        ```
If the new distance is shorter than the previous distance, update the previous distance and point values
```
if distance < length[neighbor]:
                length[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(stack, (distance, neighbor))
```


Build the shortest path from the starting point to the ending point, following the previous point that has been stored in the 'prev' variable.
```
    path = []
    current = finish
    while current in prev:
        path.insert(0, current)
        current = prev[current]
    path.insert(0, start)
```

Display results: Shortest path and given path (route) will be displayed on terminal. This code is used to debugging the program and make sure that the program run well
```    
    print(f"Shortest path from {start} to {finish}: {path}")
    print(f"Path that passed by Player from {start} to {finish}: {route}")
```
If the shortest path is equal to the given path, the function returns 2. Otherwise, the function returns -1.
```
    if route == path:
        return 2
    else:
        return -1
```
The graph used in this program will be taken from the map that was created in gameView.py
```
pos = []    # to store the index of each created node
map = []    # to save the map reference from the gameView
Mgraph = {}  # the obtained graph
```

It's a function to add index to post
```
def insertPos(index) :
    pos.append(index)
```
 
This is the function to include map description from gameview  
```
def draw(sign) :
    map.append(sign)
```
This function below is to get branches from each node (pos) along with their distance. To get a complete graph, we must iterate over all the elements from the pos and check the left branch, right branch, top branch, and bottom branch.

For each branch obtained, it will be entered into the ‘Mgraph’ dict as a reference for determining the shortest path using the Dijkstra algorithm
```  
def roadMap() :
    for element in pos :
        temp = {}
       
        #Search left branch
        i = map.index(element) - 1
        sign = 'l'
        distance_l = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_l += 1
            if(map[i] == '1') :
                sign = 'l'
            elif(map[i] == '2') :
                sign = 'u'
            elif(map[i] == '3') :
                sign = 'd'
            elif(map[i] == '4') :
                sign = 'l'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                temp[map[i]] = distance_l
                #roadMap(map[i])
                sign = 'f'
       
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'f') : i = 0
           
        #Search top branch
        i = map.index(element) - 20
        sign = 'u'
        distance_u = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_u += 1
            if(map[i] == '1') :
                sign = 'l'
            elif(map[i] == '2') :
                sign = 'u'
            elif(map[i] == '3') :
                sign = 'r'
            elif(map[i] == '4') :
                sign = 'l'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                temp[map[i]] = distance_u
                #roadMap(map[i])
                sign = 'f'
           
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'r') : i += 1
            elif(sign == 'f') : i = 0
       
        #Search right branch
        i = map.index(element) + 1
        sign = 'r'
        distance_r = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_r += 1
            if(map[i] == '1') :
                sign = 'd'
            elif(map[i] == '2') :
                sign = 'r'
            elif(map[i] == '3') :
                sign = 'r'
            elif(map[i] == '4') :
                sign = 'u'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                temp[map[i]] = distance_r
                #roadMap(map[i])
                sign = 'f'
           
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'r') : i += 1
            elif(sign == 'f') : i = 0


        #Search bottom branch
        i = map.index(element) + 20
        sign = 'd'
        distance_d = 0
        while(i > 0 and i < len(map)) :
            #print(map[i])
            distance_d += 1
            if(map[i] == '1') :
                sign = 'd'
            elif(map[i] == '2') :
                sign = 'r'
            elif(map[i] == '3') :
                sign = 'd'
            elif(map[i] == '4') :
                sign = 'l'
            elif(map[i] == "*") :
                sign = sign
            elif(map[i] == "!") :
                sign = 'f'
            elif(map[i] == '#') :
                sign = 'f'
            else :
                temp[map[i]] = distance_d
                #roadMap(map[i])
                sign = 'f'
           
            if(sign == 'd') : i += 20
            elif(sign == 'u') : i -= 20
            elif(sign == 'l') : i -= 1
            elif(sign == 'r') : i += 1
            elif(sign == 'f') : i = 0
             
        Mgraph[element] = temp
```
There are many if and elif while checking the branch. It’s because there are many type of road. And the program must adapt with all type of road model to get accurate distance of one node to another node.

Function to print the Mgraph obtained
```
def printG() :
    for node, branch in Mgraph.items():
        print(node, branch)
```
This is the Mgraph that obtained from map in gameView while the pogram run



This is the function that will be used to call the DJikstra algorithm and determine the win or lose status of the game. Route is the sequence of paths traversed by the player. if the Route is the same as the shortest path, it will be declared the win state. If not the same, then declared a lose state
```
def check(Route) :
    win = shortest_path(Mgraph, 'T', 'B', Route)
    return win
```
At this game, starting point is ‘T’ and end point is ‘B’. So, we start to find shortest path from T to B.

From Djikstra’s Algorithm we found that the shortest path from ‘T’ to ‘B’ is ['T', 'M', 'N', 'J', 'H', 'I', 'B'] 


CODE FOR “MAIN”
```
import pygame, sys
from button import Button
import subprocess


import os
import random


pygame.init()


SCREEN = pygame.display.set_mode((928, 672))
pygame.display.set_caption("Menu")


BG = pygame.image.load("asset/main_menu.png")
   
def run_game(level_code):
    subprocess.call(["python", level_code])
   
def about():
    while True:
        ABOUT_MOUSE_POS = pygame.mouse.get_pos()
        pygame.display.set_caption("About")
       
        FILL = pygame.image.load("asset/about.png")


        SCREEN.blit(FILL, (0, 0))
       
        ABOUT_BACK = Button(image=pygame.image.load("asset/silang.png"), pos=(878, 50))


        ABOUT_BACK.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ABOUT_BACK.checkForInput(ABOUT_MOUSE_POS):
                    main_menu()


        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))


        MENU_MOUSE_POS = pygame.mouse.get_pos()


        PLAY_BUTTON = Button(image=pygame.image.load("asset/play_button.png"), pos=(465, 300))
        ABOUT_BUTTON = Button(image=pygame.image.load("asset/about_button.png"), pos=(465, 400))
        EXIT_BUTTON = Button(image=pygame.image.load("asset/exit_button.png"), pos=(465, 500))


        for button in [PLAY_BUTTON, ABOUT_BUTTON, EXIT_BUTTON]:
            button.update(SCREEN)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    run_game("gameView.py")
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    about()
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()


main_menu()
```

EXPLANATION FOR “MAIN” CODE

Here's an explanation of the algorithm and functions in the code:
1. The necessary libraries are imported:
- pygame is the main library used for game development in Python.
- sys provides access to some variables and functions used to manipulate Python runtime environment.
- subprocess allows running external commands or programs.
2. The Pygame module is initialized using pygame.init().
3. A Pygame window is created using pygame.display.set_mode((928, 672)), with a resolution of 928x672 pixels. The window's title is set to "Menu" using pygame.display.set_caption("Menu").
4. The background image for the menu screen is loaded from the file "asset/main_menu.png" using pygame.image.load(). It is assigned to the variable BG.
5. The run_game(level_code) function is defined, which takes a level_code argument. This function is responsible for running the game when a play button is clicked. It uses the subprocess.call() function to execute the command python level_code in a separate process.
6. The about() function is defined, which displays the "About" screen and handles user interactions. It contains a loop that continuously updates the screen and checks for events. The "About" screen's background image is loaded from the file "asset/about.png" and assigned to the variable FILL. The function also creates a button for returning to the main menu.
7. The main_menu() function is defined, which displays the main menu screen and handles user interactions. It contains a loop that continuously updates the screen and checks for events. The main menu screen's background image is set to BG. The function creates buttons for playing the game, accessing the "About" screen, and exiting the program.
8. Inside the main_menu() loop, the Button objects are updated and checked for user input. If the play button is clicked, the run_game() function is called with the argument "gameView.py" to start the game. If the about button is clicked, the about() function is called to display the "About" screen. If the exit button is clicked, the program is terminated using pygame.quit() and sys.exit().
9. The main_menu() function is called to start the menu loop and display the menu screen.


CODE FOR “BUTTON” 
```
import pygame


class Button():
    def _init_(self, image, pos):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        if self.image is not None:
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        else:
            self.rect = pygame.Rect(self.x_pos, self.y_pos, 0, 0)


    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)


    def checkForInput(self, position):
        return self.rect.collidepoint(position)
```

EXPLAIN FOR “BUTTON” CODE

Here's an explanation of the algorithm and functions in the code:
1. The pygame library is imported at the beginning of the code.
2. The Button class is defined. This class represents a clickable button in a graphical user interface.
3. The __init__() method is the constructor of the Button class. It initializes the button object with an image and position. It takes two parameters: image (the image of the button) and pos (the position of the button on the screen). The x_pos and y_pos attributes of the button are set based on the pos parameter. If the image is not None, the rect attribute is set using the get_rect() method of the image, with the center position specified by x_pos and y_pos. Otherwise, if the image is None, a Rect object is created with the position specified by x_pos and y_pos and with a width and height of 0.
4. The update() method updates the button on the screen. It takes a screen parameter, which is the Pygame surface where the button should be drawn. If the image is not None, the blit() function is called to draw the image on the screen at the position specified by rect.
5. The checkForInput() method checks if a position (usually the mouse position) is within the boundaries of the button. It takes a position parameter, which is the position to be checked. The collidepoint() method of the rect attribute is used to determine if the position is within the button's boundaries. If the position collides with the button (i.e., it is within the button's boundaries), the method returns True; otherwise, it returns False.


EXPLAIN FOR “GAME VIEW”
This is the core code of Djikstra implementation. In this game, we define some object classes. Those are Player to define Ninja, Enemy to define Monsters, Wall to define Grass, Road to define path, and Pos to define road that also being a node for Mgraph.
```
class Player(object):
    #Initialize player
    def __init__(self):
        self.image_surf = pygame.image.load("asset/ninja.png").convert_alpha()
        self.resized = pygame.transform.scale(self.image_surf, (45, 45))
        self.x = 10
        self.y = 585
 
    #Move the player
    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0,)
        if dy != 0:
            self.move_single_axis(0, dy,)
   
    #Move single axist
    def move_single_axis(self, dx, dy):
        self.x += dx
        self.y += dy
        self._player_rect = pygame.Rect(self.x, self.y, self.resized.get_width(), self.resized.get_height())
        self._player_rect.center = (self.x, self.y)
 
class Enemy(object):
    #Initialize Monsters
    def __init__(self):
        self.end_rect = pygame.image.load("asset/monster.png").convert_alpha()
        self.resized = pygame.transform.scale(self.end_rect, (50, 50))
        self.x = 855
        self.y = 85


class Wall(object) :
    #initialize wall / grass
    def __init__(self, x, y):
        self.bg = pygame.image.load("asset/rumput.png").convert()
        self.resized = pygame.transform.scale(self.bg, (45, 45))
        self.x = x
        self.y = y
        Walls.append(self)
       
class Road(object) :
    #initialize road / path
    def __init__(self, img, x, y):
        self.model = pygame.image.load(img).convert()
        self.resized = pygame.transform.scale(self.model, (45, 45))
        self.x = x
        self.y = y
        Roads.append(self)


class Pos(object) :
    #initialize road that also be node in Mgraph or define as Pos
    def __init__(self, img, x, y, index):
        self.Pos = pygame.image.load(img).convert()
        self.resized = pygame.transform.scale(self.Pos, (45, 45))
        self.x = x
        self.y = y
        self.index = index
        self.question = 1
        Poss.append(self)
        finding_shortest.insertPos(index) 
```


This game will be set in 900 x 720 screen display
```
# Initialize pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
 
# Set up the display
pygame.display.set_caption("Try to Catch the Monster with Shortest Path!")
screen = pygame.display.set_mode((900, 720))
``` 

After that, to display the map in the game screen, we must define character in “Level” one by on
```
# Holds the level layout in a list of strings.
level = [
    "DD1WWWWWWWWWWWWWWWWW",
    "WWTDDDD1WWWNW3DDD1WW",
    "WWNWWWWNWBWNWNWWW2QD",
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
            Road("asset/jalan_1.png", x, y)
            finding_shortest.draw('*')
        if col == "N":
            Road("asset/jalan_2.png", x, y)
            finding_shortest.draw('*')
        if col == "B":
            Road("asset/buntu_1.png", x, y)
            finding_shortest.draw('!')
        if col == "X":
            Road("asset/buntu_2.png", x, y)
            finding_shortest.draw('!')
        if col == "Y":
            Road("asset/buntu_4.png", x, y)
            finding_shortest.draw('!')
        if col == "Z":
            Road("asset/buntu_3.png", x, y)
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
            Pos("asset/pertigaan_3.png", x, y, index)
            finding_shortest.draw(index)
            index = chr(ord(index) + 1)
        if col == "R":
            Pos("asset/pertigaan_4.png", x, y, index)
            finding_shortest.draw(index)
            index = chr(ord(index) + 1)
        if col == "S":
            Pos("asset/pertigaan_1.png", x, y, index)
            finding_shortest.draw(index)
            index = chr(ord(index) + 1)
        if col == "T":
            Pos("asset/pertigaan_2.png", x, y, index) #ini pertigaan T hadap kanan
            finding_shortest.draw(index)
            index = chr(ord(index) + 1)
        if col == "F":
            Pos("asset/perempatan.png", x, y, index)
            finding_shortest.draw(index)
            index = chr(ord(index) + 1)
        x += 45
    y += 45
    x = 0
```
Character in Level define a specific model of road that store in asset directory. Different model of road can be defined as different object. For example, grass is define as wall, and T-Junction is define as pos, crossroad also define as pos. For pos object, we must define an index with unique character. All the character in Level must be passed to finding_shortest.py by draw function to determine a map in finding_shortest.py.

After that, call roadMap function to make graph refer to map, and printG function to print Mgraph in terminal
```
finding_shortest.roadMap() #to draw a map reference
finding_shortest.printG() #print graph
```
To move Ninja, we use keyboard arrow. For every movement, we must check is the player overlap grass or not. We use checkWall to check this situation. If it is overlap (sign == 1) it will give a neutral movement or in otherwords, Ninja is not going anywhere because Ninja is only allowed to go through road path. We also check whenever Ninja is in the pos object, it will call checkpos to add path in route list. And if Ninja has arrived in ‘B’ pos, it will return sign = 2 or sign = -1 to determine that Ninja has finish a path to catch the Monsters. Sign = 2 means the path is same as shortest path that define by Djikstra’s algorithm. Sign = -1 means the path that through by player is not same as shortest path that define by Djikstra’s algorithm
```
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
                if(Pos.index == 'B') :
                    sign = finding_shortest.check(Route)
                   
            Pos.question = 0
            break


    return sign

if sign = 2 and Ninja overlap Monster, it will show the win page
    def win_page():
    pygame.display.set_caption("Congratulations!")


    FILL = pygame.image.load("asset/win.png")
    SCREEN = pygame.display.set_mode((928, 672))
    SCREEN.blit(FILL, (0, 0))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()


    maskP = pygame.mask.from_surface(player.resized)
    maskE = pygame.mask.from_surface(enemy.resized)
   
    offset = (enemy.x - player.x, enemy.y - player.y)
    if maskP.overlap(maskE, offset):
        win_page()

if sign = -1, it will show the lose_page (game over)
def lose_page():
    pygame.display.set_caption("Try to get the shortest path!")


    FILL = pygame.image.load("asset/game_over.png")
    SCREEN = pygame.display.set_mode((928, 672))
    SCREEN.blit(FILL, (0, 0))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()
```
And this is a program to display all object that has been created to the screen
```
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
```
