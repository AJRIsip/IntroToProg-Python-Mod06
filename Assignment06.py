# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Alvin Jappeth Isip,11/23/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"


students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

# Define the Data Variables and constants
#student_first_name: str = ''  # Holds the first name of a student entered by the user.
#student_last_name: str = ''  # Holds the last name of a student entered by the user.
#course_name: str = ''  # Holds the name of a course entered by the user.
#student_data: dict = {}  # one row of student data

#csv_data: str = ''  # Holds combined string data separated by a comma.
#json_data: str = ''  # Holds combined string data in a json format.
#file = None  # Holds a reference to an opened file.

# Processing --------------------------------------- #
class FileProcessor:

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(FILE_NAME, "r")
            student_data = json.load(file)
            file.close()

        except FileNotFoundError as e:
            IO.output_error_messages("JSON file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        # global file
        # global students

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for row in students:
                print(f"FirstName: {row['FirstName']} LastName: {row['LastName']} CourseName: {row['CourseName']}")

        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


# Present and Process the data
class IO:

    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


    @staticmethod
    def output_menu(menu: str):
        """ This function displays the a menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :return: None
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        menu_choice = "0"

        try:
            menu_choice = input("What would you like to do: ")
            if menu_choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):

        print()
        print("-" * 50)
        for student in student_data:
            message = " {} {} is enrolled in {}"
            print(message.format(student["FirstName"], student["LastName"], student["CourseName"]))
            #print(f'Student {student["FirstName"]} '
            #      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
    # Input user data
        if menu_choice == "1":  # This will not work if it is an integer!

            try:
                student_first_name = input("Enter the student's first name: ")
                if not student_first_name.isalpha():
                    raise ValueError("The last name should not contain numbers.")
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha():
                    raise ValueError("The last name should not contain numbers.")
                course_name = input("Please enter the name of the course: ")
                student = {"FirstName": student_first_name,
                                "LastName": student_last_name,
                                "CourseName": course_name}
                student_data.append(student)
                print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

            except ValueError as e:
                IO.output_error_messages("That value is not the correct type of data!", e)
            except Exception as e:
                IO.output_error_messages("There was a non-specific error!", e)
            return student_data

    #  End of function definitions

# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Get new data (and display the change)
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":  # Display current data
        IO.output_student_courses(student_data=students)  # Added this to improve user experience
        continue

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop

