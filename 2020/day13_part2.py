def main():

    # read in the file and generate a list with int type of bus_ID
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day13_data.txt'
    with open(file_path, 'r') as f:
        input_list = f.readlines()
    bus_list = input_list[1].strip('\n').split(',')

    timestamp = 0
    loops = 0
    step = int(bus_list[0])
    for index, bus_id in enumerate(bus_list[1:], start=1):
        if bus_id == 'x':
            continue
        
        bus_id = int(bus_id)
        # Find the next timestamp here.
        while (timestamp + index) % bus_id != 0:
            timestamp += step
            loops += 1
            print(timestamp)
        step *= bus_id
    print('timestamp is {}'.format(timestamp))
    print('loops is {}'.format(loops))


if __name__ == '__main__':
    main()
