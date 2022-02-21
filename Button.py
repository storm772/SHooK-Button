import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([200, 95])
pygame.display.set_caption("[SHooK] Button")

font = pygame.font.SysFont(None, 32)
def renderText(text, *pos):
    if not (pos): pos = (100,100)
    testE = font.render(text, True, (0))
    screen.blit(testE, (pos))

screen.fill((255,255,255))
renderText(f'Click this Button:', (10, 12))

base_font = pygame.font.SysFont('Arial', 25)

active = False 

x, y, w, h = 10, 50, 100, 32
borderRect = pygame.Rect(x-3, y-3, w+6, h+6)
buttonRect = pygame.Rect(x, y, w, h)

def drawButton():
    pygame.draw.rect(screen, (0,0,0), borderRect)
    pygame.draw.rect(screen, (200, 200, 200), buttonRect)

def onClick():
    print('hello')

def renderButton(text):
    screen.blit(base_font.render(text, True, (0,0,0)), (buttonRect.x*2, buttonRect.y+1.5))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if clicked at input box or its border
            if buttonRect.collidepoint(event.pos): 
                active = True 
                onClick()
                active = False
    drawButton()
    renderButton('Button')

    pygame.display.update()
    pygame.time.Clock().tick(60)
