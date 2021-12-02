with open('/Users/xiaolin/Documents/GitHub/advent_of_code/2021/data/day2.txt') as f:
    lines = f.readlines()
aim = 0
depth = 0
x = 0
for line in lines:
    num = int(line.strip('\n').split(' ')[-1])
    if line.startswith('f'):
        x += num
        depth += aim * num
    if line.startswith('d'):
        aim += num
    if line.startswith('u'):
        aim -= num
print(x * depth)
