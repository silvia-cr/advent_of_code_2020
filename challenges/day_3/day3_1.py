def get_map_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def main():
    map = get_map_from_file('input.in')

    n_lines = map.count('\n') + 1               # last line has not end-of-line
    line_len = (len(map) + 1) // n_lines - 1    # last line has not end-of-line
    map = map.replace('\n', '')

    mov_x = 3
    mov_y = 1

    current_x = 0
    current_y = 0

    trees = 0

    for _ in range((n_lines - 1) // mov_y):
        current_x = (current_x + mov_x) % line_len
        current_y = (current_y + mov_y) % n_lines

        real_position = current_y * line_len + current_x

        if map[real_position] == '#':
            trees += 1

    print(trees)


if __name__ == '__main__':
    main()
