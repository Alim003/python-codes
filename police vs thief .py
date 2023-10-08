import random

def police_vs_thief(grid, max_distance):
    num_rows = len(grid)
    num_cols = len(grid[0])
    caught_count = 0
    police = []
    thieves = []

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 'P':
                police.append([i, j])
            elif grid[i][j] == 'T':
                thieves.append([i, j])

    alt_grid = [row[:] for row in grid]
    is_thief_caught = [1] * len(thieves)

    for i in range(len(police)):
        for p in range(len(thieves)):
            if abs(police[i][0] - thieves[p][0]) <= max_distance and abs(police[i][1] - thieves[p][1]) == 0 and is_thief_caught[p] == 1:
                is_thief_caught[p] = 0
                alt_grid[thieves[p][0]][thieves[p][1]] = 'C'
                caught_count += 1
                break
            elif abs(police[i][1] - thieves[p][1]) <= max_distance and abs(police[i][0] - thieves[p][0]) == 0 and is_thief_caught[p] == 1:
                is_thief_caught[p] = 0
                alt_grid[thieves[p][0]][thieves[p][1]] = 'C'
                caught_count += 1
                break

    return caught_count

# Function to generate a random 2D grid of police and thieves.
def generate_random_grid(rows, cols):
    return [['P' if random.choice([True, False]) else 'T' for _ in range(cols)] for _ in range(rows)]

# Set the dimensions of the random grid and generate it.
rows = 4
cols = 4
city_grid = generate_random_grid(rows, cols)

max_distance = 2

caught_thieves = police_vs_thief(city_grid, max_distance)
print(f"Number of thieves caught: {caught_thieves}")
