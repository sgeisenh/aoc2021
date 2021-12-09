import fileinput

lines = [line.strip() for line in fileinput.input()]

def partOne(directions):
  hor = 0
  depth = 0
  for line in lines:
    splits = line.split(' ')
    if splits[0] == 'forward':
      hor += int(splits[1])
    if splits[0] == 'down':
      depth += int(splits[1])
    if splits[0] == 'up':
      depth -= int(splits[1])
  return hor * depth
  
def partTwo(directions):
  hor = 0
  depth = 0
  aim = 0
  for line in lines:
    splits = line.split(' ')
    if splits[0] == 'forward':
      hor += int(splits[1])
      depth += aim * int(splits[1])
    if splits[0] == 'down':
      aim += int(splits[1])
    if splits[0] == 'up':
      aim -= int(splits[1])
  return hor * depth

print('Part one:', partOne(lines))
print('Part two:', partTwo(lines))