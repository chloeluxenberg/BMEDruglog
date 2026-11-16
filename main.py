from storage import load_data, save_data
from users  import (create_user, select_user)
from medications import add_medication, list_medications
from reminders import show_reminders
from otc import lookup_otc


def main():
    data = load_data()
    current_user = None
    while True:
        print('\n=== MEDICATION TRACKER ===')
        print('Current user:', data['users'][current_user]['name'] if current_user else 'None')
        print('1. Create user')
        print('2. Select user')
        print('3. Add medication')
        print('4. View medications')
        print('5. View reminder schedule')
        print('6. OTC lookup (coming soon)')
        print('7. Exit')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            create_user(data)
            save_data(data)
        elif choice == '2':
            selected = select_user(data)
            if selected is not None:
                current_user = selected
        elif choice in ('3', '4', '5'):
            if current_user is None:
                print('Please select a user first.')
                continue
            if choice == '3':
                add_medication(data, current_user)
                save_data(data)
            elif choice == '4':
                list_medications(data, current_user)
            else:
                show_reminders(data, current_user)
        elif choice == '6':
            lookup_otc()
        elif choice == '7':
            print('Goodbye!')
            break
        else:
            print('Invalid option. Try again.')


if __name__ == '__main__':
    main()