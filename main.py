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