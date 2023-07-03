import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_grid(grid):
    updated_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            live_neighbors = np.sum(grid[max(0, i-1):min(i+2, grid.shape[0]),
                                        max(0, j-1):min(j+2, grid.shape[1])]) - grid[i, j]
            if grid[i, j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    updated_grid[i, j] = 0
            else:
                if live_neighbors == 3:
                    updated_grid[i, j] = 1
    grid[:] = updated_grid[:]

def animate(frame):
    update_grid(grid)
    img.set_array(grid)
    return [img]

grid = np.random.randint(2, size=(80, 80))
plt.style.use('dark_background')
plt.title("Conway's Game of Life")
plt.xticks([])
plt.yticks([])
img = plt.imshow(grid, cmap='binary')
ani = animation.FuncAnimation(plt.gcf(), animate, frames=100, interval=100, blit=True)
plt.show()
