import fileinput

lines = [line.strip() for line in fileinput.input()]

closing = {')': (3, '('), ']': (57, '['), '}': (1197, '{'), '>': (25137, '<')}
opening = {'(': 1, '[': 2, '{': 3, '<': 4}

def partOne():
  total = 0
  for line in lines:
    stack = []
    for c in line:
      if c in closing:
        if stack == [] or stack[-1] != closing[c][1]:
          total += closing[c][0]
          break
        else:
          stack.pop()
      else:
        stack.append(c)
  return total
      
def partTwo():
  scores = []
  for line in lines:
    stack = []
    corrupted = False
    for c in line:
      if c in closing:
        if stack == [] or stack[-1] != closing[c][1]:
          corrupted = True
          break
        else:
          stack.pop()
      else:
        stack.append(c)
    if not corrupted:
      total = 0
      for c in stack[-1::-1]:
        total = 5 * total + opening[c]
      scores.append(total)
  scores.sort()
  return scores[len(scores) // 2]

print('Part one:', partOne())
print('Part two:', partTwo())