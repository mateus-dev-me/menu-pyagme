
import pygame
from menu import Menu

pygame.init()
pygame.mixer.init()

width = 640
height = 360

window = pygame.display.set_mode((width, height))
window_title = pygame.display.set_caption("Menu")

clock = pygame.time.Clock()

loop = True
loop_game = True

bg = Menu("sprites/bg.png")

bg2 = Menu("sprites/bg.png")
bg2.sprite.rect[1] = -360

logo = Menu("sprites/logo.png")
logo.sprite.rect[0] = int(width / 2 - logo.sprite.rect[2] / 2)
logo.sprite.rect[1] = 40

button_play = Menu("sprites/play.png")
button_play.sprite.rect[0] = int(width / 2 - button_play.sprite.rect[2] / 2)
button_play.sprite.rect[1] = 200

button_quit = Menu("sprites/quit.png")
button_quit.sprite.rect[0] = int(width / 2 - button_play.sprite.rect[2] / 2)
button_quit.sprite.rect[1] = 280

seta = Menu("sprites/seta.png")
seta.sprite.rect[0] = button_play.sprite.rect[0] - seta.sprite.rect[2] - 10
seta.sprite.rect[1] = 220

direction = 1
choose = 0
seta_pos = [220, 300]


hit = pygame.mixer.Sound("sounds/click.wav")
pygame.mixer.music.load("sounds/bg.ogg")
pygame.mixer.music.play()


def events():
    global loop, choose, loop_game

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                seta.sprite.rect[1] = seta_pos[0]
                choose = 0
                hit.play()
                loop_game = True
            if event.key == pygame.K_DOWN:
                seta.sprite.rect[1] = seta_pos[1]
                choose = 1
                hit.play()
            if event.key == pygame.K_SPACE:
                if choose == 0:
                    stage_1()
                elif choose == 1:
                    loop = False


def draw():
    global direction

    window.blit(bg.sprite.image, bg.sprite.rect)
    window.blit(bg2.sprite.image, bg2.sprite.rect)
    window.blit(logo.sprite.image, logo.sprite.rect)
    window.blit(button_play.sprite.image, button_play.sprite.rect)
    window.blit(button_quit.sprite.image, button_quit.sprite.rect)
    window.blit(seta.sprite.image, seta.sprite.rect)

    bg.sprite.rect[1] += 1
    if bg.sprite.rect[1] == 360:
        bg.sprite.rect[1] = 0

    bg2.sprite.rect[1] += 1
    if bg2.sprite.rect[1] == 0:
        bg2.sprite.rect[1] = -360

    seta.sprite.rect[0] += direction
    if seta.sprite.rect[0] == 210:
        direction *= -1
    elif seta.sprite.rect[0] == 200:
        direction *= -1


def main_menu():
    while loop:

        clock.tick(30)
        events()
        draw()
        pygame.display.update()


def stage_1():
    while loop:
        window.fill((0, 0, 0))

        clock.tick(30)
        events()
        pygame.display.update()


main_menu()
