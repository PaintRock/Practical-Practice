import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))

# Caption and thumbnail image 
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("palm-tree.png") 
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# create the screen 
screen = pygame.Surface((100,200))

WHITE = (255,255,255)

FPS = 60    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                        
    pygame.display.update()
    clock.tick(60)      
            
    
if  __name___ == "__main__":
    main()

    