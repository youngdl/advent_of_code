import re

def main():
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day12_data.txt'
    with open(file_path, 'r') as f:
        input_list = f.readlines()

    ship_pos = [0, 0]  #East-North is positive
    waypoint = [10, 1] #Relative to the ship, and east-north is positive
    for item in input_list:
        m = re.match('^F(\d+)', item)
        w = re.match('^W(\d+)', item)
        e = re.match('^E(\d+)', item)
        n = re.match('^N(\d+)', item)
        s = re.match('^S(\d+)', item)
        d = re.match('^([LR])(\d+)', item)

        if w:
            waypoint[0] = waypoint[0] - int(w.group(1))
        if e:
            waypoint[0] = waypoint[0] + int(e.group(1))
        if n:
            waypoint[1] = waypoint[1] + int(n.group(1))
        if s:
            waypoint[1] = waypoint[1] - int(s.group(1))
        if m:
            ship_pos[0] = ship_pos[0] + int(m.group(1)) * waypoint[0]
            ship_pos[1] = ship_pos[1] + int(m.group(1)) * waypoint[1]
        if d:
            if d.group(1) == 'L':
                if (int(d.group(2)) // 90) % 4 == 1:
                    temp = waypoint[0]
                    waypoint[0] = -1 * waypoint[1]
                    waypoint[1] = temp
                elif (int(d.group(2)) // 90) % 4 == 2:
                    waypoint[0] = -1 * waypoint[0]
                    waypoint[1] = -1 * waypoint[1]
                elif (int(d.group(2))// 90) % 4 == 3:
                    temp = waypoint[0]
                    waypoint[0] = waypoint[1]
                    waypoint[1] = -1 * temp
                else:
                    pass
            else:
                if (int(d.group(2)) // 90) % 4 == 3:
                    temp = waypoint[0]
                    waypoint[0] = -1 * waypoint[1]
                    waypoint[1] = temp
                elif (int(d.group(2)) // 90) % 4 == 2:
                    waypoint[0] = -1 * waypoint[0]
                    waypoint[1] = -1 * waypoint[1]
                elif (int(d.group(2)) // 90) % 4 == 1:
                    temp = waypoint[0]
                    waypoint[0] = waypoint[1]
                    waypoint[1] = -1 * temp
                else:
                    pass

    print('east number is {}, north number is {}, and the Manhattan Distance is {}'.format(ship_pos[0], ship_pos[1], (abs(ship_pos[0]) + abs(ship_pos[1]))))


if __name__ == '__main__':
    main()
