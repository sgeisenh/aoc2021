import fileinput

lines = [line.strip() for line in fileinput.input()]
output_values = [(line.split(' | ')[0].split(' '), line.split(' | ')[1].split(' ')) for line in lines]

def partOne():
  count = 0
  for patterns, digits in output_values:
    for digit in digits:
      l = len(digit)
      if l == 2 or l == 4 or l == 3 or l == 7:
        count += 1
  return count

def partTwo():
  total = 0
  for patterns, digits in output_values:
    zero_pattern = None
    one_pattern = None
    two_pattern = None
    three_pattern = None
    four_pattern = None
    five_pattern = None
    six_pattern = None
    seven_pattern = None
    eight_pattern = None
    nine_pattern = None

    for pattern in patterns:
      if len(pattern) == 2:
        one_pattern = sorted(pattern)
      if len(pattern) == 4:
        four_pattern = sorted(pattern)
      if len(pattern) == 3:
        seven_pattern = sorted(pattern)
      if len(pattern) == 7:
        eight_pattern = sorted(pattern)

    for pattern in patterns:
      if len(pattern) == 6:
        if len(set(one_pattern) & set(pattern)) == 1:
          six_pattern = sorted(pattern)

    for pattern in patterns:
      if len(pattern) == 6 and sorted(pattern) != six_pattern:
        if len(set(four_pattern) & set(pattern)) == 4:
          nine_pattern = sorted(pattern)
        else:
          zero_pattern = sorted(pattern)

    a = list(set(seven_pattern) - set(one_pattern))[0]
    b = list(set(zero_pattern) & set(four_pattern) - set(one_pattern))[0]
    c = list(set(eight_pattern) - set(six_pattern))[0]
    d = list(set(eight_pattern) - set(zero_pattern))[0]
    e = list(set(eight_pattern) - set(nine_pattern))[0]
    g = list(set(nine_pattern) - set(seven_pattern) - set(four_pattern))[0]
    f = list(set(eight_pattern) - set([a, b, c, d, e, g]))[0]
    two_pattern = sorted([a, c, d, e, g])
    three_pattern = sorted([a, c, d, f, g])
    five_pattern = sorted([a, b, d, f, g])

    output = ''
    for digit in digits:
      s = sorted(digit)
      if s == zero_pattern:
        output += '0'
      elif s == one_pattern:
        output += '1'
      elif s == two_pattern:
        output += '2'
      elif s == three_pattern:
        output += '3'
      elif s == four_pattern:
        output += '4'
      elif s == five_pattern:
        output += '5'
      elif s == six_pattern:
        output += '6'
      elif s == seven_pattern:
        output += '7'
      elif s == eight_pattern:
        output += '8'
      elif s == nine_pattern:
        output += '9'
      else:
        assert(False)
    total += int(output)

  return total

print('Part one:', partOne())
print('Part two:', partTwo())