from definitions import Arena
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Initial Particles counter
particle_no = 100
# Initial Food counter
food_no = 10000


arena = Arena()
for _ in range(particle_no):
    arena.spawn_random_particle()
for _ in range(food_no):
    arena.spawn_random_food()
closest_food_dict = arena.update_closest_food()

times = []

fig, ax = plt.subplots()
def animate(frames):
    start_time = time.time()
    ax.set_xlim(0, arena.x)
    ax.set_ylim(0, arena.y)
    ax.clear()
    arena.move_particles(arena.closest_food_dict)
    a = arena.check_collision()
    # particle_positions = np.array([p.position for p in arena.particles])
    # food_positions = np.array([f.position for f in arena.foods])
    # if arena.particles:
    #     ax.plot(particle_positions[: , 0], particle_positions[:, 1], 'bo', markersize=3)
    # if arena.foods:
    #     ax.plot(food_positions[:, 0], food_positions[:, 1], 'ro', markersize=2)
    # for particle in arena.particles:
    #     ax.plot(particle.position[0], particle.position[1], 'bo', markersize=particle.size)
    # for food in arena.foods:
    #     ax.plot(food.position[0], food.position[1], 'ro', markersize=food.nutrition)
    end_time = time.time()
    times.append(end_time-start_time)
    print(max(times), np.average(times))


ani = FuncAnimation(fig, animate , interval=0, frames=100)
plt.show()