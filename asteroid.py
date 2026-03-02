import pygame
import random
from circleshape import CircleShape
from constants import (LINE_WIDTH,
                       ASTEROID_MIN_RADIUS
                       )
from logger import log_event


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    
    def draw(self, screen):
        pygame.draw.circle(screen, 
                            "white", 
                            self.position, 
                            self.radius,
                            LINE_WIDTH,
                            )
    

    def update(self, dt):
        self.position += self.velocity * dt

    
    def split(self):
        rando_angle = random.uniform(20.0, 50.0)
        new_asteroid1_velo = self.velocity.rotate(rando_angle)
        new_asteroid2_velo = self.velocity.rotate(-rando_angle)
        small_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        log_event("asteroid_split")
        
        new_asteroid1 = Asteroid(self.position.x, 
                                 self.position.y, 
                                 small_asteroid_radius,
                                 )
        new_asteroid2 = Asteroid(self.position.x, 
                                 self.position.y, 
                                 small_asteroid_radius,
                                 )
        
        self.kill()
        new_asteroid1.velocity = new_asteroid1_velo
        new_asteroid1.velocity *= 1.2
        new_asteroid2.velocity = new_asteroid2_velo
