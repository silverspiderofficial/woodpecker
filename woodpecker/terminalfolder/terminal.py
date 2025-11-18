#asciiart import
import sys
from asciiart import silverspiderascii as asciiart2

def asci():
    asciiart2.showtime()

#helpmenu
def help_menu():
    print("-- HELP MENU :")
    print(" - help : help")
    print(" - exit : exit")
    

def printbossmessage(message):
        print(message+"\n")
# terminal start
def interactive_terminal():
    print("--- Hi , Type 'exit' to exit terminal and 'help' to see help\n")
    help_menu()

    while True:
        command = input(">>> ").strip()

        if command == "exit":
            print("OK,GOODBYE...")
            sys.exit(0)

        elif command == "help":
            help_menu()

        else:
            print("WHAT ????")
            


