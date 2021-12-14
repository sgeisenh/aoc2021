import fileinput
from collections import defaultdict
import copy

lines = [line.strip() for line in fileinput.input()]

template = None
rules = {}
for line in lines:
  if '->' in line:
    pair, c = [elem.strip() for elem in line.split(' -> ')]
    rules[pair] = c
  elif line != '':
    template = line

pairs = defaultdict(int)
hist = defaultdict(int)
for i in range(len(template) - 1):
  pairs[template[i:i + 2]] += 1
  hist[template[i]] += 1
hist[template[-1]] += 1

def performRound():
  global pairs
  newP = copy.deepcopy(pairs)
  for pair, freq in pairs.items():
    newP[pair] -= freq
    newP[pair[0] + rules[pair]] += freq
    newP[rules[pair] + pair[1]] += freq
    hist[rules[pair]] += freq
  pairs = newP

def getDiff():
  top = None
  bot = None
  for c, freq in hist.items():
    if top == None or freq > hist[top]:
      top = c
    if bot == None or freq < hist[bot]:
      bot = c
  return hist[top] - hist[bot]

for i in range(40):
  if i == 10:
    print('Part one:', getDiff())
  performRound()

print('Part two:', getDiff())