import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shot)
    asteroid_field = AsteroidField()
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updateable.update(dt)

        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for s in shot:
                if s.collisions(asteroid):
                    s.kill()
                    split_results = asteroid.split()
                    if split_results is not None:
                        new_asteroid_1, new_asteroid_2 = split_results
                        asteroids.add(new_asteroid_1, new_asteroid_2)
                        

        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

