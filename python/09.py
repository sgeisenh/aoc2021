import fileinput
import heapq

lines = [line.strip() for line in fileinput.input()]

def partOne():
  total = 0
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      val = int(lines[i][j])
      if all(ni < 0 or nj < 0 or ni >= len(lines) or nj >= len(lines[0]) or int(lines[ni][nj]) > val for ni, nj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]):
        total += val + 1
  return total

def partTwo():
  largest = []
  unvisited = set((r, c) for r in range(len(lines)) for c in range(len(lines[0])))

  def visit(r, c, acc):
    if (r, c) not in unvisited:
      return acc
    if lines[r][c] == '9':
      unvisited.remove((r, c))
      return acc
    unvisited.remove((r, c))
    acc = acc + 1
    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
      acc = visit(nr, nc, acc)
    return acc

  while len(unvisited) > 0:
    for r, c in unvisited:
      break
    size = visit(r, c, 0) 
    heapq.heappush(largest, size)
    if len(largest) > 3:
      heapq.heappop(largest)

  product = 1
  for elem in largest:
    product *= elem
  return product

print('Part one:', partOne())
print('Part two:', partTwo())