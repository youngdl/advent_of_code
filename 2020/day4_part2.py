import re

REQUIRED_FIELDS = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
])

VALID_ECL_SET = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def main():
    # read in data and generate a list of all lines
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day4_data.txt'
    with open(file_path, 'r') as f:
        info_list = f.read().strip().split('\n\n')

    valid_num = 0
    for entry in info_list:
        if is_password_valid(entry):
            valid_num +=1
    print(valid_num)


def is_password_valid(entry: str) -> bool:
    """Returns True if the passport is valid, and False otherwise."""
    info_lib = {}
    entry_list = re.split('[\n\s]+', entry)
    for item in entry_list:
        key, value = item.split(':')
        info_lib[key] = value

    # Validate that all required fields are present.
    info_lib_keys = set(info_lib.keys())
    if not REQUIRED_FIELDS.issubset(info_lib_keys):
        return False

    # Validate the numbers of all the fields correct. 
    if not 1920 <= int(info_lib['byr']) <= 2002:
        return False
    
    if not 2010 <= int(info_lib['iyr']) <= 2020:
        return False

    if not 2020 <= int(info_lib['eyr']) <= 2030:
        return False

    height_match1 = re.match('^(\d+)cm$', info_lib['hgt'])
    height_match2 = re.match('^(\d+)in$', info_lib['hgt'])
    if not ((height_match1 and 150 <= int(height_match1.group(1)) <= 193) or 
            (height_match2 and 59 <= int(height_match2.group(1)) <= 76)): 
        return False

    if not re.match('^#[0-9a-f]{6}$', info_lib['hcl']):
        return False

    if info_lib['ecl'] not in VALID_ECL_SET:
        return False

    if not re.match('^\d{9}$', info_lib['pid']):
        return False

if __name__ == '__main__':
    main()
