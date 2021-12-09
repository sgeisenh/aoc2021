import fileinput

lines = [line.strip() for line in fileinput.input()]

def partOne(lines):
  lines_dict = {}

  for line in lines:
    p1, p2 = line.split(' -> ')
    x1, y1 = [int(x) for x in p1.split(',')]
    x2, y2 = [int(x) for x in p2.split(',')]
    if x1 == x2:
      lo = min(y1, y2)
      hi = max(y1, y2)
      for y in range(lo, hi + 1):
        if (x1, y) not in lines_dict:
          lines_dict[(x1, y)] = 1
        else:
          lines_dict[(x1, y)] += 1
    elif y1 == y2:
      lo = min(x1, x2)
      hi = max(x1, x2)
      for x in range(lo, hi + 1):
        if (x, y1) not in lines_dict:
          lines_dict[(x, y1)] = 1
        else:
          lines_dict[(x, y1)] += 1

  count = 0
  for num in lines_dict.values():
    if num > 1:
      count += 1

  return count

def partTwo(lines):
  lines_dict = {}

  for line in lines:
    p1, p2 = line.split(' -> ')
    x1, y1 = [int(x) for x in p1.split(',')]
    x2, y2 = [int(x) for x in p2.split(',')]
    if x1 == x2:
      lo = min(y1, y2)
      hi = max(y1, y2)
      for y in range(lo, hi + 1):
        if (x1, y) not in lines_dict:
          lines_dict[(x1, y)] = 1
        else:
          lines_dict[(x1, y)] += 1
    elif y1 == y2:
      lo = min(x1, x2)
      hi = max(x1, x2)
      for x in range(lo, hi + 1):
        if (x, y1) not in lines_dict:
          lines_dict[(x, y1)] = 1
        else:
          lines_dict[(x, y1)] += 1
    else:
      slope = None
      left = None
      right = None
      if x1 < x2:
        left = x1, y1
        right = x2, y2
        if y1 < y2:
          slope = 1
        else:
          slope = -1
      else:
        left = x2, y2
        right = x1, y1
        if y2 < y1:
          slope = 1
        else:
          slope = -1
      for i in range(right[0] + 1 - left[0]):
        pos = (left[0] + i, left[1] + i * slope)
        if pos not in lines_dict:
          lines_dict[pos] = 1
        else:
          lines_dict[pos] += 1

  count = 0
  for num in lines_dict.values():
    if num > 1:
      count += 1

  return count

print('Part one:', partOne(lines))
print('Part two:', partTwo(lines))