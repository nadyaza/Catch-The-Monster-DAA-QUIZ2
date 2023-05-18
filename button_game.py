import pygame
import requests
from io import BytesIO

class Button():
    def __init__(self, image, pos):
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


# Mengunduh gambar dari URL
def download_image(url):
    response = requests.get(url)
    image = pygame.image.load(BytesIO(response.content))
    return image


# Inisialisasi asset
button_play_url = 'https://raw.githubusercontent.com/nadyaza/Catch-The-Monster-DAA-QUIZ2/fa2faf9be48920a83cba9b80f42cebe48445df3e/asset/play_button.png'
button_about_url = 'https://raw.githubusercontent.com/nadyaza/Catch-The-Monster-DAA-QUIZ2/fa2faf9be48920a83cba9b80f42cebe48445df3e/asset/about_button.png'
button_exit_url = 'https://raw.githubusercontent.com/nadyaza/Catch-The-Monster-DAA-QUIZ2/fa2faf9be48920a83cba9b80f42cebe48445df3e/asset/exit_button.png'
background_url = 'https://raw.githubusercontent.com/nadyaza/Catch-The-Monster-DAA-QUIZ2/fa2faf9be48920a83cba9b80f42cebe48445df3e/asset/main_menu.png'
about_image_url = 'https://raw.githubusercontent.com/nadyaza/Catch-The-Monster-DAA-QUIZ2/fa2faf9be48920a83cba9b80f42cebe48445df3e/asset/about.png'

# Menggunakan asset dalam objek Button
button_play = Button(download_image(button_play_url), (200, 100))
button_about = Button(download_image(button_about_url), (200, 200))
button_exit = Button(download_image(button_exit_url), (200, 300))
background = download_image(background_url)
about_image = download_image(about_image_url)

# Contoh penggunaan dalam loop utama pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    button_play.update(screen)
    button_about.update(screen)
    button_exit.update(screen)
    pygame.display.flip()

pygame.quit()
