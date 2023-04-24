import os

from arq_tests import arq_crc, arq_parity_bit, no_arq
import stats


class Menu:
    def __init__(self, title, items):
        self.title = title
        self.items = items

        self.package_length = 8
        self.number_of_packages = 10
        self.n = 8
        self.divisor = "111010101"

    def display(self, title, items):
        self.clear_console()
        print("package length: ", self.package_length)
        print("number of packages: ", self.number_of_packages)
        print("n: ", self.n)
        print("divisor: ", self.divisor)

        print()
        print("++++++++++++++++")
        print("   " + title)
        print("++++++++++++++++")

        for i in range(len(items)):
            print(f"{i+1}. {items[i]}")

    def get_choice(self):
        choice = int(input("Choose option: "))
        return choice

    def get_int_input(self, message):
        return int(input(message))

    def get_string_input(self, message):
        return input(message)

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def change_settings(self):
        self.display("Settings", [
                     "Set number of packages", "Set package length", "Set n", "Set divisor", "Exit"])

        choice = self.get_choice()
        if choice == 1:
            self.number_of_packages = self.get_int_input(
                "Enter number of packages: ")
        elif choice == 2:
            self.package_length = self.get_int_input("Enter package length: ")
        elif choice == 3:
            self.n = self.get_int_input("Enter n: ")
        elif choice == 4:
            self.divisor = input("Enter divisor: ")
        elif choice == 5:
            pass
        else:
            print("Wrong choice!")

    def run(self):
        while (True):
            self.display(self.title, self.items)
            choice = self.get_choice()

            if choice == 1 or choice == 2 or choice == 3:
                filename = self.get_string_input("Enter filename: ")

            if choice == 1:
                stats.save_to_file(filename, arq_crc(self.package_length, self.number_of_packages,
                                                     self.n, self.divisor))
            elif choice == 2:
                stats.save_to_file(filename, arq_parity_bit(
                    self.package_length, self.number_of_packages))
            elif choice == 3:
                stats.save_to_file(filename, no_arq(
                    self.package_length, self.number_of_packages))
            elif choice == 4:
                self.change_settings()
            elif choice == 5:
                break
            else:
                print("Wrong choice!")
