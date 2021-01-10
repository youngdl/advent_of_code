def main():

    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day13_data.txt'
    with open(file_path, 'r') as f:
        input_list = f.readlines()
    time_stamp = int(input_list[0].strip('\n'))
    bus_list = []
    for _ in input_list[1].strip('\n').split(','):
        try:
            bus_list.append(int(_))
        except:
            pass

    wait_time = {}
    for i in bus_list:
        wait_time[i] = i - time_stamp % i
        print(time_stamp, i, time_stamp%i)
    print(wait_time)
    min_wait = min(list(wait_time.values()))
    bus_id = list(wait_time.keys())[list(wait_time.values()).index(min_wait)]
    print('ID is {} and wait_time is {}, result is {}'.format(bus_id, min_wait, bus_id * min_wait))


if __name__ == '__main__':
    main()
