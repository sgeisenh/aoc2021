import fileinput

grid = [[int(c) for c in line.strip()] for line in fileinput.input()]

D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

steps = 0
total_flashes = 0
while True:
  for row in grid:
    for col in range(len(row)):
      row[col] += 1
  flash_coords = set()
  while any(any(col >= 10 for col in row) for row in grid):
    for r in range(len(grid)):
      for c in range(len(grid[r])):
        if grid[r][c] >= 10:
          for dr, dc in D:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] != 0:
              grid[nr][nc] += 1
          grid[r][c] = 0
          total_flashes += 1
          flash_coords.add((r, c))
  steps += 1
  if steps == 100:
    print('Part one:', total_flashes)
  if len(flash_coords) == 100:
    print('Part two:', steps)
    break