class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"

def sort_student(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with a list of student objects
students = [
    Student("Alice", "A001", 3.75),
    Student("Bob", "B002", 3.89),
    Student("Charlie", "C003", 3.65),
    Student("David", "D004", 3.95),
]

sorted_students = sort_student(students)

# Print the sorted list of students
for student in sorted_students:
    print(student)