class Student:
    def __init__(self, student_id, name, gpa):
        self.student_id = student_id
        self.name = name
        self.gpa = gpa
        self.file = "students.csv"

    def __str__(self):
        return f"  Student ID: {self.student_id}, Student Name: {self.name}, Student GPA: {self.gpa}"

    def load_students(self):
        students = []
        with open(self.file, mode='r') as file:
            for line in file:
                row = line.strip().split(',')
                if len(row) < 3:
                    continue  # Skip lines that don't have enough data
                student_id = int(row[0])
                name = row[1]
                gpa = float(row[2])
                students.append(Student(student_id, name, gpa))

        return students

    def save_students(self, students):
        with open(self.file, 'w') as file:
            for student in students:
                file.write(f"{student.student_id},{student.name},{student.gpa}\n")



class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.n = 0

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def heapify(self, index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left].gpa > self.heap[largest].gpa:
            largest = left

        if right < len(self.heap) and self.heap[right].gpa > self.heap[largest].gpa:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(largest)

    def insert(self, student):
        self.n += 1
        self.heap.append(student)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current].gpa > self.heap[self.parent(current)].gpa:
            self.heap[current], self.heap[self.parent(current)] = self.heap[self.parent(current)], self.heap[current]
            current = self.parent(current)


    def display_top_k(self, k):
        students = self.heap[:]
        top_students = []

        for i in range(k):
            if not students:
                break
            max_student = students[0]
            for student in students:
                if student.gpa > max_student.gpa:
                    max_student = student

            top_students.append(max_student)
            students.remove(max_student)

        return top_students


class Node:
    def __init__(self, student):
        self.leftchild = None
        self.rightchild = None
        self.student = student


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, student):
        if not self.root:
            self.root = Node(student)
        else:
            self._insert_rec(self.root, student)

    def _insert_rec(self, node, student):
        if student.gpa < node.student.gpa:
            if node.leftchild is None:
                node.leftchild = Node(student)
            else:
                self._insert_rec(node.leftchild, student)
        else:
            if node.rightchild is None:
                node.rightchild = Node(student)
            else:
                self._insert_rec(node.rightchild, student)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.leftchild, result)
            result.append(node.student)
            self.inorder_traversal(node.rightchild, result)

    def search_by_gpa(self, gpa, node, result):
        if node:
            if node.student.gpa == gpa:
                result.append(node.student)
            self.search_by_gpa(gpa, node.leftchild, result)
            self.search_by_gpa(gpa, node.rightchild, result)


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, student):
        index = self.hash(student.student_id)
        while self.table[index] is not None:
            if self.table[index].student_id == student.student_id:
                self.table[index] = student
                return
            index = (index + 1) % self.size
        self.table[index] = student

    def search(self, student_id):
        index = self.hash(student_id)
        while self.table[index] is not None:
            if self.table[index].student_id == student_id:
                return self.table[index]
            index = (index + 1) % self.size
        return None

    def remove(self, student_id):
        index = self.hash(student_id)
        while self.table[index] is not None:
            if self.table[index].student_id == student_id:
                self.table[index] = None  # Physically remove the student
                return True
            index = (index + 1) % self.size
        return False

    def display(self):
        for student in self.table:
            if student is not None:
                print(student)


def menu():
    while True:
        try:
            print("\n------ Welcome to Student Records Management System! -----")
            print(" Please choose an option from the menu below:")
            print("   Type [1] to Add student record")
            print("   Type [2] to Search student by ID (Hash Table)")
            print("   Type [3] to Delete Student record (Hash Table)")
            print("   Type [4] to Display all student records (Hash Table)")
            print("   Type [5] to Display sorted student records by GPA (BST)")
            print("   Type [6] to Search for students by GPA (BST)")
            print("   Type [7] to Prioritize scholarship candidates (Heap)")
            print("   Type [8] to Save student records to file")
            print("   Type [9] to Load student records from File")
            print("   Type [10] to Exit.")
            print("----------------------------------------------------")
            choice = int(input("Enter your choice: "))
            assert choice in range(1, 11), "Invalid Input, please choose between 1 - 10."
            return choice

        except ValueError:
            print("Invalid Input. Please enter a number.")
        except AssertionError as e:
            print(e)
