import fileinput

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

def doIntersect(c1, c2):
  x11, x12, y11, y12, z11, z12 = c1
  x21, x22, y21, y22, z21, z22 = c2
  return not (x11 > x22 or x21 > x12 or y11 > y22 or y21 > y12 or z11 > z22 or z21 > z12)

def remove(c1, c2):
  x11, x12, y11, y12, z11, z12 = c1
  x21, x22, y21, y22, z21, z22 = c2
  x31, x32 = max(x11, x21), min(x12, x22)
  y31, y32 = max(y11, y21), min(y12, y22)
  z31, z32 = max(z11, z21), min(z12, z22)
  result = [(x11, x12, y11, y31 - 1, z11, z12), # bottom
            (x11, x12, y32 + 1, y12, z11, z12), # top
            (x11, x31 - 1, y31, y32, z11, z12), # left
            (x32 + 1, x12, y31, y32, z11, z12), # right
            (x31, x32, y31, y32, z11, z31 - 1), # front
            (x31, x32, y31, y32, z32 + 1, z12)] # back
  result = [(x1, x2, y1, y2, z1, z2) for (x1, x2, y1, y2, z1, z2) in result if x1 <= x2 and y1 <= y2 and z1 <= z2]
  return result
  
def cuboidVolume(c):
  x1, x2, y1, y2, z1, z2 = c
  return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

def stepVolume(steps):
  cuboids = []
  for step in steps:
    ison, x1, x2, y1, y2, z1, z2 = step
    newc = x1, x2, y1, y2, z1, z2
    newcuboids = []
    for cuboid in cuboids:
      if doIntersect(cuboid, newc):
        for subc in remove(cuboid, newc):
          newcuboids.append(subc)
      else:
        newcuboids.append(cuboid)
    if ison:
      newcuboids.append(newc)
    cuboids = newcuboids

  totalVol = 0
  for cuboid in cuboids:
    totalVol += cuboidVolume(cuboid)
  return totalVol

print('Part one:', stepVolume([(ison, x1, x2, y1, y2, z1, z2) for (ison, x1, x2, y1, y2, z1, z2) in steps if not(x1 > 50 or x2 < -50 or y1 > 50 or y2 < -50 or z1 > 50 or z2 < -50)]))
print('Part two:', stepVolume(steps))