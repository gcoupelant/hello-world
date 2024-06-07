import argparse

from colorama import Fore

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", action="store_true", help="Print the text in red")
    parser.add_argument("--green", action="store_true", help="Print the text in green")
    parser.add_argument("--blue", action="store_true", help="Print the text in blue")
    args = parser.parse_args()

    color = ""
    if args.red:
        color = Fore.RED
    if args.green:
        color = Fore.GREEN
    if args.blue:
        color = Fore.BLUE

    print(color + "Hello World")
