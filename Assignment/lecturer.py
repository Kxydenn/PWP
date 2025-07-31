
# LECTURER LOGIN

def lecturer_login():
    while True:
        username = input('Enter Lecturer ID: ')
        password = input('Enter Password: ')

        try:
            with open('C:/Users/Cale/Documents/PWP/Assignment/lecturer.txt', 'r') as file:
                lecturers = file.readlines()
        except FileNotFoundError:
            print('FILE NOT FOUND')
            return

        for index, line in enumerate(lecturers):
            parts = line.strip().split(',')
            if len(parts) >= 2:
                stored_username = parts[0]
                stored_password = parts[1]
                if username == stored_username and password == stored_password:
                    print('========== Login Successful! ==========')
                    lecturer_menu(index)
                    return

        print('Invalid ID or Password.')
        retry = input('Try again? (Y/N): ').lower()
        if retry != 'y':
            return

# LECTURER MENU

def lecturer_menu(index):

    while True:
        print('''
SM University: Lecturer's Menu
    1. Lecturer Profile
    2. Student List
    3. View Appeals
    4. Return to Main Menu''')
        
        try:
            choice = int(input('Select option >> '))

            if choice == 1:
                print('Entering Profile...')
                lecturer_profile(index)

            elif choice == 2:
                print('Entering Student List...')
                student_list(index)

            elif choice == 3:
                print('Checking Appeals...')
                # appeal_list()

            elif choice == 4:
                print('Returning to Main Menu...')
                return

            else:
                print('Invalid Input, Try Again')

        except ValueError:
            print('Invalid Input! Please enter a number.')

# VIEW PROFILE

def lecturer_profile(index):
    try:
        with open('C:/Users/Cale/Documents/PWP/Assignment/lecturer.txt', 'r') as file:
            lines = file.readlines()

        if index < 0 or index >= len(lines):
            print('Invalid Line')
            return

        parts = lines[index].strip().split(',')

        if len(parts) >= 4:
            username = parts[0]
            full_name = parts[2]
            number = parts[3]
            department = parts[4]

            print(f'''
Lecturer Profile:
    Name: {full_name}
    Department: {department}
    Email: {username}
    Number: {number}
    ''')
            
        else:
            print('Incomplete Data')

    except FileNotFoundError:
        print('FILE NOT FOUND')
        return

    while True:

        try:

            choice = int(input('''
Return?
    1. Yes
    2. No
>> '''))
            if choice == 1:
                print('Returning...')
                break

            elif choice == 2:
                print('Staying in Profile...')

            else:
                print('Invalid choice.')

        except ValueError:
            print('Please enter a number.')

# STUDENT LIST

def student_list(index):
    try:
        with open('C:/Users/Cale/Documents/PWP/Assignment/student.txt', 'r') as file:
            students = file.readlines()

        for line in students:
            parts = line.strip().split(',')

            if len(parts) >= 5:
                username = parts[0]
                full_name = parts[2]
                number = parts[3]
                studies = parts[4]
                grade = parts[-1]

                print(f'''
{full_name} Profile:
Grades: {grade}
Study: {studies}
Email: {username}
Number: {number}
''')
            else:
                print('Incomplete Data')

    except FileNotFoundError:
        print('FILE NOT FOUND')

    while True:

            try:

                choice = int(input('''
Return?
    1. Yes
OR
    2. Change Grades
>> '''))
                if choice == 1:
                    print('Returning...')
                    lecturer_menu(index)
                    break
                
                elif choice == 2:
                    print('Entering...')
                    change_grades(name = input('Enter Student Name: '))
                    break

                else:
                    print('Invalid choice.')

            except ValueError:
                print('Please enter a number.')

# CHANGE GRADES

def change_grades(name):
    try:
        with open('C:/Users/Cale/Documents/PWP/Assignment/student.txt', 'r') as file:
            students = file.readlines()

        found = False
        for i, line in enumerate(students):
            parts = line.strip().split(',')
            if len(parts) >= 5:
                full_name = parts[2]
                if name.lower() in full_name.lower():
                    print(f'Found: {full_name} (Current grade: {parts[-1]})')
                    new_grade = input('Enter new grade: ')
                    parts[-1] = new_grade
                    students[i] = ','.join(parts) + '\n'
                    found = True
                    break

        if found:
            with open('C:/Users/Cale/Documents/PWP/Assignment/student.txt', 'w') as file:
                file.writelines(students)
            print('Grade updated successfully.')
        else:
            print('Student not found.')

    except FileNotFoundError:
        print('FILE NOT FOUND')

# APPEAL LIST

# def appeal_list():

# TEST RUN
student_list(index = 0)