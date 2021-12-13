import fileinput

lines = [line.strip() for line in fileinput.input()]

dotpositions = set()

for line in lines:
  if line == '' or line.startswith('fold'):
    continue
  x, y = line.split(',')
  dotpositions.add((int(x), int(y)))

def foldX(positions, foldat):
  newpositions = set()
  for x, y in positions:
    newx = x if x <= foldat else 2 * foldat - x
    newpositions.add((newx, y))
  return newpositions

def foldY(positions, foldat):
  newpositions = set()
  for x, y in positions:
    newy = y if y <= foldat else 2 * foldat - y
    newpositions.add((x, newy))
  return newpositions

firstfold = True
for line in lines:
  if line.startswith('fold'):
    foldat = int(line.split('=')[1])
    if line.startswith('fold along y'):
      dotpositions = foldY(dotpositions, foldat)
    else:
      dotpositions = foldX(dotpositions, foldat)
    if firstfold:
      print('Part one:', len(dotpositions))
      firstfold = False

minx = None
maxx = None
miny = None
maxy = None
for x, y in dotpositions:
  if minx == None or x < minx:
    minx = x
  if maxx == None or x > maxx:
    maxx = x
  if miny == None or y < miny:
    miny = y
  if maxy == None or y > maxy:
    maxy = y

output = ''
for y in range(miny, maxy + 1):
  line = ''
  for x in range(minx, maxx + 1):
    if (x, y) in dotpositions:
      line += '#'
    else:
      line += '.'
  output += line + '\n'
    
print('ASCII Part two:')
print(output)