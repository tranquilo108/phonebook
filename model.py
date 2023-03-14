def add_contact():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию:')
    phone = input("Введите телефон:")
    file = open("file.txt", "a", encoding='utf-8')
    file.write(first_name + ' ')
    file.write(last_name + ' ')
    file.write(phone + '\n')
    file.close()

def find():
    f = input("Введите элемент поиска")
    lines = read_phonebook()
    for line in lines:
        if f in line:
            return line
        else:
            return "Контакт не найден "

def read_phonebook():
    file = open("file.txt", "r", encoding='utf-8')
    lines = file.readlines()
    mat_line = []
    for line in lines:
        mat_line.append(line)
    file.close()
    return mat_line