import fileinput
from itertools import product, combinations
from collections import deque

lines = [line.strip() for line in fileinput.input()]

scanners = []
curr_scanner = []
for line in lines:
  if line.startswith('---'):
    continue
  if line == '':
    scanners.append(curr_scanner)
    curr_scanner = []
  else:
    x, y, z = [int(elem) for elem in line.split(',')]
    curr_scanner.append((x, y, z))

scanners.append(curr_scanner)

oriented_scanners = [None for _ in scanners]
oriented_scanners[0] = scanners[0]
scanner_locations = [None for _ in scanners]
scanner_locations[0] = (0, 0, 0)

facings = ['forward', 'back', 'up', 'down', 'left', 'right']
rotations = [0, 1, 2, 3]

def generateRelative(scanner):
  result = [{} for _ in scanner]
  for i in range(len(scanner)):
    for j in range(len(scanner)):
      if i != j:
        x1, y1, z1 = scanner[i]
        x2, y2, z2 = scanner[j]
        result[i][(x1 - x2, y1 - y2, z1 - z2)] = j
  return result

def applyFacing(facing, scanner):
  if facing == 'forward':
    return scanner
  elif facing == 'back':
    return [(-x, y, -z) for x, y, z in scanner]
  elif facing == 'up':
    return [(x, -z, y) for x, y, z in scanner]
  elif facing == 'down':
    return [(x, z, -y) for x, y, z in scanner]
  elif facing == 'left':
    return [(z, y, -x) for x, y, z in scanner]
  elif facing == 'right':
    return [(-z, y, x) for x, y, z in scanner]
  assert(False)

def applyRotation(rotation, scanner):
  if rotation == 0:
    return scanner
  rotated = [(-y, x, z) for x, y, z in scanner]
  return applyRotation(rotation - 1, rotated)

def findOverlapping(i):
  assert(oriented_scanners[i] != None)
  relative = generateRelative(oriented_scanners[i])
  for j in range(len(scanners)):
    if i == j or oriented_scanners[j] != None:
      continue
    for facing, rotation in product(facings, rotations):
      oriented = applyRotation(rotation, applyFacing(facing, scanners[j]))
      orientRelative = generateRelative(oriented)
      for sd in relative:
        for od in orientRelative:
          overlap = sd.keys() & od.keys()
          if len(overlap) >= 11:
            for k in overlap:
              x1, y1, z1 = oriented_scanners[i][sd[k]]
              x2, y2, z2 = oriented[od[k]]
              break
            oriented_scanners[j] = [(x + x1 - x2, y + y1 - y2, z + z1 - z2) for x, y, z in oriented]
            scanner_locations[j] = (x2 - x1, y2 - y1, z2 - z1)
            if j not in tried:
              toTry.append(j)
              tried.add(j)

tried = set([0])
toTry = deque([0])
while toTry:
  i = toTry.popleft()
  findOverlapping(i)

beacons = set()
for s in oriented_scanners:
  for p in s:
    beacons.add(p)
print('Part one:', len(beacons))

def manDist(left, right):
  x1, y1, z1 = left
  x2, y2, z2 = right
  return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)

print('Part two:', max(manDist(left, right) for left, right in combinations(scanner_locations, 2)))
