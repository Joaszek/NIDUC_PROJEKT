# Description: This file contains the function that simulates the channel

from randGen import RandGen
import time


def disrupted_package(package, probability):
    changed_package = ""
    random = RandGen(time.time())
    for bit in package:
        x = random.generate_zero_to_one()
        if x < probability:
            if bit == '1':
                changed_package += '0'
            else:
                changed_package += '1'
        else:
            changed_package += bit

    return changed_package
