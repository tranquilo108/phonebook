import os
import view

def add_contact():
    os.system('cls' if os.name == 'nt' else 'clear')
    view.title('Add contact')
    first_name = input('Input first name: ')
    last_name = input('Input last name: ')
    phone = input('Input phone: ')
    contact = first_name + ' ' + last_name + ' ' + phone + '\n'
    file = open('file.txt', 'a', encoding='utf-8')
    file.write(contact)
    file.close()
    return contact
    

def find():
    view.title('Find contact','not')
    f = input('\nFind: ').upper()
    lines = reed_phonebook()
    cnt = 0
    lst = []
    for line in lines:
        if f in line.upper():
            cnt += 1
            lst.append(line)
    if cnt == 0:
        lst.append('error find contact')
    return lst

def reed_phonebook():
    file = open('file.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    lst = []
    for line in lines:
        lst.append(line)
    file.close()
    return lst

def delete(st):
    lines = reed_phonebook()
    file = open('file.txt', 'w', encoding='utf-8')
    for line in lines:
        if st not in line:
            file.write(line)
    file.close()

def edit(st):
    lines = reed_phonebook()
    file = open('file.txt', 'w', encoding='utf-8')
    for i in range(len(lines)):
        if st in lines[i]:
            lines[i] = lines[i].replace(st, add_contact())
            file.write(lines[i])
        else:
            file.write(lines[i])
    file.close()

def press_any_key():
    if os.name == 'nt':
        os.system('pause')
    else:
        os.system('read -s -n 1 -p "Press any key to  continue ..."')

def get_int_input(st=''):
    while True:
        try:
            value = int(input(st))
            return value
        except ValueError:
            print('Invalid input. Please enter an integer.')

def memu_2(line):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        view.find_menu(line.replace('\n', ''))
        find_choice = get_int_input()
        if find_choice == 1:
            edit(line)
            break
        elif find_choice == 2:
            delete(line)
            break
        elif find_choice == 0:
            break
        else:
            print('Input error')
            press_any_key()
