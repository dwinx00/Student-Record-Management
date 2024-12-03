from classes import menu
from classes import HashTable
from classes import BinarySearchTree
from classes import PriorityQueue
from classes import Student


# function to validate all user input
def user_input(x):
    while True:
        try:
            if x == "id":
                student_id = int(input("Enter student ID: "))
                return student_id


            elif x == "name":
                student_name = input("Enter student Name: ").strip()
                assert student_name != "", "Invalid Input, It blank"
                return student_name

            elif x == "gpa":
                student_gpa = float(input("Enter student GPA: "))
                assert 0 < student_gpa < 6, "Invalid Input, GPA is only 1 to 5."
                return student_gpa

            elif x == 'k':
                k = int(input("Enter number of top students to display: "))
                return k


        except ValueError:
            print("Invalid Input")
        except AssertionError as e:
            print(e)


# Function to add a student record
def add_student(bst, pq, ht, file):
    student = Student(user_input("id"), user_input("name"), user_input("gpa"))
    pq.insert(student)
    bst.insert(student)
    ht.insert(student)
    students = file.load_students()
    students.append(student)
    file.save_students(students)


# Function to search for a student by ID (Hash Table)
def search_student(ht):
    print(" - Searching for a student by ID (using hash table) - ")
    student = ht.search(user_input("id"))
    if student:
        print(student)
    else:
        print("Student not found.")


# Function to delete a student record (Hash Table)
def delete_student(ht, file):
    student_id = user_input("id")
    if ht.remove(student_id):
        print("Deleted.")
        # Load current students and exclude the deleted student
        students = file.load_students()  # Load current students
        students = [student for student in students if student.student_id != student_id]  # Remove deleted student
        file.save_students(students)  # Save all students
    else:
        print("Student not found.")


# Function to display all student records (Hash Table)
def display_all_students(ht):
    print(" - Displaying all student records (using hash table) -")
    ht.display()


# Function to display sorted student records by GPA (BST)
def display_sorted_by_gpa(bst):
    print(" - Displaying student records sorted by GPA (using BST) -")
    students = list()
    bst.inorder_traversal(bst.root, students)
    print("Students sorted by GPA:")
    for student in students:
        print(student)


# Function to search for students by GPA (BST)
def search_gpa(bst):
    print(" - Searching for students by GPA (using BST) -")
    result = list()
    gpa = user_input("gpa")
    bst.search_by_gpa(gpa, bst.root, result)
    if result:
        print(f"Students with GPA {gpa} :")
        for student in result:
            print(student)


# Function to prioritize scholarship candidates (Heap)
def prioritize_scholarship(pq):
    print(" - Prioritizing scholarship candidates (using heap) -")
    k = user_input('k')
    top_students = pq.display_top_k(k)
    print(f"Top {k} students eligible for scholarship:")
    for student in top_students:
        print(student)


def output():
    pq = PriorityQueue()
    bst = BinarySearchTree()
    ht = HashTable(20)
    file = Student(None, None, None)  # just for file handling
    # load students from students
    students = file.load_students()
    for student in students:
        ht.insert(student)
        bst.insert(student)
        pq.insert(student)

    while True:
        select = menu()
        if select == 1:
            add_student(bst, pq, ht, file)

        elif select == 2:
            search_student(ht)

        elif select == 3:
            delete_student(ht, file)

        elif select == 4:
            display_all_students(ht)
            input("Click to return...")


        elif select == 5:
            display_sorted_by_gpa(bst)
            input("Click to return...")

        elif select == 6:
            search_gpa(bst)

        elif select == 7:
            prioritize_scholarship(pq)
            input("Click to return")


        elif select == 8:
            print("Saving students to file")
            file.save_students(students)

        elif select == 9:
            print("loading students from file")
            file.load_students()

        elif select == 10:
            print("Exiting...")
            break


output()
