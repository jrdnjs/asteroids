import pygame
import random
from constants import *
from player import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            positive_random_angle = self.velocity.rotate(random_angle)
            negative_random_angle = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = positive_random_angle * 1.2
            asteroid_b.velocity = negative_random_angle * 1.2
            return asteroid_a, asteroid_b
