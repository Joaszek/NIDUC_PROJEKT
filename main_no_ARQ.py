import generator
import channel
import statistics
import checker
import numpy as np

csv_data = []
FILENAME = "ARQ_results_no_arq.csv"
PACKAGE_LENGTH = 8
NUMBER_OF_PACKAGES = 10


def main():
    statistics.clear_file(FILENAME)

    for probability in np.arange(0.8, 0, -0.01):

        packages = generator.create_packages_with_parity_bit(NUMBER_OF_PACKAGES, PACKAGE_LENGTH)

        # statistics
        incorrect_return_packages = 0
        correct_return_packages = 0

        for package in packages:
            return_package = channel.disrupted_package(package, probability)

            if checker.check_if_packages_are_the_same(package, return_package):
                correct_return_packages += 1
            else:
                incorrect_return_packages += 1

        percentage_correct = correct_return_packages / NUMBER_OF_PACKAGES * 100
        percentage_incorrect = incorrect_return_packages / NUMBER_OF_PACKAGES * 100

        data = (round(probability, 2), correct_return_packages, round(percentage_correct, 2), incorrect_return_packages, round(percentage_incorrect, 2))
        csv_data.append(data)

    statistics.save_to_file(FILENAME, csv_data)


if __name__ == '__main__':
    main()
