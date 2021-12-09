import fileinput

lines = [line.strip() for line in fileinput.input()]
bits = len(lines[0])

def partOne(numbers):
  counts = [(sum(1 for number in numbers if number[i] == '0'), sum(1 for number in numbers if number[i] == '1')) for i in range(bits)]

  gamma = int(''.join(['1' if ones > zeros else '0' for (zeros, ones) in counts]), 2)
  epsilon = int(''.join(['0' if ones > zeros else '1' for (zeros, ones) in counts]), 2)

  return gamma * epsilon

def oneMostFrequent(numbers, i):
  zeros = 0
  ones = 0
  for number in numbers:
    if number[i] == '0':
      zeros += 1
    else:
      ones += 1
  return ones >= zeros

def partTwo(numbers):
  oxy = numbers[:]
  co2 = numbers[:]

  for i in range(bits):
    if len(oxy) > 1:
      bit = '1' if oneMostFrequent(oxy, i) else '0'
      oxy = [line for line in oxy if line[i] == bit]
    if len(co2) > 1:
      bit = '0' if oneMostFrequent(co2, i) else '1'
      co2 = [line for line in co2 if line[i] == bit]
    
  return (int(oxy[0], 2) * int(co2[0], 2))

print('Part one:', partOne(lines))
print('Part two:', partTwo(lines))