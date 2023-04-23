import checker
import generator
import statistics
import channel
import numpy as np

csv_data = []
FILENAME = "ARQ_results_parity_bit.csv"
PACKAGE_LENGTH = 8
NUMBER_OF_PACKAGES = 10000


statistics.clear_file(FILENAME)

for probability in np.arange(0.8, 0, -0.01):
    packages = generator.create_packages_with_parity_bit(NUMBER_OF_PACKAGES, PACKAGE_LENGTH)

    # statistics
    arq_requests = 0
    correct_returns = 0

    for package in packages:
        return_package = channel.disrupted_package(package, probability)
        while not checker.check_parity_bit(return_package, PACKAGE_LENGTH):
            return_package = channel.disrupted_package(package, probability)

            arq_requests += 1
        if checker.check_if_packages_are_the_same(package, return_package):
            correct_returns += 1

    percentage = (correct_returns / NUMBER_OF_PACKAGES) * 100
    data = (round(probability, 2), arq_requests, correct_returns, round(percentage, 2))
    csv_data.append(data)

statistics.save_to_file(FILENAME, csv_data)