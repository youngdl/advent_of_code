# read in data and generate a list of all lines
file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day4_data.txt'
with open(file_path, 'r') as f:
    info_list = f.read().split('\n\n')

# parse all the useful information from each element 
valid_num = 0
requirement = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in info_list:
    meta_data = []
    newline_list = passport.split('\n')
    for item in newline_list:
        entry_list = item.split(' ')
        for entry in entry_list:
            meta_temp = entry.split(':')[0]
            meta_data.append(meta_temp)
    if all(x in meta_data for x in requirement):
        valid_num += 1

print(valid_num)
