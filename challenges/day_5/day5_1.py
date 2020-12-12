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


def main():
    boarding_pass_list = get_data_from_file('input.in').split()

    highest_id = 0

    for boarding_pass in boarding_pass_list:
        row = boarding_pass[:-3]
        seat = boarding_pass[-3:]

        my_row = search_row(row)
        my_seat = search_seat(seat)

        seat_id = my_row * 8 + my_seat

        # print(f'Row: {my_row}; Seat: {my_seat}; seat ID: {seat_id}')

        highest_id = max(highest_id, seat_id)

    print(highest_id)


if __name__ == '__main__':
    main()
