import fileinput

arr = [int(line.strip()) for line in fileinput.input()]

def partOne(depths):
  count = 0
  for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
      count += 1
  return count

def partTwo(depths):
  count = 0
  for i in range(3, len(arr)):
    if arr[i] > arr[i - 3]:
      count += 1
  return count

print('Part one:', partOne(arr))
print('Part two:', partTwo(arr))