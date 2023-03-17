import model as processing
import view
import os

def run():
    view.greeting()
    processing.press_any_key()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        view.menu()
        choice = processing.get_int_input('Select a menu item: ')
        if choice == 1:
            a = processing.find()
            if a[0] == 'error find contact':
                view.show_string(a[0])
                processing.press_any_key()
            else:
                if len(a) == 1:
                    processing.memu_2(a[0])
                else:
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        view.show_list(a)
                        view.choice_contact_menu()
                        choice_contact = processing.get_int_input('Select the contact id: ')
                        if choice_contact == 0:
                            break
                        elif len(a) >= choice_contact >= 1:       
                            processing.memu_2(a[choice_contact-1])
                            break
                        else:
                            view.show_string('Invalid input.')
                            processing.press_any_key()
        elif choice == 2:
            processing.add_contact()
        elif choice == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            view.show_phonebook()
            processing.press_any_key()
        elif choice == 0:
            break
        else:
            view.show_string('Invalid input.')
            processing.press_any_key()