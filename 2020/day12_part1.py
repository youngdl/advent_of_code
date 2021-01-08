import re

def main():
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day12_data.txt'
    with open(file_path, 'r') as f:
        input_list = f.readlines()
    
    sum_NS = 0
    sum_WE = 0
    current_dir = 'E'
    directions = ['E', 'N', 'W', 'S']
    for item in input_list:
        r = re.match('^F(\d+)', item)
        w = re.match('^W(\d+)', item)
        e = re.match('^E(\d+)', item)
        n = re.match('^N(\d+)', item)
        s = re.match('^S(\d+)', item)
        d = re.match('^([LR])(\d+)', item)

        if w:
            sum_WE += int(w.group(1)) * -1
        if e:
            sum_WE += int(e.group(1))  
        if n:
            sum_NS += int(n.group(1)) * -1
        if s:
            sum_NS += int(s.group(1))

        if r:
            if current_dir == 'E':
                sum_WE += int(r.group(1))
            elif current_dir == 'W':
                sum_WE += int(r.group(1)) * -1
            elif current_dir == 'N':
                sum_NS += int(r.group(1)) * -1
            else:
                sum_NS += int(r.group(1))

        if d:
            if d.group(1) == 'L':
                index = (directions.index(current_dir) + int(d.group(2)) // 90) % 4
            else:
                index = (directions.index(current_dir) - int(d.group(2)) // 90) % 4
            current_dir = directions[index]

    print(sum_WE)
    print(sum_NS)        
    print('result is {}'.format(abs(sum_WE) + abs(sum_NS)))

if __name__ == '__main__':
    main()
