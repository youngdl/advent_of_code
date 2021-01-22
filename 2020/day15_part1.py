def main():

    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day15_data.txt'
    with open(file_path, 'r') as f:
        start_number = [int(i) for i in f.read().strip().split(',')]
    c = len(start_number)
    while c < 2020:
        if start_number[c-1] not in start_number[:c-1]:
            start_number.append(0)
        else:
            for i in range(c-2, -1, -1):
                if start_number[i] == start_number[c-1]:
                    break
            start_number.append(c-1-i)    
        c += 1
    print(start_number[-1])
if __name__ == '__main__':
    main()
