from definitions import Arena
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

arena = Arena()

# Initial Particles counter
particle_no = 10
# Initial Food counter
food_no = 150

for _ in range(particle_no):
    arena.spawn_random_particle()
for _ in range(food_no):
    arena.spawn_random_food()

closest_food_dict = arena.update_closest_food()
print(closest_food_dict)

fig, ax = plt.subplots()
def animate(frames):
    closest_food_dict = arena.update_closest_food()
    ax.set_xlim(0, arena.x)
    ax.set_ylim(0, arena.y)
    ax.clear()
    arena.move_particles(closest_food_dict)
    a = arena.check_collision()
    for particle in arena.particles:
        ax.plot(particle.position[0], particle.position[1], 'bo', markersize=particle.size)
    for food in arena.foods:
        ax.plot(food.position[0], food.position[1], 'ro', markersize=food.nutrition)

        


ani = FuncAnimation(fig, animate , interval=0, frames=100)

plt.show()