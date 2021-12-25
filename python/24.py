import fileinput

program = [tuple(line.strip().split(' ')) for line in fileinput.input()]

def runProgram(prog, input):
  progIdx = 0
  inputIdx = 0
  ctx = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
  while progIdx < len(prog):
    match prog[progIdx]:
      case ('inp', a):
        ctx[a] = input[inputIdx]
        inputIdx += 1
      case ('add', a, b):
        if b[0].isdigit() or b[0] == '-':
          ctx[a] = ctx[a] + int(b)
        else:
          ctx[a] = ctx[a] + ctx[b]
      case ('mul', a, b):
        if b[0].isdigit() or b[0] == '-':
          ctx[a] = ctx[a] * int(b)
        else:
          ctx[a] = ctx[a] * ctx[b]
      case ('div', a, b):
        if b[0].isdigit() or b[0] == '-':
          ctx[a] = ctx[a] // int(b)
        else:
          ctx[a] = ctx[a] // ctx[b]
      case ('mod', a, b):
        if b[0].isdigit() or b[0] == '-':
          ctx[a] = ctx[a] % int(b)
        else:
          ctx[a] = ctx[a] % ctx[b]
      case ('eql', a, b):
        if a == 'x' and b == 'w':
          print('x:', ctx['x'], 'w:', ctx['w'])
        if b[0].isdigit() or b[0] == '-':
          ctx[a] = 1 if ctx[a] == int(b) else 0
        else:
          ctx[a] = 1 if ctx[a] == ctx[b] else 0
    progIdx += 1
  return ctx['z']

def numToInput(num):
  result = []
  while num > 0:
    result.append(num % 10)
    num //= 10
  return [digit for digit in reversed(result)]

def inputToNum(input):
  num = 0
  for digit in input:
    num *= 10
    num += digit
  return num

num = 11721151118175
inp = numToInput(num)
result = runProgram(program, inp)
print(num, result)

# inp w
# mul x 0 x -> 0
# add x z x -> 0
# mod x 26 x -> 0
# div z 1 z -> 0
# add x 15 x -> 15
# eql x w x -> 0
# eql x 0 x -> 1
# mul y 0 y -> 0
# add y 25 y -> 25
# mul y x y -> 25
# add y 1 y -> 26
# mul z y z -> 0
# mul y 0 y -> 0
# add y w y -> dig1
# add y 13 y -> dig1 + 13
# mul y x y -> dig1 + 13
# add z y z -> dig1 + 13
# inp w w -> dig2
# mul x 0 x -> 0
# add x z x -> dig1 + 13
# mod x 26 x -> (dig1 + 13) % 26
# div z 1 z -> dig1 + 13
# add x 10 x -> (dig1 + 13) % 26 + 10
# eql x w x -> 0
# eql x 0 x -> 1
# mul y 0 y -> 0
# add y 25 y -> 25
# mul y x y -> 25
# add y 1 y -> 26
# mul z y z -> (dig1 + 13) * 26
# mul y 0 y -> 0
# add y w y -> dig2
# add y 16 y -> dig2 + 16
# mul y x y -> dig2 + 16
# add z y z -> (dig1 + 13) * 26 + dig2 + 16
# inp w w -> dig3
# x -> 1, y -> dig2 + 16, z -> (dig1 + 13) * 26 + dig2 + 16
# mul x 0 x -> 0
# add x z x -> (dig1 + 13) * 26 + dig2 + 16
# mod x 26 x -> ((dig1 + 13) * 26 + dig2 + 16) % 26
# div z 1 z -> (dig1 + 13) * 26 + dig2 + 16
# add x 12 x -> ((dig1 + 13) * 26 + dig2 + 16) % 26 + 12
# eql x w // not possible
# eql x 0 // x -> 1
# mul y 0 y -> 0
# add y 25 y -> 25
# mul y x y -> 25
# add y 1 y -> 26
# mul z y z -> ((dig1 + 13) * 26 + dig2 + 16) * 26
# mul y 0 -> y -> 0
# add y w y -> dig3
# add y 2 y -> dig3 + 2
# mul y x y -> dig3 + 2
# add z y z -> ((dig1 + 13) * 26 + dig2 + 16) * 26 + dig3 + 2
# inp w
# x -> 1, y -> dig3 + 2
# mul x 0 x -> 0
# add x z x -> ((dig1 + 13) * 26 + dig2 + 16) * 26 + dig3 + 2
# mod x 26 x -> (dig3 + 2) % 26
# div z 1
# add x 10 x -> (dig3 + 2) % 26 + 10
# eql x w 
# eql x 0 x -> 1
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y z -> z -> (((dig1 + 13) * 26 + dig2 + 16) * 26 + dig3 + 2) * 26
# mul y 0
# add y w
# add y 8 y -> dig4 + 8
# mul y x y -> dig4 + 8
# add z y z z -> z + dig4 + 8
# inp w
# mul x 0
# add x z
# mod x 26 x -> (dig4 + 8) % 26
# div z 1
# add x 14
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 11
# mul y x
# add z y 
# inp w
# mul x 0
# add x z
# mod x 26 x -> (dig5 + 11) % 26
# div z 26 z -> ... dig4 + 8
# add x -11 x -> dig5
# eql x w dig6 == dig5?
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 6
# mul y x
# add z y
# inp w w -> dig7
# mul x 0
# add x z
# mod x 26 x -> dig6 + 6 or dig4 + 8
# div z 1
# add x 10
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 12
# mul y x
# add z y
# inp w
# mul x 0
# add x z
# mod x 26
# div z 26
# add x -16
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 2
# mul y x
# add z y
# inp w
# mul x 0
# add x z
# mod x 26
# div z 26
# add x -9
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 2
# mul y x
# add z y
# inp w
# mul x 0
# add x z
# mod x 26
# div z 1
# add x 11
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 15
# mul y x
# add z y
# inp w
# mul x 0
# add x z
# mod x 26
# div z 26
# add x -8
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 1
# mul y x
# add z y
# inp w
# mul x 0
# add x z
# mod x 26
# div z 26
# add x -8
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 10
# mul y x
# add z y
# inp w
# mul x 0
# add x z
# mod x 26
# div z 26
# add x -10
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y 14
# mul y x
# add z y
# inp w
# mul x 0 x -> 0
# add x z x -> z
# mod x 26 x -> z % 26
# div z 26 z -> z // 26
# add x -9 x -> z % 26 - 9
# eql x w // is digit 14 equal to z % 26 - 9?
# eql x 0 
# mul y 0 y -> 0
# add y 25 y -> 25
# mul y x y is 25 if 306 else 0
# add y 1 y is 26 if 306 else 1
# mul z y z *= something
# mul y 0 y -> 0
# add y w y -> dig14
# add y 10 y -> dig14 + 10
# mul y x y -> dig14 must be z % 26 - 9
# add z y