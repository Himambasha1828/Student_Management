students = []

def add_student():
    name = str(input("Enter Name: "))
    roll = int(input("Enter Roll No: "))
    gend = str(input("Enter Gender: "))

    students.append({"name": name, "roll": roll, "gend":gend})
    print("Student Added!")

def view_students():
    for s in students:
        print(f"Name: {s['name']} | Roll: {s['roll']} | Gender: {s['gend']}")

while True:
    print("\n1. Add  2. View  3. Exit")
    ch = input("Enter choice: ")
    if ch == '1':
        add_student()
    elif ch == '2':
        view_students()
    else:
        break
