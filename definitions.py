import math
from random import randint, uniform, choices
import string

class Arena:
    def __init__(self, x=200, y=200):
        self.particles = []
        self.foods = []
        # self.grid = [['   ' for _ in range(0,x)] for _ in range(0,y)]
        self.x = x
        self.y = y

    def add_particle(self, Particle):
        self.particles.append(Particle)

    def add_food(self, Food):
        self.foods.append(Food)

    # def render(self):
    #     self.grid = [['   ' for _ in range(0,self.x)] for _ in range(0,self.y)]
    #     for particle in self.particles:
    #         self.grid[particle.position[1]][particle.position[0]] = f'P{particle.name}'
    #     for food in self.foods:
    #         self.grid[food.position[1]][food.position[0]] = f'F'
    #     for row in self.grid:
    #         print(''.join(row))

    def check_collision(self, particle):
        for food in self.foods:
            if round(particle.position[0]) == round(food.position[0]) and round(particle.position[1]) == round(food.position[1]):
                self.foods.remove(food)
                particle.hunger += food.nutrition

    def random_position(self):
        random_position = (round(uniform(0, self.x-1), 1), round(uniform(0, self.y-1), 1))
        return random_position

    def update_particles(self):
        for particle in self.particles:
            particle.move(self.foods)
            self.check_collision(particle)

    def respawn_food(self):
        random_position = self.random_position()
        nutrition_value = randint(1,3)
        food = Food(nutrition_value, random_position)
        self.add_food(food)

    def spawn_particles(self):
        name = ''.join(choices(string.ascii_uppercase + string.digits, k=4))
        random_position = self.random_position()
        size = randint(1,5)
        hunger = 10
        self.add_particle(Particle(name, size, hunger, random_position))



class Particle:
    def __init__(self, name, size, hunger, position=(0.,0.)):
        self.name = name
        self.size = size
        self.hunger = hunger
        self.velocity = int(5/size)
        self.position = position
        

    def feed(self):
        self.hunger -= 1
        if self.hunger <= 0:
            self.size += 1
            self.hunger = 10

    def move(self, foods):
        x,y = self.position
        velocity = self.velocity
        try:
            closest_food = min(foods, key=lambda food: math.sqrt((food.position[0] - x)**2 + (food.position[1] - y)**2))
            fx,fy = closest_food.position #food x and y
            dx = x - fx # distance in X axis
            dy = y - fy # distance in Y axis
            # vector = (dx, dy)
            angle = math.atan(abs(dy)/abs(dx)) # in radians
            vx = math.cos(angle)*velocity
            vy = math.sin(angle)*velocity
            # distance = math.sqrt(dx**2 + dy**2) # distance between the 2 points
            if dx < vx:
                vx = abs(dx)
                # print(f'speed exceeds distance - new speed {xspeed}')
            if dy < vy:
                vy = abs(dy)
                # print(f'speed exceeds distance - new speed {yspeed}')
            new_x = x - vx if dx > 0 else (x + vx if dx < 0 else x)
            new_y = y - vy if dy > 0 else (y + vy if dy < 0 else y)
            new_position = (round(new_x, 1), round(new_y, 1))
            self.position = new_position
            return new_position
        except:
            return

        # try:
        #     closest_food = min(foods, key=lambda food: math.sqrt((food.position[0] - x)**2 + (food.position[1] - y)**2))
        #     fx,fy = closest_food.position
        #     dx = x - fx 
        #     dy = y - fy
        #     distance = math.sqrt(dx**2 + dy**2)
        #     if distance == 0:
        #         return
        #     if dx < xspeed:
        #         xspeed = abs(dx)
        #         # print(f'speed exceeds distance - new speed {xspeed}')
        #     if dy < yspeed:
        #         yspeed = abs(dy)
        #         # print(f'speed exceeds distance - new speed {yspeed}')
        #     new_x = x - xspeed if dx > 0 else (x + xspeed if dx < 0 else x)
        #     new_y = y - yspeed if dy > 0 else (y + yspeed if dy < 0 else y)
        #     new_position = (new_x, new_y)
        #     self.position = new_position
        #     return new_position
        # except:
        #     return


class Food:
    def __init__(self, nutrition, position=(0.,0.)):
        self.nutrition = nutrition
        self.position = position
