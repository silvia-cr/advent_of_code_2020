def get_map_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def main():
    map = get_map_from_file('input.in')

    n_lines = map.count('\n') + 1               # last line has not end-of-line
    line_len = (len(map) + 1) // n_lines - 1    # last line has not end-of-line
    map = map.replace('\n', '')

    mov = (3, 1)

    current = (0, 0)

    trees = 0

    for _ in range((n_lines - 1) // mov[1]):
        current = ((current[0] + mov[0]) % line_len, (current[1] + mov[1]) % n_lines)

        real_position = current[1] * line_len + current[0]

        if map[real_position] == '#':
            trees += 1

    print(trees)


if __name__ == '__main__':
    main()
