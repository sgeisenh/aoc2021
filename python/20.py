import fileinput

lines = [line.strip() for line in fileinput.input()]

algorithm = lines[0]

lit = set()
for i in range(2, len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] == '#':
      lit.add((i, j))

def getMinRow(lit):
  return min(row for row, col in lit)

def getMaxRow(lit):
  return max(row for row, col in lit)

def getMinCol(lit):
  return min(col for row, col in lit)

def getMaxCol(lit):
  return max(col for row, col in lit)

olr = getMinRow(lit)
omr = getMaxRow(lit)
olc = getMinCol(lit)
omc = getMaxCol(lit)
ds = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

def enhance(lit, i):
  global olr, omr, olc, omc
  result = set()
  lr = getMinRow(lit) - 30
  mr = getMaxRow(lit) + 30
  lc = getMinCol(lit) - 30
  mc = getMaxCol(lit) + 30
  for row in range(lr, mr):
    for col in range(lc, mc):
      index_str = ''
      for dr, dc in ds:
        if (row + dr, col + dc) in lit:
          index_str += '1'
        else:
          index_str += '0'
      idx = int(index_str, 2)
      if algorithm[idx] == '#':
        result.add((row, col))
  if i % 2 == 1:
    result = set([(r, c) for r, c in result if olr - 5 <= r <= omr + 5 and olc - 5 <= c <= omc + 5])
    olr = getMinRow(result)
    omr = getMaxRow(result)
    olc = getMinCol(result)
    omc = getMaxCol(result)

  return result

for i in range(50):
  lit = enhance(lit, i)
  if i == 1:
    print('Part one:', len(lit))

print('Part two:', len(lit))