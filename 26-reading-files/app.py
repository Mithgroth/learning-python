from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'employees.txt'

print(file_location)

employee_file = open(file_location, "r")

print(employee_file.read())

# returns nothing because it works with a cursor, and read() moves the cursor to the end
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readlines())

# can open the file again to reset cursor, throws no exceptions
employee_file = open(file_location, "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()