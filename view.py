import os


def greeting():
    print('Weolcome to the phonebook program. \n\n\n Version 2.0.0.1\n\n\n ')

def menu(tit = 'Menu Phonebook'):
    title(tit)
    print('\n 1. Find contact\n 2. Add contact\n 3. Show phonebook\n\n 0. Quit\n')

def show_phonebook():
    title('Phonebook', 'not')
    path = 'file.txt'
    file = open(path, 'r')
    print('id\tfirst name\tlast name\tphone\n')
    ind = 0
    for line in file:
        ind += 1
        temp = line.replace(' ', '\t\t')
        print(f'{ind}\t{temp}')
    file.close
    print(' ' + '-'*60)

def find_menu(tit = 'Choice'):
    title(tit)
    print(' 1. Edit contact\n 2. Delete contact\n\n 0. Return menu\n')

def choice_contact_menu(tit = 'Choice contact'):
    title(tit)
    print('\n  0. Return munu\n')

def show_list(lst):
    ind = 0
    title('Phonebook')
    print('id\tfirst name\tlast name\tphone\n')
    for item in lst:
        ind += 1
        temp = item.replace(' ', '\t\t')
        print(f'{ind}\t{temp}')

def show_string(st):
    print(st) 

def title(title, n=''):
    if n == 'not':
        os.system('cls' if os.name == 'nt' else 'clear')
    n = (60 - len(title))//2 
    tit = ' ' + '-'*60 + '\n|' + ' '*n + title + ' '*n + '|\n' + ' ' + '-'*60
    print(tit)