with open('/Users/xiaolin/Documents/GitHub/advent_of_code/2021/data/day2.txt') as f:
    lines = f.readlines()
forwards = []
ups = []
downs = []
for line in lines:
    num = int(line.strip('\n').split(' ')[-1])
    if line.startswith('f'):
        forwards.append(num)
    if line.startswith('d'):
        downs.append(num)
    if line.startswith('u'):
        ups.append(num)
print(sum(forwards) * (sum(downs) - sum(ups)) )
