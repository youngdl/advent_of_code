import re

def main():
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day12_data.txt'
    with open(file_path, 'r') as f:
        input_list = f.readlines()

    ship_pos = [0, 0]  #East-North is positive
    waypoint = [10, 1] #Relative to the ship, and east-north is positive
    pattern = re.compile('^([FWENSLR])(\d+)')
    
    for item in input_list:
        match = pattern.match(item)
        action = match.group(1)
        value = match.group(2)
        if action == 'W':
            waypoint[0] = waypoint[0] - int(value)
        if action == 'E':
            waypoint[0] = waypoint[0] + int(value)
        if action == 'N':
            waypoint[1] = waypoint[1] + int(value)
        if action == 'S':
            waypoint[1] = waypoint[1] - int(value)
        if action == 'F':
            ship_pos[0] = ship_pos[0] + int(value) * waypoint[0]
            ship_pos[1] = ship_pos[1] + int(value) * waypoint[1]
        if action == 'L':
            if (int(value) // 90) % 4 == 1:
                temp = waypoint[0]
                waypoint[0] = -1 * waypoint[1]
                waypoint[1] = temp
            elif (int(value) // 90) % 4 == 2:
                waypoint[0] = -1 * waypoint[0]
                waypoint[1] = -1 * waypoint[1]
            elif (int(value)// 90) % 4 == 3:
                temp = waypoint[0]
                waypoint[0] = waypoint[1]
                waypoint[1] = -1 * temp
            else:
                pass
        if action == 'R':
            if (int(value) // 90) % 4 == 3:
                temp = waypoint[0]
                waypoint[0] = -1 * waypoint[1]
                waypoint[1] = temp
            elif (int(value) // 90) % 4 == 2:
                waypoint[0] = -1 * waypoint[0]
                waypoint[1] = -1 * waypoint[1]
            elif (int(value) // 90) % 4 == 1:
                temp = waypoint[0]
                waypoint[0] = waypoint[1]
                waypoint[1] = -1 * temp
            else:
                pass

    print('east number is {}, north number is {}, and the Manhattan Distance is {}'.format(ship_pos[0], ship_pos[1], (abs(ship_pos[0]) + abs(ship_pos[1]))))


if __name__ == '__main__':
    main()
