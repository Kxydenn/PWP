
# MAIN MENU

def main_menu():
    from lecturer import lecturer_login
    from student import student_login

    while True:
        print('''
                  
  ██████   ███████   ██████  
 ██       ██        ██       
  █████   ██   ███   █████   
      ██  ██    ██       ██  
 ██████   ███████   ██████   

SM University Student Grading System!
    1. Lecturer Menu
    2. Student Menu
    3. Exit''')
        
        try:
            choice = int(input('>> Select your menu: '))

            if choice == 1:
                print('''
========== User Login: Lecturer ==========
''') 
                lecturer_login()

            elif choice == 2:
                print('''
========== User Login: Student ==========
''')  
                student_login()

            elif choice == 3:
                print('Thank you! Exiting....')
                break

            else:
                print('Invalid Input, Try Again')

        except ValueError:
            print('Invalid Input! Please enter a number.')


# RUN
main_menu()