
# Student Login

def student_login():
    while True:
        username = input('Enter Studen ID: ')
        password = input('Enter Password: ')

        try:
            with open('C:/Users/Cale/Documents/PWP/Assignment/student.txt', 'r') as file:
                lecturers = file.readlines()
        except FileNotFoundError:
            print('FILE NOT FOUND')
            return

        for lecturer in lecturers:
            stored_username, stored_password = lecturer.strip().split(',')
            if username == stored_username and password == stored_password:
                print('========== Login Successful! ==========')
                student_menu()
                return

        print('Invalid ID or Password.')

# Student Menu

def student_menu():
    while True:
        print('''
SM University: Student's Menu
    1. Student Profile
    2. View Grades
    3. Return to Main Menu''')
     
        try:    
            choice = int(input('Select option >> '))

            if choice == 1 :
                print('Entering Profile...')
                # student_profile()
                break
        
            elif choice == 2 :
                print('Viweing Grades...')
                # view_grades()
                break
            
            elif choice == 3:
                print('Returning....')
                from menu import main_menu
                main_menu()
                break

            else:
                print('Invalid Input, Try Again')

        except ValueError:
            print('Invalid Input! Please enter a number.')
    