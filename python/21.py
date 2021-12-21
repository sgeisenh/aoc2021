p1 = 7
p1score = 0
p2 = 2
p2score = 0
die = 0
p1turn = True
num_rolls = 0

while p1score < 1000 and p2score < 1000:
  rolls = 3 * die + 6
  if p1turn:
    p1 = (p1 + rolls) % 10
    p1score += p1 + 1
    p1turn = False
  else:
    p2 = (p2 + rolls) % 10
    p2score += p2 + 1
    p1turn = True
  die = (die + 3) % 100
  num_rolls += 1

print('Part one:', min(p1score, p2score) * 3 * num_rolls)

D = {}
def playerWins(p1, p2, p1score, p2score, p1turn):
  if p1score >= 21:
    return (1, 0)
  elif p2score >= 21:
    return (0, 1)
  elif (p1, p2, p1score, p2score, p1turn) in D:
    return D[(p1, p2, p1score, p2score, p1turn)] 
  p1total = 0
  p2total = 0
  for d1 in [1, 2, 3]:
    for d2 in [1, 2, 3]:
      for d3 in [1, 2, 3]:
        if p1turn:
          newp1 = (p1 + d1 + d2 + d3) % 10
          (p1wins, p2wins) = playerWins(newp1, p2, p1score + newp1 + 1, p2score, False)
          p1total += p1wins
          p2total += p2wins
        else:
          newp2 = (p2 + d1 + d2 + d3) % 10
          (p1wins, p2wins) = playerWins(p1, newp2, p1score, p2score + newp2 + 1, True)
          p1total += p1wins
          p2total += p2wins
  D[(p1, p2, p1score, p2score, p1turn)] = (p1total, p2total)
  return (p1total, p2total)

print('Part two:', max(playerWins(7, 2, 0, 0, True)))