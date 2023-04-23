import generator
import channel
import crc
import statistics
import checker
import numpy as np

csv_data = []
FILENAME = "ARQ_results_crc.csv"
PACKAGE_LENGTH = 8
NUMBER_OF_PACKAGES = 10

N = 8
DIVISOR = "111010101"


def main():

    statistics.clear_file(FILENAME)

    for probability in np.arange(0.3, 0, -0.01):
        packages = generator.create_packages_with_parity_bit(NUMBER_OF_PACKAGES, PACKAGE_LENGTH)

        # statistics
        arq_requests = 0
        correct_returns = 0

        for package in packages:
            package = crc.create_package(package, N)
            code = crc.crc(package, N, DIVISOR, PACKAGE_LENGTH)[PACKAGE_LENGTH:PACKAGE_LENGTH + N]
            package = package[:PACKAGE_LENGTH] + code
            return_package = channel.disrupted_package(package, probability)

            while not crc.check(return_package, N, DIVISOR, PACKAGE_LENGTH):
                return_package = channel.disrupted_package(package, probability)
                arq_requests += 1

            if checker.check_if_packages_are_the_same(package, return_package):
                correct_returns += 1

        percentage = correct_returns / NUMBER_OF_PACKAGES * 100
        data = (round(probability, 2), arq_requests, correct_returns, round(percentage, 2))
        csv_data.append(data)

    statistics.save_to_file(FILENAME, csv_data)


if __name__ == '__main__':
    main()
