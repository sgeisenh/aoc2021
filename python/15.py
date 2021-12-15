import fileinput
import heapq

lines = [[int(c) for c in line.strip()] for line in fileinput.input()]
biglines = [[] for _ in range(5 * len(lines))]
for i in range(5):
  for j in range(5):
    for r in range(len(lines)):
      for c in range(len(lines[0])):
        newval = lines[r][c] + i + j
        if newval > 9:
          newval -= 9
        biglines[i * len(lines) + r].append(newval)

def minDist(grid):
  Q = [(0, (0, 0))]
  D = {}

  while Q:
    dist, (r, c) = heapq.heappop(Q)
    if (r, c) in D and dist > D[(r, c)]:
      continue
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nr = r + dr
      nc = c + dc
      if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        cost = dist + grid[nr][nc]
        if (nr, nc) not in D or cost < D[(nr, nc)]:
          D[(nr, nc)] = cost
          heapq.heappush(Q, (cost, (nr, nc)))

  return D[(len(grid) - 1, len(grid[0]) - 1)]

print('Part one:', minDist(lines))
print('Part two:', minDist(biglines))