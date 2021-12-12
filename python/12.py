import fileinput
import copy
from collections import defaultdict

lines = [line.strip() for line in fileinput.input()]
G = {}
for line in lines:
  a, b = line.split('-')
  if a not in G:
    G[a] = set()
  if b not in G:
    G[b] = set()
  G[a].add(b)
  G[b].add(a)

def partOne():
  def dfs(start, seen, path):
    if start == 'end':
      return set([tuple(path + ['end'])])
    paths = []
    seen = copy.deepcopy(seen)
    seen.add(start)
    path = copy.deepcopy(path)
    path.append(start)
    for cave in G[start]:
      if cave.isupper() or cave not in seen:
        paths += dfs(cave, seen, path)
    return paths

  return len(dfs('start', set(), []))

def partTwo():
  def dfs(start, seen, path, twice):
    if start == 'end':
      return set([tuple(path + ['end'])])
    paths = []
    seen = copy.deepcopy(seen)
    seen.add(start)
    path = copy.deepcopy(path)
    path.append(start)
    for cave in G[start]:
      if cave.isupper():
        paths += dfs(cave, seen, path, twice)
      elif cave != 'start' and cave in seen and not twice:
        paths += dfs(cave, seen, path, True)
      elif cave != 'start' and cave not in seen:
        paths += dfs(cave, seen, path, twice)
    return paths

  return len(dfs('start', set(), [], False))

print('Part one:', partOne())
print('Part two:', partTwo())