import pygame

import constants
from logger import log_state
from player import Player


def main():
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    ship = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
