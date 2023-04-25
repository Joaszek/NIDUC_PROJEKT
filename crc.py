def xor(p, q):
    if p == q:
        return '0'
    else:
        return '1'


def create_package(package, n):
    for i in range(0, n):
        package = package + '0'
    return package


# Funkcja crc(crc_package, n, divisor, package_length) przyjmuje pakiet crc_package,
# długość segmentu CRC n, dzielnik CRC divisor i długość pakietu package_length.
# Wykorzystuje ona algorytm CRC-division do wygenerowania końcowej sumy kontrolnej CRC.
# W pętli while, crc_package jest poddawany ciągłym operacjom XOR z divisor
# aż do osiągnięcia zerowego segmentu CRC.

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


#  Funkcja check(package, n, divisor, package_length) przyjmuje pakiet package,
#  długość segmentu CRC n, dzielnik CRC divisor i długość pakietu package_length.
#  Wykorzystuje ona crc() do obliczenia sumy kontrolnej CRC dla package,
#  a następnie zwraca True, jeśli końcowa suma kontrolna CRC jest równa ciągowi zer o
#  długości package_length + n, w przeciwnym razie zwraca False.

def check(package, n, divisor, package_length):
    crc_check = ""
    for x in range(0, package_length + n):
        crc_check = crc_check + '0'
    package = crc(package, n, divisor, package_length)
    return bool(crc_check == package)
