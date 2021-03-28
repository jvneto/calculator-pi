from decimal import Decimal, getcontext
import time
import pathlib

init_time = int(round(time.time()))


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


mode = input(f"{bcolors.HEADER}Operation mode: {bcolors.OKBLUE}\n(1 -> Calculation Time) \n(2 -> Console) \n(3 -> Write To File)\n{bcolors.ENDC}")
if mode != '1' and mode != '2' and mode != '3':
    print(f"{bcolors.FAIL}Incorrect Operating Mode!{bcolors.ENDC}")
else:

    if mode == '3':
        nameFile = input(f"{bcolors.HEADER}File Name: (pi.txt){bcolors.ENDC}")

    number = input(
        f"{bcolors.HEADER}Number of numbers after the comma: {bcolors.ENDC}")
    precision = input(f"{bcolors.HEADER}Precision (500): {bcolors.ENDC}")

    if number != "":
        if precision == "":
            precision = 500

        getcontext().prec = int(number)

        pi = sum(1/Decimal(16)**k * (Decimal(4)/(8*k+1) -
                                     Decimal(2)/(8*k+4) -
                                     Decimal(1)/(8*k+5) -
                                     Decimal(1)/(8*k+6)) for k in range(precision))

        if mode == '1':
            print(
                f'{bcolors.OKGREEN}Calculation Time: {int(round(time.time())) - init_time} Segundos!{bcolors.ENDC}')
        elif mode == '2':
            print(f'{bcolors.OKCYAN}{pi}{bcolors.ENDC}')
        elif mode == '3':
            if nameFile != "":
                open(nameFile + '.txt', 'w').write(str(pi))
                print(
                    f'{bcolors.WARNING}Created file path: {pathlib.Path(__file__).parent.absolute()}\{nameFile}.txt {bcolors.ENDC}')
            else:
                open('pi.txt', 'w').write(str(pi))
                print(
                    f'{bcolors.WARNING}Created file path: {pathlib.Path(__file__).parent.absolute()}\pi.txt {bcolors.ENDC}')
            print(f'{bcolors.OKGREEN}Success! Saved to File.{bcolors.ENDC}')
    else:
        print(
            f"{bcolors.FAIL}Number of numbers after the comma undefined!{bcolors.ENDC}")
