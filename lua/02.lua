require 'util'

lines = split(readall('../input/02.txt'), '\n')

function partOne(directions)
  local hor, depth
  hor = 0
  depth = 0
  for _, line in ipairs(lines) do
    splits = split(line, ' ')
    local dist = tonumber(splits[2])
    if splits[1] == 'forward' then
      hor = hor + dist
    elseif splits[1] == 'down' then
      depth = depth + dist
    elseif splits[1] == 'up' then
      depth = depth - dist
    end
  end
  return hor * depth
end

function partTwo(directions)
  local hor, depth, aim
  hor = 0
  depth = 0
  aim = 0
  for _, line in ipairs(lines) do
    splits = split(line, ' ')
    local dist = tonumber(splits[2])
    if splits[1] == 'forward' then
      hor = hor + dist
      depth = depth + aim * dist
    elseif splits[1] == 'down' then
      aim = aim + dist
    elseif splits[1] == 'up' then
      aim = aim - dist
    end
  end
  return hor * depth
end

print('Part one:', partOne(lines))
print('Part two:', partTwo(lines))