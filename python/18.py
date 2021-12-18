import fileinput
from itertools import combinations

def parseElem(s):
  if s[0] != '[':
    i = 0
    num = ''
    while s[i].isdigit():
      num += s[i]
      i += 1
    return int(num), s[i:]
  else:
    return parsePair(s)

def parsePair(s):
  assert(s[0] == '[')
  left, s = parseElem(s[1:])
  assert(s[0] == ',')
  right, s = parseElem(s[1:])
  assert(s[0] == ']')
  return (left, right), s[1:]

pairs = [parsePair(line.strip())[0] for line in fileinput.input()]

def addToRight(value, elem):
  if isinstance(elem, int):
    return elem + value
  else:
    left, right = elem
    return (left, addToRight(value, right))

def addToLeft(value, elem):
  if isinstance(elem, int):
    return elem + value
  else:
    left, right = elem
    return (addToLeft(value, left), right)

def explodeHelper(pair, level):
  left, right = pair
  if level == 4:
    return 0, left, right
  else:
    if not isinstance(left, int):
      newLeft, addLeft, addRight = explodeHelper(left, level + 1)
      if newLeft != left:
        return (newLeft, addToLeft(addRight or 0, right)), addLeft, None
    if not isinstance(right, int):
      newRight, addLeft, addRight = explodeHelper(right, level + 1)
      if newRight != right:
        return (addToRight(addLeft or 0, left), newRight), None, addRight
    return pair, None, None

def explode(pair):
  newPair, _, _ = explodeHelper(pair, 0)
  return newPair, pair != newPair

def splitElem(elem):
  if isinstance(elem, int):
    if elem >= 10:
      left = elem // 2
      right = (elem + 1) // 2
      assert(left + right == elem)
      return (left, right), True
    else:
      return elem, False
  else:
    left, right = elem
    left, didSplitL = splitElem(left)
    if didSplitL:
      return (left, right), True
    right, didSplitR = splitElem(right)
    return (left, right), didSplitR

def split(pair):
  left, right = pair
  left, didSplitL = splitElem(left)
  if didSplitL:
    return (left, right), True
  right, didSplitR = splitElem(right)
  return (left, right), didSplitR

def reducePair(pair):
  while True:
    exploded_once = False
    while True:
      pair, did_explode = explode(pair)
      if did_explode:
        exploded_once = True
      else:
        break
    pair, did_split = split(pair)
    if did_split:
      return reducePair(pair)
    if not exploded_once:
      break
  return pair

def addPairs(left, right):
  return reducePair((left, right))

def magnitude(elem):
  if isinstance(elem, int):
    return elem
  else:
    left, right = elem
    return 3 * magnitude(left) + 2 * magnitude(right)

acc = pairs[0]
for pair in pairs[1:]:
  acc = addPairs(acc, pair)

print('Part one:', magnitude(acc))

maxMag = None
for a, b in combinations(pairs, 2):
  mag = magnitude(addPairs(a, b))
  if maxMag == None or mag > maxMag:
    maxMag = mag

print('Part two:', maxMag)