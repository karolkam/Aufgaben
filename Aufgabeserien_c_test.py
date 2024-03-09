"""Das Ziel dieser Aufgabenserie ist es, einen Taschenrechner zu erstellen,
welcher zwei Zahlen vom Benutzer abfragt. Die Zahlen sollen dann die
Eingabe der mathematischen Grundfunktionen (Addition, Subtraktion,
Multiplikation und Division) bilden. Da Sie den Umgang mit Rechnungen,
Typkonvertierungen und Textausgabe bereits kennengelernt haben, sollen die
Resultate der Rechnungen wie im folgenden Beispiel tabellarisch dargestellt
werden (First number und Second number stellen die Eingabe des Benutzers
dar)."""

print('Aufgabenserie_C\n')
number_1 = float(input('Please insert first number: '))
number_2 = float(input('Please insert second number: '))
print("\n")

import colorama
from colorama import Fore, Back, Style

if number_2 == 0:
    print(colorama.Fore.RED + "Division by 0 is not allowed")
    print(Style.RESET_ALL)
    number_2 = float(input('You can insert one more time second number: '))
    print("\n")
    if number_2 != 0:
        result_addition = number_1 + number_2
        result_subtraktion = number_1 - number_2
        result_multiplication = number_1 * number_2
        result_division = number_1 / number_2
        print(colorama.Fore.YELLOW, "First number:\t", number_1)
        print(colorama.Fore.MAGENTA, "Second number:\t", number_2)
        print(Style.RESET_ALL)
        width = 75
        print("-" * width)
        print("|\t\t + \t\t" + " |" + "\t\t- \t\t" + " |" + "\t\t* \t\t" + " |" + "\t\t/ \t\t")
        print("_" * width)

        print("|{:5s} {:7s} | {:4s} {:8s} | {:4s} {:8s} | {:1s} {:33s}" .format(" int\t", str(int(result_addition)), "\t", str(int(result_subtraktion)), "\t", str(int(result_multiplication)), "\t", str(int(result_division))))
        print("|{:5s} {:7s} | {:4s} {:8s} | {:4s} {:8s} | {:1s} {:33s}" .format(" float\t", str(round(float(result_addition), 2)), "\t", str(round(float(result_subtraktion), 2)), "\t", str(round(float(result_multiplication), 2)), "\t", str(round(float(result_division), 10))))
        print("|{:6s}{:1s}{:6s} | {:4s}{:1s}{:8s} | {:4s}{:1s}{:8s} | {:1s}{:1s}{:33s}" .format(" string ", "~", str(int(result_addition)), "\t", "~", str(int(result_subtraktion)), "\t", "~", str(int(result_multiplication)), "\t", "~", str(int(result_division))))
    else:
        print(colorama.Fore.RED + "Division by 0 is not allowed.\nIt was your last chance! ")
        print(Style.RESET_ALL)
else:
    result_addition = number_1 + number_2
    result_subtraktion = number_1 - number_2
    result_multiplication = number_1 * number_2
    result_division = number_1 / number_2

    print(colorama.Fore.CYAN, "First number:\t", number_1)
    print(colorama.Fore.BLUE, "Second number:\t", number_2)
    print(Style.RESET_ALL)
    width = 75
    print("_" * width)
    print("|\t\t + \t\t" + " |" + "\t\t- \t\t" + " |" + "\t\t* \t\t" + " |" + "\t\t/ \t\t")
    print("_" * width)

    print("|{:5s} {:7s} | {:4s} {:8s} | {:4s} {:8s} | {:4s} {:13s}" .format(" int\t", str(int(result_addition)), "\t", str(int(result_subtraktion)), "\t", str(int(result_multiplication)), "\t", str(int(result_division))))
    print("|{:5s} {:7s} | {:4s} {:8s} | {:4s} {:8s} | {:4s} {:13s}" .format(" float\t", str(round(float(result_addition), 2)), "\t", str(round(float(result_subtraktion), 2)), "\t", str(round(float(result_multiplication), 2)), "\t", str(round(float(result_division), 15))))
    print("|{:6s}{:1s}{:6s} | {:4s}{:1s}{:8s} | {:4s}{:1s}{:8s} | {:4s}{:1s}{:13s}" .format(" string ", "~", str(int(result_addition)), "\t", "~", str(int(result_subtraktion)), "\t", "~", str(int(result_multiplication)), "\t", "~", str(int(result_division))))