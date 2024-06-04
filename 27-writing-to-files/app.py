from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'employees.txt'

employee_file = open(file_location, "a")

employee_file.write("Toby - Human Resources\n")
employee_file.write("Kelly - Customer Service\n")

employee_file.close()

employee_file = open(file_location, "w")

employee_file.write("Toby - Human Resources\n")
employee_file.write("Kelly - Customer Service\n")

employee_file.close()