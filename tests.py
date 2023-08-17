from definitions import Arena
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

arena = Arena()

# spawning test particle
arena.spawn_particle(5, (40,12))

# spwaning test food
arena.spawn_food(20, (1.12,99.77))

fig, ax = plt.subplots()

def plot():
    ax.set_xlim(0, arena.x)
    ax.set_ylim(0, arena.y)
    # ax.clear()
    # arena.update_particles()
    for particle in arena.particles:
        ax.plot(particle.position[0], particle.position[1], 'bo', markersize=particle.size)
        # print(particle.position, particle.velocity)

    for food in arena.foods:
        ax.plot(food.position[0], food.position[1], 'ro', markersize=food.nutrition)
        # print(food.position, food.nutrition)


def move():
    particle = arena.particles[0]
    foods = arena.foods

    closest_food = min(foods, key=lambda food: math.sqrt((food.position[0] - particle.position[0])**2 + (food.position[1] - particle.position[1])**2))

    x, y = particle.position
    fx, fy = closest_food.position
    print(f'particle {x,y} | food {fx,fy}')

    dx = x - fx # distance in X axis
    dy = y - fy # distance in Y axis
    print(f'distance x {dx} | distance y {dy}')
    if dx == 0 and dy == 0:
        return

    angle = math.atan(abs(dy)/abs(dx)) # in radians
    print(f'angle in degrees = {math.degrees(angle)} | in radians = {angle}')


    angle_noabs = math.atan(dy/dx) # in radians
    print(f'no abs angle in degrees = {math.degrees(angle_noabs)} | in radians = {angle_noabs}')

    vx = math.cos(angle)*particle.velocity
    vy = math.sin(angle)*particle.velocity
    vx_noabs = math.cos(angle_noabs)*particle.velocity
    vy_noabs = math.sin(angle_noabs)*particle.velocity
    print(f'particle velocity: {particle.velocity}')
    print(f'vX component: {vx} | vY component: {vy}')
    print(f'vX component: {vx_noabs} | vY component: {vy_noabs}')
    if dx < vx:
        vx = abs(dx)
        # print(f'speed exceeds distance - new speed {xspeed}')
    if dy < vy:
        vy = abs(dy)
    new_x = x - vx if dx > 0 else (x + vx if dx < 0 else x)
    new_y = y - vy if dy > 0 else (y + vy if dy < 0 else y)
    new_x_noabs = x - vx_noabs if dx > 0 else (x + vx_noabs if dx < 0 else x)
    new_y_noabs = y - vy_noabs if dy > 0 else (y + vy_noabs if dy < 0 else y)
    print(new_x, new_y)
    print(new_x_noabs, new_y_noabs)
    particle.position = (new_x, new_y)

    print(particle.position)
for i in range(100):
    move()
# for food in arena.foods:
#     print(food.position, food.nutrition)
# for particle in arena.particles:
#     print(particle.position, particle.velocity, particle.size)