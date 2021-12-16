import fileinput
import math

lines = [line.strip() for line in fileinput.input()]

bits = bin(int(lines[0], base=16))[2:]
if len(bits) % 4 != 0:
  bits = (4 - len(bits) % 4) * '0' + bits
version_total = 0

def parseLiteralHelper(bits, acc):
  if bits[0] == '0':
    bits = bits[1:]
    return acc + int(bits[:4], 2), bits[4:]
  bits = bits[1:]
  return parseLiteralHelper(bits[4:], (acc + int(bits[:4], 2)) << 4)

def parseLiteral(bits):
  return parseLiteralHelper(bits, 0)

def parseLenPackets(bits):
  payload = []
  while bits != '' and int(bits, 2) != 0:
    packet, bits = parsePacket(bits)
    payload.append(packet)
  return payload

def parseNumPackets(bits, num):
  payload = []
  while len(payload) < num:
    packet, bits = parsePacket(bits)
    payload.append(packet)
  return payload, bits

def parseOperator(bits):
  length_type_id = int(bits[:1], 2)
  bits = bits[1:]
  if length_type_id == 0:
    total_length = int(bits[:15], 2)
    bits = bits[15:]
    return parseLenPackets(bits[:total_length]), bits[total_length:]
  else:
    num_subpackets = int(bits[:11], 2)
    bits = bits[11:]
    return parseNumPackets(bits, num_subpackets)


def parsePacket(bits):
  global version_total
  version = int(bits[:3], 2)
  bits = bits[3:]
  version_total += version
  type_id = int(bits[:3], 2)
  bits = bits[3:]
  payload = None
  if type_id == 4:
    payload, bits = parseLiteral(bits)
  else:
    payload, bits = parseOperator(bits)

  return (version, type_id, payload), bits

def evaluate(program):
  version, type_id, payload = program
  if type_id == 4:
    return payload
  subexprs = [evaluate(subprogram) for subprogram in payload]
  if type_id == 0:
    return sum(subexprs)
  if type_id == 1:
    return math.prod(subexprs)
  if type_id == 2:
    return min(subexprs)
  if type_id == 3:
    return max(subexprs)
  if type_id == 5:
    assert(len(subexprs) == 2)
    return 1 if subexprs[0] > subexprs[1] else 0
  if type_id == 6:
    assert(len(subexprs) == 2)
    return 1 if subexprs[0] < subexprs[1] else 0
  if type_id == 7:
    assert(len(subexprs) == 2)
    return 1 if subexprs[0] == subexprs[1] else 0

program = parsePacket(bits)[0]
print('Part one:', version_total)
print('Part two:', evaluate(program))