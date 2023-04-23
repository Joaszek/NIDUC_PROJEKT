import random


def disrupted_package(package, probability):
    changed_package = ""
    for bit in package:
        x = random.uniform(0, 1)
        if x < probability:
            if bit == '1':
                changed_package = changed_package + '0'
            else:
                changed_package = changed_package + '1'
        else:
            changed_package = changed_package + bit
    return changed_package
