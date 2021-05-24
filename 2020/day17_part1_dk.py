from typing import Set, Tuple

Coordinate = Tuple[int, int, int]


def main():
    with open('data/day17_data_test.txt') as f:
        data = [line.strip() for line in f.readlines()]

    # Use a sparse representation of the data. Map (x, y, z) to a value.
    state: Set[Coordinate] = set()
    for y in range(len(data)):
        for x in range(len(data[y])):
            value = data[len(data)-y-1][x]
            if value == '#':
                state.add((x, y, 0))

    print_state(state)
    print('Cycle {} result: {}'.format(0, len(state)))
    for i in range(6):
        state = simulate(state)
        print('-' * 80)
        print_state(state)
        print('Cycle {} result: {}'.format(i+1, len(state)))
        break

    # print(len(state))


def print_state(state: Set[Coordinate]) -> None:
    min_x, min_y, min_z, max_x, max_y, max_z = next(iter(state)) * 2
    for (x, y, z) in state:
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        min_z = min(z, min_z)
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        max_z = max(z, max_z)

    for z in range(min_z, max_z+1):
        print('z={}'.format(z))
        output = []
        for y in range(max_y, min_y-1, -1):
            line = []
            for x in range(min_x, max_x+1):
                line.append('#' if (x, y, z) in state else '.')
            output.append(line)
        print('\n'.join(''.join(line) for line in output))


def simulate(
    state: Set[Coordinate],
) -> Set[Coordinate]:
    min_x, min_y, min_z, max_x, max_y, max_z = next(iter(state)) * 2
    for (x, y, z) in state:
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        min_z = min(z, min_z)
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        max_z = max(z, max_z)

    new_state = set()
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            for z in range(min_z-1, max_z+2):
                count = get_active_neighbor_count((x, y, z), state)
                if (x, y, z) in state:
                    if 2 <= count <= 3:
                        new_state.add((x, y, z))
                else:
                    if count == 3:
                        new_state.add((x, y, z))

    return new_state


def get_active_neighbor_count(
    coordinate: Coordinate,
    state: Set[Coordinate],
) -> int:
    cx, cy, cz = coordinate
    count = 0
    for x in [cx-1, cx, cx+1]:
        for y in [cy-1, cy, cy+1]:
            for z in [cz-1, cz, cz+1]:
                if (cx, cy, cz) == (x, y, z):
                    continue
                if (x, y, z) in state:
                    count += 1
    return count


if __name__ == '__main__':
    main()
