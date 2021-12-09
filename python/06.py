import fileinput

lines = [line.strip() for line in fileinput.input()]
fishes = [int(fish) for fish in lines[0].split(',')]

D = {}
def createdFish(fish, days):
  if days == 0:
    return 1
  elif (fish, days) in D:
    return D[(fish, days)]
  
  if fish == 0:
    result = createdFish(8, days - 1) + createdFish(6, days - 1)
    D[(fish, days)] = result
    return result
  else:
    result = createdFish(fish - 1, days - 1)
    D[(fish, days)] = result
    return result

def partOne():
  total = 0
  for fish in fishes:
    total += createdFish(fish, 80)
  return total

def partTwo():
  total = 0
  for fish in fishes:
    total += createdFish(fish, 256)
  return total

print('Part one:', partOne())
print('Part two:', partTwo())