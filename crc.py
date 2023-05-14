# Description: This file contains the functions to calculate the CRC code of a package and to check if the CRC code is correct

def xor(p, q):
    if p == q:
        return '0'
    else:
        return '1'


def create_package(package, n):
    for i in range(0, n):
        package = package + '0'
    return package


def crc(crc_package, n, divisor, package_length):
    crc_end = ""
    for x in range(0, package_length):
        crc_end = crc_end + '0'

    i = 0
    while not crc_package[0:package_length] == crc_end:
        result_xor = ""
        while crc_package[i] != '1':
            i += 1

        for y in range(i, i + n + 1):
            result_xor = result_xor + xor(crc_package[y], divisor[y - i])

        crc_package = crc_package[:i] + result_xor + crc_package[i + n + 1:]
    return crc_package


def check(package, n, divisor, package_length):
    crc_check = ""
    for x in range(0, package_length + n):
        crc_check = crc_check + '0'
    package = crc(package, n, divisor, package_length)
    return bool(crc_check == package)
