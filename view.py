from tabulate import tabulate
from model.assignment import Assignment
import sys
import os
from controller.mentor_controller import MentorController


class View:
    """Class which have methods for UI"""

    @staticmethod
    def student_menu():
        """
        Student Menu
        :return None
        """
        View.clear()
        print('''
        -----------MENU-----------
        1. List your assignments
        2. Submit assignment
        0. Exit
        ''')

    @staticmethod
    def main_menu():
        """
        Show main menu
        :param assignment_grades: list
        :returns username,password
        """
        View.clear()
        print('Welcome in CodeCool Management System')
        print('\nTo EXIT program press "0"\n')
        username = input('Enter your username:')
        if username == '0':
            sys.exit()
        password = input('Enter your password:')
        return username, password

    @staticmethod
    def mentor_menu():
        """
        Show mentor menu
        :return: None
        """
        View.clear()
        print('''
        -----------MENU-----------
        1. Check attendance
        2. Add assignment
        3. Grade assignment
        4. Add student
        5. Edit student
        6. Delete student
        7. View presence statistics
        0. Exit
        ''')

    @staticmethod
    def display_students(students_list):
        """
        Show students list
        :param students_list: list of students
        :return: None
        """
        for index, student in enumerate(students_list):
            print('{} {} {}'.format(index, student.first_name, student.last_name))

    @staticmethod
    def display_static_present(list_stat):
        """
        Show statistics of present of student
        :param list_stat: list of stats
        :return: None
        """
        if list_stat:
            for key, value in list_stat.items():
                print('{} {}'.format(key, value))

    @staticmethod
    def menager_menu():
        """
        Show manager menu
        :return: None
        """
        print('''
        -----------MENU-----------
        1. List mentors
        2. Add mentor
        3. Add assistant
        4. Edit mentor
        5. Delete mentor
        0. Exit
        ''')

    @staticmethod
    def employee_menu():
        """
        Show employee menu
        :return: None
        """
        View.clear()
        print('''
        -----------MENU-----------
        1. List student
        0. Exit
        ''')

    @staticmethod
    def show_user_details(user):
        """
        Show user details
        :param user: list
        :return: none
        """
        if user:
            headers = ['First name', 'Last name', 'User name', 'Phone Number', 'Mail']
            print(tabulate([list(user)], headers, tablefmt="fancy_grid"))
        else:
            print('There is ampty.')

    @staticmethod
    def print_assignment_grades(assignment_grades):
        """
        Show assignment grades
        :param assignment_grades: list
        :return None
        """
        if assignment_grades:
            headers = ['Assiment', 'Grade']
            print(tabulate(assignment_grades, headers,
                           tablefmt="fancy_grid", stralign="center"))
        else:
            print('There is ampty.')

    @staticmethod
    def print_assignments_list(assignments_list):
        """
        Print assigments list
        :param assignments_list: list
        :return: None
        """
        if assignments_list:
            headers = ['Title', 'Due_date', 'description']
            print(tabulate(assignments_list, headers, tablefmt="fancy_grid"))
        else:
            print('There is ampty.')

    @staticmethod
    def print_user_list(user_list):
        """
        Print user list
        :param assignments_list: list
        :return: None
        """
        if user_list:
            headers = ['Index', 'First name', 'Last name', 'User name']
            print(tabulate(user_list, headers, tablefmt="fancy_grid"))
        else:
            print('There is ampty.')

    @staticmethod
    def print_mentors_list(mentors_list):
        """
        Show mentor list
        :param mentors_list: list
        :return:
        """
        for mentor in mentors_list:
            print(mentor)

    @staticmethod
    def edit_menu():
        """
        Show edit menu for student
        :return: None
        """
        print('''
        You can edit following parameters:
            - telephone
            - mail
        ''')

    @staticmethod
    def show_full_name(user_list):
        """
        Show full name of user list
        :param user_list: user list
        :return: None
        """
        View.clear()
        n = 0
        for user in user_list:
            n += 1
            print('{}. {} {}'.format(n, user[0], user[1]))

    @staticmethod
    def print_two_demention_list(printed_list):
        """Print all 2 demention list

        """
        for index, sub_list in enumerate(printed_list):
            print('{}. {}'.format(index, ' - '.join(sub_list)))

    @staticmethod
    def show_details(user):
        """
        Show details of user
        :param user: list
        :return: None
        """
        print(
            '\n\t{} {}, phone number:{}, e-mail: {}'.format(user[0], user[1], user[3], user[4]))

    @staticmethod
    def clear():
        """
        Clears screen for better display
        :return None
        """
        os.system('cls' if os.name == 'nt' else 'clear')
