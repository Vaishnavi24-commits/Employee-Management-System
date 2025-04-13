import sqlite3

# Connect to SQLite DB (creates if not exists)
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create employee table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT,
        salary REAL
    )
''')
conn.commit()

# Add new employee
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    dept = input("Enter department: ")
    salary = float(input("Enter salary: "))
    cursor.execute("INSERT INTO employee (name, age, department, salary) VALUES (?, ?, ?, ?)",
                   (name, age, dept, salary))
    conn.commit()
    print("✅ Employee added successfully.")

# View all employees
def view_employees():
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    print("\n--- Employee List ---")
    for row in rows:
        print(row)

# Search employee by ID
def search_employee():
    emp_id = int(input("Enter Employee ID: "))
    cursor.execute("SELECT * FROM employee WHERE id = ?", (emp_id,))
    row = cursor.fetchone()
    if row:
        print("👤 Employee Details:", row)
    else:
        print("❌ No employee found with that ID.")

# Update employee
def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))
    new_salary = float(input("Enter new salary: "))
    cursor.execute("UPDATE employee SET salary = ? WHERE id = ?", (new_salary, emp_id))
    conn.commit()
    print("✅ Salary updated.")

# Delete employee
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))
    cursor.execute("DELETE FROM employee WHERE id = ?", (emp_id,))
    conn.commit()
    print("🗑️ Employee deleted.")

# Menu
def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("👋 Exiting program.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

menu()

# Close connection
conn.close()
