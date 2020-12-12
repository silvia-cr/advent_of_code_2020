def get_data_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def search_row(row):
    return get_value(row, ['F', 'B'], 0, 127)


def search_seat(seat):
    return get_value(seat, ['L', 'R'], 0, 7)


def get_value(data, values, start, end):

    for d in data:

        if d == values[0]:
            end = (start + end) // 2
        elif d == values[1]:
            start = (start + end) // 2 + 1
        else:
            raise Exception("Value not valid")

    if start != end:
        print(f'Error: {start} != {end}; {values}')

    return start


def search_seat_id(id_list):

    for row in range(128):
        for seat in range(8):
            id = row * 8 + seat

            if (id not in id_list) and ((id - 1) in id_list) and ((id + 1) in id_list):
                return id

    return None


def main():
    boarding_pass_list = get_data_from_file('input.in').split()

    id_list = set()

    for boarding_pass in boarding_pass_list:
        row = boarding_pass[:-3]
        seat = boarding_pass[-3:]

        my_row = search_row(row)
        my_seat = search_seat(seat)

        seat_id = my_row * 8 + my_seat

        id_list.add(seat_id)

        # print(f'Row: {my_row}; Seat: {my_seat}; seat ID: {seat_id}')

    my_seat_id = search_seat_id(id_list)
    print(my_seat_id)


if __name__ == '__main__':
    main()
