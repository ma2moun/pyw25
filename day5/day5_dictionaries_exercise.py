# Without functions....
# How can it be improved using functions?

# Step 1: Create a dictionary to store employee data
employees = {
    'E001': {'name': 'Hamad', 'position': 'Manager', 'salary': 5000},
    'E002': {'name': 'Al Yaman', 'position': 'Developer', 'salary': 4000},
    'E003': {'name': 'Mohammed', 'position': 'Designer', 'salary': 3500},
}

# Step 2: Add a new employee
new_id = input("Enter the new employee ID: ")
new_name = input("Enter the employee name: ")
new_position = input("Enter the employee position: ")
new_salary = int(input("Enter the employee salary: "))

employees[new_id] = {'name': new_name, 'position': new_position, 'salary': new_salary}
print(f"Employee {new_name} added successfully!")

# Step 3: Update the salary of an existing employee
update_id = input("Enter the employee ID to update salary: ")
if update_id in employees:
    new_salary = int(input("Enter the new salary: "))
    employees[update_id]['salary'] = new_salary
    print(f"Salary of {employees[update_id]['name']} updated successfully!")
else:
    print("Employee ID not found.")

# Step 4: Delete an employee record
delete_id = input("Enter the employee ID to delete: ")
if delete_id in employees:
    del employees[delete_id]
    print(f"Employee {delete_id} deleted successfully!")
else:
    print("Employee ID not found.")

# Step 5: Display all employee information
print("\nEmployee Information:")
for emp_id, emp_data in employees.items():
    print(f"Employee ID: {emp_id}")
    print(f"Name: {emp_data['name']}")
    print(f"Position: {emp_data['position']}")
    print(f"Salary: ${emp_data['salary']}")
    print('-' * 20)
