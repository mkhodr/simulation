from definitions import Arena
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

# Initial Particles counter
particle_no = 500
# Initial Food counter
food_no = 5000


arena = Arena(x=1000, y=1000)
for _ in range(particle_no):
    arena.spawn_random_particle()
for _ in range(food_no):
    arena.spawn_random_food()
closest_food_dict = arena.update_closest_food()

times = []

fig, ax = plt.subplots()
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
def animate(frames):
    start_time = time.time()
    ax.clear()
    arena.move_particles(arena.closest_food_dict)
    a = arena.check_collision()
    particle_positions = np.array([p.position for p in arena.particles])
    food_positions = np.array([f.position for f in arena.foods])
    if arena.particles:
        ax.plot(particle_positions[: , 0], particle_positions[:, 1], 'bo', markersize=3)
    if arena.foods:
        ax.plot(food_positions[:, 0], food_positions[:, 1], 'ro', markersize=2)
    end_time = time.time()
    times.append(end_time-start_time)
    print(max(times), np.average(times))
    if not arena.foods:
        plt.close()


anim = FuncAnimation(fig, animate , interval=50, frames=300, )
video = anim.save(f'{particle_no}p{food_no}n.gif', writer=PillowWriter(fps=15))
plt.show()
  

