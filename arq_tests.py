# Description: This file contains functions that test ARQ methods.

import generator
import channel
import checker
import crc

import numpy as np


def no_arq(package_length, number_of_packages):
    csv_data = []

    for probability in np.arange(0.8, 0, -0.01):

        packages = generator.create_packages(
            number_of_packages, package_length)

        # statistics
        incorrect_return_packages = 0
        correct_return_packages = 0

        for package in packages:
            return_package = channel.disrupted_package(package, probability)

            if checker.check_if_packages_are_the_same(package, return_package):
                correct_return_packages += 1
            else:
                incorrect_return_packages += 1

        percentage_correct = correct_return_packages / number_of_packages * 100
        percentage_incorrect = incorrect_return_packages / number_of_packages * 100

        data = (round(probability, 2), correct_return_packages, round(
            percentage_correct, 2), incorrect_return_packages, round(percentage_incorrect, 2))
        csv_data.append(data)

    return csv_data


def arq_parity_bit(package_length, number_of_packages):
    csv_data = []

    for probability in np.arange(0.8, 0, -0.01):
        packages = generator.create_packages_with_parity_bit(
            number_of_packages, package_length)

        # statistics
        arq_requests = 0
        correct_returns = 0

        for package in packages:
            return_package = channel.disrupted_package(package, probability)
            while not checker.check_parity_bit(return_package, package_length):
                return_package = channel.disrupted_package(
                    package, probability)

                arq_requests += 1
            if checker.check_if_packages_are_the_same(package, return_package):
                correct_returns += 1

        percentage = (correct_returns / number_of_packages) * 100
        data = (round(probability, 3), arq_requests,
                correct_returns, round(percentage, 3))
        csv_data.append(data)

    return csv_data


def arq_crc(package_length, number_of_packages, n, divisor):
    csv_data = []

#  Dla prawdopodobienstwa od 0.8 do 0.0 z krokiem 0.01 tworzymy paczki z bitem parzystosci
    for probability in np.arange(0.3, 0, -0.01):
        packages = generator.create_packages_with_parity_bit(
            number_of_packages, package_length)

        # Statystyki dla ARQ
        arq_requests = 0
        correct_returns = 0

#  Dla kazdej paczki
        for package in packages:
#  Tworzymy kod CRC
            package = crc.create_package(package, n)
#  Wysylamy paczke
            code = crc.crc(package, n, divisor, package_length)[
                package_length:package_length + n]
#  Dodajemy kod CRC do paczki
            package = package[:package_length] + code
#  Wysylamy paczke
            return_package = channel.disrupted_package(package, probability)

#  Wysylanie paczki z powrotem jesli jest niepoprawna
            while not crc.check(return_package, n, divisor, package_length):
                return_package = channel.disrupted_package(
                    package, probability)
                arq_requests += 1
#  Weryfikujemy poprawność paczki zwróconej
            if checker.check_if_packages_are_the_same(package, return_package):
                correct_returns += 1

#  Dodajemy do pliku nasze dane
        percentage = correct_returns / number_of_packages * 100
        data = (round(probability, 2), arq_requests,
                correct_returns, round(percentage, 2))
        csv_data.append(data)

    return csv_data
