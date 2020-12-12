def get_data_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content.split('\n\n')


def main():
    answers_list = get_data_from_file('input.in')

    answer_count = 0
    for group in answers_list:

        group = group.split('\n')

        answer_sets = list()
        for person in group:
            answer_sets.append(set(person))

        full_answered = set.intersection(*answer_sets)
        answer_count += len(full_answered)

    print(answer_count)


if __name__ == '__main__':
    main()
