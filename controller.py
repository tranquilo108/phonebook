import view
import model
def run():
    view.greeting()
    while True:
        view.menu()
        choice = int(input())
        match choice:
            case 1:
                model.find()
            case 2:
                model.add_contact()
            case 3:
                view.show_phonebook()
            case 4:
                break    
            case _:
                print('Введено неверное знаечние, попробуем снова =)')
                view.menu()