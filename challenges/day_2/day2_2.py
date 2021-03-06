def get_list_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content.split('\n')


def check_password(password):
    pwd_config = password.split()

    positions = pwd_config[0].split('-')
    char = pwd_config[1][0]
    pwd = pwd_config[2]

    if (pwd[int(positions[0])-1] == char) ^ (pwd[int(positions[1])-1] == char):
        return True
    else:
        return False


def main():
    passwords_list = get_list_from_file('input.in')

    valid_passwords = 0

    for password in passwords_list:
        valid = check_password(password)

        if valid:
            valid_passwords += 1

    print(valid_passwords)


if __name__ == '__main__':
    main()
