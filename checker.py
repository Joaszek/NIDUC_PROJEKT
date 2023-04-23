def check_parity_bit(package, package_length):
    number_of_1 = 0
    parity_bit = '1'
    for i in range(package_length):
        if package[i] == '1':
            number_of_1 = number_of_1 + 1
    print(number_of_1)
    print(number_of_1 % 2)
    if number_of_1 % 2 == 0:
        parity_bit = '0'

    return bool(package[package_length] == parity_bit)


def check_if_packages_are_the_same(package_1, package_2):
    return bool(package_1 == package_2)
