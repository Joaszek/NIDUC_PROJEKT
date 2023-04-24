from menu import Menu


def main():
    menuItems = ["arq crc", "arq parity bit",
                 "no arq", "change settings", "exit"]

    menu = Menu("Main menu", menuItems)

    menu.run()


if __name__ == '__main__':
    main()
