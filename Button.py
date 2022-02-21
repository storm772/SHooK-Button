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

buttonBoundsX, buttonBoundsY = 10, 50 # positions
buttonBounds2W, buttonBounds2H = 100, 32 # width height (W,H)
borderRect = pygame.Rect(buttonBoundsX-3, buttonBoundsY-3, buttonBounds2W+6, buttonBounds2H+6)
buttonRect = pygame.Rect(buttonBoundsX, buttonBoundsY, buttonBounds2W, buttonBounds2H)

def drawButton():
    pygame.draw.rect(screen, (0,0,0), borderRect)
    pygame.draw.rect(screen, (200, 200, 200), buttonRect)

def onClick():
    print('hello')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Perfect colliding box in button
            if buttonRect.collidepoint(event.pos): 
                onClick()
    drawButton()
    
    screen.blit(base_font.render(' Button', True, (0,0,0)), buttonRect)
    pygame.display.update()
    pygame.time.Clock().tick(60)
