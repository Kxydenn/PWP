import re

# STUDENT LOGIN
def student_login():
    try:
        with open("student.txt", "r") as file:
            students = [line.strip().split(",") for line in file]
    except FileNotFoundError:
        print("No student records found.")
        return

    while True:
        username = input("Enter Student Email: ").strip()
        password = input("Enter Password: ").strip()

        found = False
        for index, student in enumerate(students):
            if len(student) < 6:
                continue
            email, pwd, name, phone, course, score = student

            if email == username and pwd == password:
                print(f"\nWelcome {name} ({course})!\n")
                student_menu(name, course, index)
                found = True
                break

        if found:
            break
        else:
            print("Invalid username or password. Please try again.")


# MENU
def student_menu(name, index):
    while True:
        print(f'''
===== Student Menu ({name}) =====
1. Profile
2. Check Grades
3. Appeals
4. Logout
''')
        try:
            choice = int(input(">> Select: "))
            if choice == 1:
                print("Showing Profile...")
                student_profile(index)

            elif choice == 2:
                print("Showing Grades...")
                view_grades(index)

            elif choice == 3:
                print('Entering Appeals...')
                appeal_menu(index)

            elif choice == 4:
                print("Logging out...\n")
                break

            else:
                print("Invalid option, try again.")

        except ValueError:
            print("Enter a number only.")


# STUDENT PROFILE
def student_profile(index):
    try:
        with open('student.txt', 'r') as file:
            lines = file.readlines()

        if index < 0 or index >= len(lines):
            print('Invalid Line')
            return

        parts = lines[index].strip().split(',')

        if len(parts) >= 6:
            username, _, full_name, number, studies, _ = parts

            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', username):
                email_status = '(Invalid Email Format)'
            else:
                email_status = ''

            print(f'''
Student Profile:
    Name: {full_name}
    Study: {studies}
    Email: {username} {email_status}
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
What would you like to change?
    1. Name
    2. Phone Number
    3. Field of Study
    4. Password
    5. Cancel
''')

        choice = input('Select option (1-5): ').strip()

        if choice == '1':  # Change Name
            while True:
                new_name = input('Enter Name: ').strip()

                if re.match(r'^[A-Za-z ]+$', new_name):
                    parts[2] = new_name
                    break
                print('Name should only contain letters and spaces.')

        elif choice == '2':  # Change Number
            while True:
                new_number = input('Enter New Number (format: 601XXXXXXXX): ').strip()

                if re.match(r'^601\d{7,9}$', new_number):
                    parts[3] = new_number
                    break
                print('Invalid phone number. Use format: 601XXXXXXXX.')

        elif choice == '3':  # Change Study
            while True:
                new_study = input('Enter New Study: ').strip()

                if re.match(r'^[A-Za-z &]+$', new_study):
                    parts[4] = new_study
                    break
                print("Field of study must only contain letters, spaces, or '&'.")

        elif choice == '4':  # Change Password
            current_password = input('Enter Current Password: ').strip()

            if current_password != parts[1]:
                print('Incorrect password.')
                return

            while True:
                new_password = input('Enter New Password: ').strip()
                confirm_password = input('Confirm New Password: ').strip()

                if new_password != confirm_password:
                    print('Passwords do not match. Try again.')
                    continue

                if len(new_password) >= 6:
                    parts[1] = new_password
                    break
                print('Password must be at least 6 characters long.')

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

            if not re.match(r'^\d+(\.\d+)?$', grade_str):
                print('Invalid grade data. Must be numeric.')
                return

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

    input("\nPress Enter to return...")


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
                create_appeal(index)

            elif choice == 2:
                print('Entering...')
                check_appeal(index)

            elif choice == 3:
                print('Returning...')
                return

            else:
                print('Invalid Choice')

        except ValueError:
            print('Please enter a number.')


def create_appeal(index):
    try:
        with open('student.txt', 'r') as file:
            lines = file.readlines()
            parts = lines[index].strip().split(',')
            student_name = parts[2]
    except:
        print('Error retrieving student info.')
        return

    while True:
        grade = input('What grade are you appealing for? ').strip().upper()
        if grade not in ['A+', 'A', 'B+', 'B', 'C+', 'C', 'C-', 'D', 'D-', 'F']:
            print('Invalid grade. Must be A+, A, B+, B, C+, C, C-, D, D-, or F.')
            continue
        break

    while True:
        reason = input('Enter your reason for the appeal: ').strip()
        if len(reason) < 10:
            print('Reason must be at least 10 characters long.')
            continue
        break

    appeal_entry = f'{student_name},{grade},{reason}\n'

    try:
        with open('appeal.txt', 'a') as file:
            file.write(appeal_entry)
        print('Appeal submitted successfully.')

    except FileNotFoundError:
        print('Could not find appeal.txt.')


def check_appeal(index):
    try:
        with open('student.txt', 'r') as file:
            parts = file.readlines()[index].strip().split(',')
            student_name = parts[2]
    except:
        print('Error retrieving student info.')
        return

    try:
        with open('appeal.txt', 'r') as file:
            appeals = file.readlines()

        filtered = [a for a in appeals if a.startswith(student_name + ',')]

        if filtered:
            print('\n=== Your Appeals ===')
            for i, line in enumerate(filtered, 1):
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    grade = parts[1]
                    reason = ','.join(parts[2:])
                    print(f'\n{i}. Appealing Grade: {grade}\n   Reason: {reason}')
                else:
                    print(f'\n{i}. Incomplete appeal entry.')
        else:
            print('You have not submitted any appeals.')

    except FileNotFoundError:
        print('No appeal file found.')

# IMPORT FUNCTIONS

# STUDENT LIST
def student_list():
    print('\n=== Student List ===')

    try:
        with open('student.txt', 'r') as file:
            students = file.readlines()

    except FileNotFoundError:
        print('No student records found.')
        return

    for idx, student in enumerate(students, 1):
        parts = student.strip().split(',')

        if len(parts) >= 6:
            print(f"\n{idx}.")
            print(f"   Name:   {parts[2]}")
            print(f"   Email:  {parts[0]}")
            print(f"   Number: {parts[3]}")
            print(f"   Grade:  {parts[5]}")

    choice = input("\nDo you want to change a student's grade? (yes/no): ").strip().lower()

    if choice == 'yes':
        student_id = input('Enter Student Email to change grade: ').strip()
        change_grades(student_id)


# CHANGE GRADES
def change_grades(student_email):
    try:
        with open('student.txt', 'r') as file:
            students = file.readlines()

        updated = False
        with open('student.txt', 'w') as file:
            for student in students:
                parts = student.strip().split(',')

                if len(parts) >= 6 and parts[0].lower() == student_email.lower():
                    print(f"\nCurrent Grade for {parts[2]}: {parts[5]}")
                    new_grade = input("Enter new grade: ").strip()

                    try:
                        float(new_grade)
                        parts[5] = new_grade
                        updated = True
                        print(f"Grade updated successfully for {parts[2]} ({student_email}).")

                    except ValueError:
                        print("Invalid grade. Must be a number.")

                    file.write(','.join(parts) + "\n")
                else:
                    file.write(student)

        if not updated:
            print("Student not found.")

    except FileNotFoundError:
        print("Student records not found.")


# ADD STUDENT
def add_student():
    print('\n=== Add Student ===')

    while True:
        email = input('Enter Student Email: ').strip()
        if re.match(r'[^@]+@[^@]+\.[^@]+', email):
            break
        print('Invalid email format.')

    while True:
        password = input('Enter Password (min 5 chars): ').strip()
        confirm_password = input('Confirm Password: ').strip()
        if len(password) >= 5 and password == confirm_password:
            break
        print('Passwords must match and be at least 5 characters.')

    while True:
        full_name = input('Enter Full Name: ').strip()
        if re.match(r'^[A-Za-z ]+$', full_name):
            break
        print('Invalid name. Letters and spaces only.')

    while True:
        phone_number = input('Enter Phone Number (e.g. 601XXXXXXXX): ').strip()
        if re.match(r'^601\d{7,9}$', phone_number):
            break
        print('Invalid phone number format.')

    while True:
        studies = input('Enter Field of Study: ').strip()
        if re.match(r'^[A-Za-z ]+$', studies):
            break
        print('Invalid field of study. Letters and spaces only.')

    while True:
        score = input('Enter Score (0–100): ').strip()
        if score.replace('.', '', 1).isdigit():
            score = float(score)
            if 0 <= score <= 100:
                break
        print('Invalid score. Must be a number 0–100.')

    with open('student.txt', 'a') as file:
        file.write(f'{email},{password},{full_name},{phone_number},{studies},{score}\n')

    print('Student added successfully.')

# TEST RUN