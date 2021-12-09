import fileinput

lines = [line.strip() for line in fileinput.input()]
positions = sorted([int(crab) for crab in lines[0].split(',')])

def partOne():
  median = positions[len(positions) // 2]
  return sum(abs(position - median) for position in positions)

def partTwo():
  lowestPosition = min(positions)
  highestPosition = max(positions)
  minFuel = None
  for align in range(lowestPosition, highestPosition):
    total = 0
    for position in positions:
      dist = abs(position - align)
      total += dist * (dist + 1) // 2
    if minFuel == None or total < minFuel:
      minFuel = total
  return minFuel

print('Part one:', partOne())
print('Part two:', partTwo())