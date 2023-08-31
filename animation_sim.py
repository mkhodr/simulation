from definitions import Arena, visualize_quadtree
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.colors import Normalize
import numpy as np


arena = Arena(x=500, y=500 ,particle_no=500, food_no=11200)
times = []

fig, ax = plt.subplots()
cmap = plt.get_cmap('Blues')

def animate(frames):
    ax.clear()

    start_time = time.time()
    arena.move_particles(arena.closest_food_map)
    a = arena.check_collision()
    end_time = time.time()

    ##Visualize quadtree
    # visualize_quadtree(arena.quadtree, ax)

    ## Particles 
    particle_positions = [(p.position.x, p.position.y, p.size) for p in arena.particles]
    if particle_positions:
        particle_positions_x, particle_positions_y, particle_size = zip(*particle_positions)
        norm = Normalize(vmin=min(particle_size), vmax=max(particle_size))
        particle_colors = cmap(norm(particle_size))
        scatter = ax.scatter(particle_positions_x, particle_positions_y, marker='h', c=particle_colors , s=np.array(particle_size)*4)
    ## Foods
    food_positions = [(f.position.x, f.position.y, f.nutrition) for f in arena.foods]
    if food_positions:
        food_positions_x, food_positions_y, food_nutrition = zip(*food_positions)
        ax.scatter(food_positions_x, food_positions_y, marker='1', c='red', s=np.array(food_nutrition)*2)

    times.append(end_time-start_time)
    print(end_time-start_time, max(times), np.average(times))

    if not arena.foods:
        plt.close()
    

anim = FuncAnimation(fig, animate , interval=10, frames=150, )
# video = anim.save(f'{arena.particle_no}p{arena.food_no}ns.gif', writer=PillowWriter(fps=15))
plt.show()