import fileinput
import copy

grid = [[c for c in line.strip()] for line in fileinput.input()]

wasMovement = True
step = 0
while wasMovement:
  wasMovement = False
  newGrid = copy.deepcopy(grid)
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == '>':
        if grid[i][(j + 1) % len(grid[i])] == '.':
          newGrid[i][j] = '.'
          newGrid[i][(j + 1) % len(grid[i])] = '>'
          wasMovement = True
  grid = newGrid
  newGrid = copy.deepcopy(grid)
  for j in range(len(grid[0])):
    for i in range(len(grid)):
      if grid[i][j] == 'v':
        if grid[(i + 1) % len(grid)][j] == '.':
          newGrid[i][j] = '.'
          newGrid[(i + 1) % len(grid)][j] = 'v'
          wasMovement = True
  grid = newGrid
  step += 1

print('Part one:', step)