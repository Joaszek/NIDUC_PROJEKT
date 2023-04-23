import random


def create_packages(number_of_packages, package_size):
    packages = []

    for i in range(number_of_packages):

        package = ''
        for j in range(0, package_size):
            bit = random.randint(0, 1)
            package += str(bit)

        packages.append(package)

    return packages


def create_packages_with_parity_bit(number_of_packages, package_size):
    packages = []

    for i in range(number_of_packages):

        package = ''
        number_of_1 = 0
        for j in range(0, package_size):

            bit = random.randint(0, 1)
            package += str(bit)
            if bit == 1:
                number_of_1 += 1

        # even number_of_1
        if number_of_1 % 2 == 0:
            package += str(0)
        else:
            package += str(1)

        packages.append(package)
    return packages
