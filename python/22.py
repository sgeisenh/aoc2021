import fileinput
import copy

lines = [line.strip() for line in fileinput.input()]

steps = []
for line in lines:
  comps = line.split(' ')
  ison = comps[0] == 'on'
  coords = comps[1].split(',')
  x, y, z = tuple([[int(num) for num in coord.split('=')[1].split('..')] for coord in coords])
  x1, x2 = x
  y1, y2 = y
  z1, z2 = z
  steps.append((ison, x1, x2, y1, y2, z1, z2))

cubes = set()
for step in steps:
  ison, x1, x2, y1, y2, z1, z2 = step
  if x1 > 50 or x2 < -50 or y1 > 50 or y2 < -50 or z1 > 50 or z2 < -50:
    continue
  for x in range(x1, x2 + 1):
    for y in range(y1, y2 + 1):
      for z in range(z1, z2 + 1):
        if ison:
          cubes.add((x, y, z))
        elif (x, y, z) in cubes:
          cubes.remove((x, y, z))

print('Part one:', len([(x, y, z) for (x, y, z) in cubes if -50 <= x <= 50 and -50 <= y <= 50 and -50 <= z <= 50]))

def intersection(c1, c2):
  x11, x12, y11, y12, z11, z12 = c1
  x21, x22, y21, y22, z21, z22 = c2
  x31, x32 = max(x11, x21), min(x12, x22)
  y31, y32 = max(y11, y21), min(y12, y22)
  z31, z32 = max(z11, z21), min(z12, z22)
  return x31, x32, y31, y32, z31, z32

def cuboidVolume(c):
  x1, x2, y1, y2, z1, z2 = c
  return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

cuboids = {}
for step in steps:
  ison, x1, x2, y1, y2, z1, z2 = step
  newc = x1, x2, y1, y2, z1, z2
  new_cuboids = copy.deepcopy(cuboids)
  for cbd, count in cuboids.items():
    ix1, ix2, iy1, iy2, iz1, iz2 = intersection(newc, cbd)
    if ix1 <= ix2 and iy1 <= iy2 and iz1 <= iz2:
      icbd = ix1, ix2, iy1, iy2, iz1, iz2
      if icbd not in new_cuboids:
        new_cuboids[icbd] = -count
      else:
        new_cuboids[icbd] -= count
  if ison:
    if newc not in new_cuboids:
      new_cuboids[newc] = 1
    else:
      new_cuboids[newc] += 1
  cuboids = new_cuboids

totalVol = 0
for cuboid, count in cuboids.items():
  totalVol += count * cuboidVolume(cuboid)

print('Part two:', totalVol)