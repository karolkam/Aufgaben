"""Das Ziel dieser Aufgabenserie ist es, einen Taschenrechner zu erstellen,
welcher zwei Zahlen vom Benutzer abfragt. Die Zahlen sollen dann die
Eingabe der mathematischen Grundfunktionen (Addition, Subtraktion,
Multiplikation und Division) bilden. Da Sie den Umgang mit Rechnungen,
Typkonvertierungen und Textausgabe bereits kennengelernt haben, sollen die
Resultate der Rechnungen wie im folgenden Beispiel tabellarisch dargestellt
werden (First number und Second number stellen die Eingabe des Benutzers
dar)."""

print('Aufgabenserie_C\n')
# die Funktion aufgaben(number_1, number_2)  führt arithmetische Operationen mit den Zwei gewähle Zahlen durch,
# und stellt die Tabelle mit der Ergebnisse dar.
number_1 = float(input('Please insert first number: '))
number_2 = float(input('Please insert second number: '))


def aufgaben(number_1, number_2):
    result_addition = number_1 + number_2
    result_subtraktion = number_1 - number_2
    result_multiplication = number_1 * number_2
    result_division = number_1 / number_2

    # man ruft die gewählte Zahlen auf
    print(colorama.Fore.CYAN, "First number:\t", number_1)
    print(colorama.Fore.BLUE, "Second number:\t", number_2, "\n", Style.RESET_ALL)

    # Tabelle
    width = 75
    print(colorama.Fore.LIGHTRED_EX, ("-" * 30) + " RESULTS " + ("-" * 36))
    print(colorama.Fore.YELLOW, "|\t\t  + \t\t" + " |" + "\t\t- \t\t" + " |" + "\t\t* \t\t" + " |" + "\t\t/")
    print(colorama.Fore.LIGHTRED_EX, "-" * width, Style.RESET_ALL)

    print(colorama.Back.BLACK, "|{:4s} {:7s} | {:4s} {:8s} | {:4s} {:8s} | {:1s} {:18s}".format(" int\t\t",
         str(int(result_addition)), "\t", str(int(result_subtraktion)), "\t", str(int(result_multiplication)), "\t",
             str(int(result_division))), Style.RESET_ALL)

    print(colorama.Back.LIGHTBLACK_EX, "|{:5s} {:7s} | {:4s} {:8s} | {:4s} {:8s} | {:1s} {:18s}".format(" float\t",
        str(round(float(result_addition), 2)), "\t", str(round(float(result_subtraktion), 2)), "\t",
            str(round(float(result_multiplication), 2)), "\t", str(round(float(result_division), 10))), Style.RESET_ALL)

    print(colorama.Back.BLACK, "|{:7s}{:1s}{:7s} | {:4s}{:1s}{:8s} | {:4s}{:1s}{:8s} | {:1s}{:1s}{:18s}"
        .format(" string \t", "~", str(int(result_addition)), "\t", "~", str(int(result_subtraktion)), "\t", "~",
            str(int(result_multiplication)), "\t", "~", str(int(result_division))), Style.RESET_ALL)


import colorama
from colorama import Style

if number_2 == 0:
    print(colorama.Fore.RED + "Division by 0 is not allowed", Style.RESET_ALL)
    number_2 = float(input('You can insert one more time second number: '))
    if number_2 != 0:
        aufgaben(number_1, number_2)
    else:
        print(colorama.Fore.RED + "Division by 0 is not allowed.\nIt was your last chance!", Style.RESET_ALL)

else:
    aufgaben(number_1, number_2)
