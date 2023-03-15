from os import name


def greeting():
    print('Weolcome to the phonebook program. \n')

def menu():
    print('********************************\n           Phonebook\n********************************\n\n 1. Find\n 2. Add contact\n 3. Show phonebook\n 4. Quit\n')

def show_phonebook():
    path = 'file.txt'
    file = open(path, 'r', encoding='utf-8')
    print('\n********************************\n')
    for line in file:
        print(line)
    file.close
    print('\n********************************')

def find_menu():
    print('********************************\n             Choice\n********************************\n\n 1. Edit contact\n 2. Delete contact\n 3. Return menu\n')
