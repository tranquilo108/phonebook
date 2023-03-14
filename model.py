def add_contact():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию:')
    phone = input("Введите телефон:")
    file = open("file.txt", "a")
    file.write(first_name + ' ')
    file.write(last_name + ' ')
    file.write(phone + '\n')
    file.close()

def find():
    # file = open("file.txt", "r")
    # f = input("")
    # lines = file.readlines()
    lines = read_phonebook()
    for line in lines:
        if f in line:
            print(line)
        else:
            print("Контакт ненайден")

def read_phonebook():
    file = open("file.txt", "r")
    lines = file.readlines()
    mat_line = []
    for line in lines:
        mat_line.append(line)
    file.close()
    return mat_line