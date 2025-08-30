import re
import os
from student import student_list, add_student

# LOGIN
def lecturer_login():
    with open("lecturer.txt", "r") as file:
        lecturers = [line.strip().split(",") for line in file]

    while True:
        username = input("Enter Lecturer Email: ").strip()
        password = input("Enter Password: ").strip()

        found = False
        for lecturer in lecturers:
            email, pwd, name, phone, dept = lecturer

            if email == username and pwd == password:
                print(f"\nWelcome {name} ({dept} Department)!\n")
                lecturer_menu(email, name, phone, dept)
                found = True
                break

        if found:
            break
        else:
            print("Invalid username or password. Please try again.")


# MENU
def lecturer_menu(email, name, phone, dept):
    while True:
        print(f'''
===== Lecturer Menu ({name} - {dept}) =====
1. Profile
2. View Student List
3. Add Student
4. View Appeals
5. Logout
''')
        try:
            choice = int(input(">> Select: "))

            if choice == 3:
                print("Entering...")
                add_student()

            elif choice == 1:
                print('Entering Profile...')
                lecturer_profile(email, name, phone, dept)

            elif choice == 2:
                print("Viewing student list...")
                student_list()

            elif choice == 4:
                print('Checking Appeals')
                appeal_list()

            elif choice == 5:
                print("Logging out...\n")
                break

            else:
                print("Invalid option, try again.")

        except ValueError:
            print("Enter a number only.")


# PROFILE
def lecturer_profile(email, name, phone, dept):
    print('\n=== Lecturer Profile ===')
    print(f'Email: {email}')
    print(f'Full Name: {name}')
    print(f'Phone Number: {phone}')
    print(f'Department: {dept}')

    try:
        print('''
1. Update Profile
2. Return
''')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            print('Entering Update Menu: ')
            update_lecturer_profile(email, name, phone, dept)

        elif choice == 2:
            print('Leaving')
            return
        
        else:
            print('Invalid Option, Try Again')

    except ValueError:
        print("Enter a number only.")
            

# UPDATE PROFILE
def update_lecturer_profile(email, name, phone, dept):
    print('\nUpdate Profile:')
    print('1. Change Full Name')
    print('2. Change Phone Number')
    print('3. Change Department')
    print('4. Change Password')

    choice = input('Enter your choice: ').strip()

    new_name, new_phone, new_dept, new_password = name, phone, dept, None

    if choice == '1':
        while True:
            new_name = input('Enter Full Name: ').strip()
            
            if re.match(r'^[A-Za-z ]+$', new_name):
                break
            print('Invalid name. Use letters and spaces only.')

    elif choice == '2':
        while True:
            new_phone = input('Enter Phone Number (e.g. 601XXXXXXXX): ').strip()

            if re.match(r'^601\d{7,9}$', new_phone):
                break
            print('Invalid phone number. Format must be 601XXXXXXXX.')

    elif choice == '3':
        while True:
            new_dept = input('Enter Department: ').strip()

            if re.match(r'^[A-Za-z ]+$', new_dept):
                break
            print('Invalid department. Letters and spaces only.')

    elif choice == '4':
        while True:
            current_password = input('Enter Current Password: ').strip()

            with open('lecturer.txt', 'r') as file:
                lecturers = [line.strip().split(',') for line in file]
            stored_password = None

            for lec in lecturers:

                if lec[0].lower() == email.lower():
                    stored_password = lec[1]
                    break

            if stored_password and current_password == stored_password:
                new_password = input('Enter New Password (min 5 chars): ').strip()
                confirm_password = input('Confirm New Password: ').strip()

                if len(new_password) >= 5 and new_password == confirm_password:
                    break

                print('Passwords do not match or too short.')
            else:
                print('Incorrect current password.')
                return
    else:
        print('Invalid choice.')
        return

    # SAVE UPDATES
    try:
        with open('lecturer.txt', 'r') as file:
            lecturers = [line.strip().split(',') for line in file]

        with open('lecturer.txt', 'w') as file:
            for lec in lecturers:
                if lec[0].lower() == email.lower():
                    lec[2] = new_name
                    lec[3] = new_phone
                    lec[4] = new_dept
                    if new_password:
                        lec[1] = new_password
                file.write(','.join(lec) + '\n')

        print('Profile updated successfully.')

    except FileNotFoundError:
        print('Lecturer records not found.')


# APPEALS
def appeal_list():
    print('\n=== Appeal List ===')

    try:
        with open('appeal.txt', 'r') as file:
            appeals = file.readlines()

    except FileNotFoundError:
        print('No appeals found.')
        return

    for idx, appeal in enumerate(appeals, 1):
        parts = appeal.strip().split('|')
        if len(parts) >= 4:
            print(f'{idx}. Name: {parts[0]}, Grade: {parts[1]}, Reason: {parts[2]}, Date: {parts[3]}')

# TEST RUN