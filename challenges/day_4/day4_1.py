
def get_passports_list_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    return content.split('\n\n')


def check_passport(passport):
    keys_to_search = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    fields = passport.split()

    key_list = set()

    for field in fields:
        key, value = field.split(':')
        key_list.add(key)

    return len(keys_to_search - key_list) == 0


def main():
    passports_list = get_passports_list_from_file('input.in')

    count = 0

    for passport in passports_list:
        valid = check_passport(passport)

        if valid:
            count += 1

    print(count)




if __name__ == '__main__':
    main()
