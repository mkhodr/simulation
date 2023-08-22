import math
import numpy as np
from random import randint, uniform, choices
import string

class Arena:
    def __init__(self, x=500, y=500):
        self.particles = []
        self.foods = []
        self.x = x
        self.y = y
        self.closest_food_dict = {}

    def add_particle(self, Particle):
        self.particles.append(Particle)

    def add_food(self, Food):
        self.foods.append(Food)

    def random_position(self):
        random_position = (round(uniform(0, self.x-1), 1), round(uniform(0, self.y-1), 1))
        return random_position
    
    def check_collision(self):
        foods = set(food.position for food in self.foods)
        particles = set(particle.position for particle in self.particles)
        collisions = foods & particles
        if collisions:
            for collision in collisions:
                for particle in self.particles:
                    if particle.position == collision:
                        collided_particle = particle
                for food in self.foods:
                    if food.position == collision:
                        collided_food = food
                self.foods.remove(collided_food)
                collided_particle.check_collision(collided_food)
            self.update_closest_food()
            return True
        return False


    def move_particles(self, closest_foods_dict):
        for particle in self.particles:
            closest_food = closest_foods_dict.get(particle.name)
            particle.move(closest_food)

    
    def update_closest_food(self):
        for particle in self.particles:
            closest_food = particle.closest_food(self.foods)
            self.closest_food_dict[particle.name] = closest_food
        return self.closest_food_dict

    def spawn_random_food(self):
        random_position = self.random_position()
        nutrition_value = randint(1,4)
        food = Food(nutrition_value, random_position)
        self.add_food(food)
        return

    def spawn_food(self, nutrition, position):
        nutrition_value = nutrition
        food = Food(nutrition_value, position)
        self.add_food(food)
        return

    def spawn_random_particle(self):
        name = ''.join(choices(string.ascii_uppercase + string.digits, k=4))
        random_position = self.random_position()
        size = randint(1,5)
        hunger = 10
        self.add_particle(Particle(name, size, hunger, random_position))
        return

    def spawn_particle(self, size, position):
        name = ''.join(choices(string.ascii_uppercase + string.digits, k=4))
        hunger = 10
        self.add_particle(Particle(name, size, hunger, position))
        return




class Particle:
    def __init__(self, name, size, hunger, position=(0.,0.)):
        self.name = name
        self.size = size
        self.hunger = hunger
        self.velocity = (2-(size*0.15))
        self.position = position
        

    def feed(self):
        self.hunger -= 1
        if self.hunger <= 0:
            self.size += 1
            self.hunger = 10
        return
    
    def closest_food(self, foods):
        x,y = self.position
        if foods:
            closest_food = min(foods, key=lambda food: math.sqrt((food.position[0] - x)**2 + (food.position[1] - y)**2))
            return closest_food
        return

    def check_collision(self, closest_food):
        if closest_food:
            if self.position == closest_food.position:
                self.hunger += closest_food.nutrition
                if self.hunger > 10:
                    self.size += 1
                    self.hunger = 0
                return True
        return False

    def move(self, closest_food):
        x,y = self.position
        velocity = self.velocity
        if closest_food:
            fx,fy = closest_food.position   # food x and y
            dx = fx - x                     # distance in X axis
            dy = fy - y                     # distance in Y axis
            if dx == 0 and dy == 0:         # particle in the same point as the food
                return
                # if self.check_collision(closest_food):
                #     foods.remove(closest_food)
            angle = math.atan2(dy,dx)       # in radians
            if angle < 0:                   # converting negative angles to positive
                angle += math.pi * 2
            vx = math.cos(angle)*velocity   # Calculating the X component of the speed
            vy = math.sin(angle)*velocity   # Calculating the Y component of the speed
            if abs(dx) < abs(vx):           # Reducing the X speed to the distance if the particle is close enough
                vx = dx
            if abs(dy) < abs(vy):           # Reducing the X speed to the distance if the particle is close enough
                vy = dy
            new_x = x + vx
            new_y = y + vy
            new_position = (new_x, new_y)
            self.position = new_position
            return
        return
        


class Food:
    def __init__(self, nutrition, position=(0.,0.)):
        self.nutrition = nutrition
        self.position = position
