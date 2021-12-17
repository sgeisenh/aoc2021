import math

x1 = 206
x2 = 250
y1 = -105
y2 = -57

min_x_vel = math.ceil(math.sqrt(2 * x1 + 1 / 4) - 1 / 2)

def stepsToX(vel):
  x = 0
  num_steps = 0
  while x < x1:
    x += vel
    vel -= 1
    num_steps += 1
  return num_steps

steps = stepsToX(min_x_vel)

def yPosAfterSteps(vy):
  y = 0
  while y >= y1:
    if y <= y2:
      return y
    y += vy
    vy -= 1
  return y

def highest(vy):
  y = 0
  while vy > 0:
    y += vy
    vy -= 1
  return y

maxVy = None
for vy in range(0, 500):
  if y1 <= yPosAfterSteps(vy) <= y2 and (maxVy == None or vy > maxVy):
    maxVy = vy

print('Part one:', highest(maxVy))

def stepsInX(vx):
  minstep = None
  x = 0
  step = 0
  while vx > 0 and x <= x2:
    x += vx
    vx -= 1
    step += 1
    if x1 <= x <= x2 and minstep == None:
      minstep = step
  return minstep, (None if x <= x2 else step - 1)

def yInBox(vy, stepsInX):
  minstep, maxstep = stepsInX
  step = minstep
  while maxstep == None or step <= maxstep:
    y = step * (step + 1) // 2 + step * (vy - step)
    if y < y1:
      return False
    if y1 <= y <= y2:
      return True
    step += 1
  return False

vels = set()
for vx in range(min_x_vel, x2 + 1):
  for vy in range(y1, 500):
    minstep, maxstep = stepsInX(vx)
    if minstep != None:
      if yInBox(vy, (minstep, maxstep)):
        vels.add((vx, vy))
print('Part two:', len(vels))
