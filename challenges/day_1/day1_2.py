import cProfile


def get_list_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return list(map(int, content.split()))


def search_values(numbers, value):
    for first in numbers:
        second = value - first
        if second in numbers:
            return first, second

    return None, None


def get_numbers(numbers):
    for idx, first in enumerate(numbers):
        values = search_values(numbers[idx+1:], 2020-first)

        if all(values):
            return first, values[0], values[1]

    return None, None, None


def main():
    numbers_list = get_list_from_file('input.in')

    numbers = get_numbers(numbers_list)

    if all(numbers):
        result = numbers[0] * numbers[1] * numbers[2]
        print(result)
        print(numbers)
    else:
        print('ERROR')


if __name__ == '__main__':
    cProfile.run('main()')
