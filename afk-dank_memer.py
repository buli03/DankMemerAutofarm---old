from pynput.keyboard import Key, Controller
import time
import array

keyboard =Controller()

def pobieranie_danych():
    n = input("Prosze podac liczbe komend: ")
    n = int(n)
    for _ in range(0,n):
        komenda = input("Prosze podac komende: ")
        commands.append(komenda)
    print(" ")
def coutdown():
    for liczba in odliczanie:
        time.sleep(1)
        print(liczba)

commands = []
odliczanie = [10,9,8,7,6,5,4,3,2,1]

pobieranie_danych()

print("Program will start in...")
coutdown()

print("Press Ctrl-C to stop the program")

loop = 0
number_of_commands = 0
wait_time = 2 #change the wait time between each command
number_of_commands_entered = 0

try:
    while True:
        print(" ")
        loop = loop + 1
        for komenda in commands:
            time.sleep(wait_time)
            keyboard.type(komenda)
            keyboard.press(Key.enter)
            number_of_commands = number_of_commands + 1
        print("Number of commands written: ",number_of_commands)
        print("Number of loops done: ",loop)
        number_of_commands_entered = len(commands)
        how_much_timne_left = 45 - (number_of_commands_entered * wait_time)
        print(" ")
        print("Waiting ",how_much_timne_left," seconds to write down next commands...")
        print("---------------------------------------------------")
        time.sleep(how_much_timne_left)

except KeyboardInterrupt:
    print("Program has been terminated...")
    pass