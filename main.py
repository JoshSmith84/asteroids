import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    
    
    print("Starting Asteroids with pygame version: 2.6.1\n"
    f"Screen width: {SCREEN_WIDTH}\n"
    f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    win_clock = pygame.time.Clock()
    dt = 0
    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = win_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
