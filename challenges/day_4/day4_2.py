import re


def get_passports_list_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    return content.split('\n\n')


def check_byr(value):
    if len(value) == 4 and (1920 <= int(value) <= 2002):
        return True
    return False


def check_iyr(value):
    if len(value) == 4 and (2010 <= int(value) <= 2020):
        return True
    return False


def check_eyr(value):
    if len(value) == 4 and (2020 <= int(value) <= 2030):
        return True
    return False


def check_hgt(value):
    measure_unit = value[-2:]
    measure_value = value[:-2]
    
    if measure_unit == 'cm' and (150 <= int(measure_value) <= 193):
        return True
    elif measure_unit == 'in' and (59 <= int(measure_value) <= 76):
        return True
    return False


def check_hcl(value):
    pattern = re.compile('^\#[0-9a-f]{6}$')
    if pattern.match(value):
        return True
    return False


def check_ecl(value):
    values_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value in values_list:
        return True
    return False


def check_pid(value):
    pattern = re.compile('^([0-9]{9})$')

    if pattern.match(value):
        return True
    return False


def check_field(field):
    field_splited = field.split(':')

    if len(field_splited) != 2:
        return False

    key = field_splited[0]
    value = field_splited[1]

    if key == 'byr' and check_byr(value):
        return True
    elif key == 'iyr' and check_iyr(value):
        return True
    elif key == 'eyr' and check_eyr(value):
        return True
    elif key == 'hgt' and check_hgt(value):
        return True
    elif key == 'hcl' and check_hcl(value):
        return True
    elif key == 'ecl' and check_ecl(value):
        return True
    elif key == 'pid' and check_pid(value):
        return True
    elif key == 'cid':
        return True
    
    return False
        

def check_passport(passport):
    fields = passport.split()

    if len(fields) <= 7 or len(fields) > 9:
        return False

    for field in fields:
        if not check_field(field):
            return False

    return True


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
