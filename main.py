import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    clock = pygame.time.Clock()
    dt = 0

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for d in drawable:
            d.draw(screen)

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            collides = a.collides(player)
            if collides:
                print('Game over!')
                sys.exit()

            for s in shots:
                collides = s.collides(a)
                if collides:
                    a.kill()
                    s.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == '__main__':
    main()
