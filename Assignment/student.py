
# STUDENT LOGIN

def student_login():
    while True:
        username = input('Enter Student ID: ')
        password = input('Enter Password: ')

        try:
            with open('student.txt', 'r') as file:
                students = file.readlines()
        except FileNotFoundError:
            print('FILE NOT FOUND')
            return

        for index, line in enumerate(students):
            parts = line.strip().split(',')
            if len(parts) >= 2:
                stored_username = parts[0]
                stored_password = parts[1]
                if username == stored_username and password == stored_password:
                    print('========== Login Successful! ==========')
                    student_menu(index)
                    return

        print('Invalid ID or Password.')
        retry = input('Try again? (Y/N): ').lower()
        if retry != 'y':
            return



# STUDENT MENU

def student_menu(index):
    while True:
        print('''
              
SM University: Student's Menu
    1. Student Profile
    2. View Grades
    3. Appeals
    4. Return to Main Menu
''')
     
        try:    
            choice = int(input('Select option >> '))

            if choice == 1:
                print('Entering Profile...')
                student_profile(index)
        
            elif choice == 2:
                print('Viweing Grades...')
                view_grades(index)

            elif choice == 3:
                print('Entering Appeal Menu...')
                appeal_menu(index)
            
            elif choice == 4:
                print('Returning....')
                return

            else:
                print('Invalid Input, Try Again')

        except ValueError:
            print('Invalid Input! Please enter a number.')



# STUDENT PROFILE

def student_profile(index):
    try:
        with open('student.txt', 'r') as file:
            lines = file.readlines()

        if index < 0 or index >= len(lines):
            print('Invalid Line')
            return

        parts = lines[index].strip().split(',')

        if len(parts) >= 4:
            username = parts[0]
            full_name = parts[2]
            number = parts[3]
            studies = parts[4]

            print(f'''
                  
Student Profile:
    Name: {full_name}
    Study: {studies}
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
    2. Update Profile
>> '''))
            if choice == 1:
                print('Returning...')
                break

            elif choice == 2:
                print('Entering...')
                update_student_profile(index)

            else:
                print('Invalid choice.')

        except ValueError:
            print('Please enter a number.')



# UPDATE STUDENT PROFILE

def update_student_profile(index):
    try:
        with open('student.txt', 'r') as file:
            students = file.readlines()

        if index < 0 or index >= len(students):
            print('Invalid student index.')
            return

        parts = students[index].strip().split(',')

        if len(parts) < 6:
            print('Incomplete student data.')
            return

        print(f'''
              
Current Information:
    Name: {parts[2]}
    Number: {parts[3]}
    Study: {parts[4]}
    Password: {'*' * len(parts[1])}
''')

        print('''
              
What would you like to change?')
    1. Name
    2. Phone Number
    3. Field of Study
    4. Password
    5. Cancel

''')

        choice = input('Select option (1-5): ')

        if choice == '1':
            new_name = input('Enter Name: ')
            parts[2] = new_name

        elif choice == '2':
            new_number = input('Enter New Number: ')
            parts[3] = new_number

        elif choice == '3':
            new_study = input('Enter New Study: ')
            parts[4] = new_study

        elif choice == '4':
            current_password = input('Enter Current Password: ')

            if current_password != parts[1]:
                print('Incorrect password.')
                return
            
            new_password = input('Enter New Password: ')
            parts[1] = new_password

        elif choice == '5':
            print('Cancelled.')
            return

        else:
            print('Invalid choice.')
            return

        students[index] = ','.join(parts) + '\n'

        with open('student.txt', 'w') as file:
            file.writelines(students)

        print('Information updated successfully.')

    except FileNotFoundError:
        print('FILE NOT FOUND')



# VIEW GRADES

def view_grades(index):
    try:
        with open('student.txt', 'r') as file:
            lines = file.readlines()

        if index < 0 or index >= len(lines):
            print('Invalid Line')
            return

        parts = lines[index].strip().split(',')

        if len(parts) >= 6:
            full_name = parts[2]
            studies = parts[4]
            grade_str = parts[-1]

            grade_letter, remarks = grade_range(grade_str)

            print(f'''
                  
Student Profile:
    Name: {full_name}
    Study: {studies}
    Score: {grade_str}
    Grade: {grade_letter}
    Remarks: {remarks}
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
>> '''))
            if choice == 1:
                print('Returning...')
                break

            else:
                print('Invalid choice.')

        except ValueError:
            print('Please enter a number.')



# GRADE RANGE

def grade_range(score):

    try:
        score = float(score)
    except ValueError:
        return 'Invalid', 'Non-numeric score'
    
    grading_table = [
        (80, 100, 'A+', 'Excellent'),
        (75, 79.99, 'A', 'Very Good'),
        (70, 74.99, 'B+', 'Good'),
        (65, 69.99, 'B', 'Above Average'),
        (60, 64.99, 'C+', 'Average'),
        (55, 59.99, 'C', 'Pass'),
        (50, 54.99, 'C-', 'Marginal Pass'),
        (45, 49.99, 'D', 'Marginal Fail'),
        (40, 44.99, 'D-', 'Fail'),
        (0, 39.99, 'F', 'Fail')
    ]

    for low, high, grade, remark in grading_table:
        if low <= score <= high:
            return grade, remark
    return 'Invalid', 'Out of range'



# APPEAL

def appeal_menu(index):
    while True:
        try:
            choice = int(input('''
                               
What would you like to do?
    1. Create Appeal
    2. Check Appeal
    3. Return

>> '''))
            if choice == 1:
                print('Entering...')
                create_appeal()

            elif choice == 2:
                print('Entering...')
                check_appeal()

            elif choice == 3:
                print('Returning...')
                return
            
            else:
                print('Invalide Choice')

        except ValueError:
            print('Please enter a number.')



def create_appeal():

    name = input('Enter your full name: ').strip()
    grade = input('What grade are you appealing for? ').strip()
    reason = input('Enter your reason for the appeal: ').strip()

    appeal_entry = f'{name},{grade},Reason: {reason}\n'

    try:
        with open('appeal.txt', 'a') as file:
            file.write(appeal_entry)
        print('Appeal submitted successfully.')

    except FileNotFoundError:
        print('Could not find appeal.txt.')



def check_appeal():
    try:
        with open('appeal.txt', 'r') as file:
            appeals = file.readlines()

        if appeals:
            print('\n=== All Appeals ===')
            for i, line in enumerate(appeals, 1):
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    name = parts[0]
                    grade = parts[1]
                    reason = ','.join(parts[2:])
                    print(f'\n{i}. Name: {name}\n   Appealing Grade: {grade}\n   {reason}')
                else:
                    print(f'\n{i}. Incomplete appeal entry.')
        else:
            print('No appeals yet.')

    except FileNotFoundError:
        print('No appeal file found.')

# TEST RUN
