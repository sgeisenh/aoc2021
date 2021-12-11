require 'util'

numbers = map(split(readall('../input/01.txt'), '\n'), function(line)
    return tonumber(line)
end)

count1 = 0
count2 = 0
for i = 2, #numbers do
    if numbers[i] > numbers[i - 1] then
        count1 = count1 + 1
    end
    if i >= 4 and numbers[i] > numbers[i - 3] then
        count2 = count2 + 1
    end
end
print('Part one:', count1)
print('Part two:', count2)
