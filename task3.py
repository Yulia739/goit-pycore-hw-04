from sys import argv
from pathlib import Path
from colorama import Fore, Style


def print_directory_contents(directory, level=0):
    '''
    This function displays all files and directory from given directory
    '''
    prefix = "\t" * level
    print(Fore.BLUE + f"{prefix}{directory.name}/" + Style.RESET_ALL)
    for path in directory.iterdir():
        if path.is_dir():
            print_directory_contents(path, level + 1)
        else:
            print(Fore.LIGHTMAGENTA_EX + f"{prefix}\t{path.name}" + Style.RESET_ALL)


print_directory_contents(Path(argv[1]))
