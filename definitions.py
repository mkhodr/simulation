import math

class Arena:
    def __init__(self, x=50, y=45):
        self.particles = []
        self.foods = []
        self.grid = [[' ' for _ in range(x)] for _ in range(y)]
        self.x = x
        self.y = y

    def add_particle(self, Particle):
        self.particles.append(Particle)

    def add_food(self, Food):
        self.foods.append(Food)

    def display(self):
        for particle in self.particles:
            self.grid[particle.position[1]][particle.position[0]] = 'P'
        for food in self.foods:
            self.grid[food.position[1]][food.position[0]] = 'F'

        for row in self.grid:
            print(''.join(row))


class Particle:
    def __init__(self, size, hunger, position=(0,0)):
        self.size = size
        self.hunger = hunger
        self.position = position

    def feed(self):
        self.hunger -= 1
        if self.hunger <= 0:
            self.size += 1
            self.hunger = 10

    def move(self, foods):
        x,y = self.position
        closest_food = min(foods, key=lambda food: math.sqrt((food.position[0] - x)**2 + (food.position[1] - y)**2))
        fx,fy = closest_food.position
        if x > fx:
            x -= 1
        else:
            x =+ 1
        if y > fy:
            y -= 1
        else:
            y += 1
        self.position = (x,y)
        

    # def seek_food(self):
    #     if Arena.foods

class Food:
    def __init__(self, nutrition, position=(0,0)):
        self.nutrition = nutrition
        self.position = position


        
particle1 = Particle(5, 10, (20,20))
particle3 = Particle(5, 10, (45,40))
particle2 = Particle(1, 1, (12,12))
food1 = Food(2,(15,15))
food2 = Food(2,(35,35))

arena1 = Arena()

arena1.add_food(food1)
arena1.add_food(food2)
arena1.add_particle(particle1)
arena1.add_particle(particle2)
arena1.add_particle(particle3)

# arena1.display()
print(particle1.position)

for _ in range(10):
    for particle in arena1.particles:
        particle.move(arena1.foods)


arena1.display()
for particle in arena1.particles:
    print(particle.position)