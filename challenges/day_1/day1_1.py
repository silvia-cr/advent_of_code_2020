def get_list_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return list(map(int, content.split()))


def get_numbers(numbers):
    for first in numbers:
        second = 2020 - first
        if second in numbers:
            return first, second

    return None, None


def main():
    numbers_list = get_list_from_file('input.in')

    first, second = get_numbers(numbers_list)

    if all([first, second]):
        result = first * second
        print(result)
    else:
        print('ERROR')


if __name__ == '__main__':
    main()
