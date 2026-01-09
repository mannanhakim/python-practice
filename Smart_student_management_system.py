students = []
subjects = ["English", "Maths", "Science"]
def add_student():
    name = input("Enter student name: ")
    marks_english = int(input("Enter student marks in English: "))
    marks_math = int(input("Enter student marks in Math: "))
    marks_science = int(input("Enter student marks in Science: "))
    total_marks = int(marks_english + marks_math + marks_science)
    average_marks = int(total_marks / len(subjects))

    students.append({"name": name,"English": marks_english,"Maths": marks_math, "Science": marks_science, "total_marks": total_marks, "average_marks": average_marks})
    print(f"{name} added successfully!")

def display_students():
    if not students:
        print("No students available.")
        return
    for s in students:
        print(f"Name: {s['name']}, English: {s['English']}, Math: {s['Maths']}, Science: {s['Science']}, Total Marks: {s['total_marks']}, Average Marks: {s['average_marks']}")

def grade_student():
    if not students:
        print("No students available to grade.")
        return
    for s in students:
        if s['average_marks'] >= 80:
            grade = 'A'
        elif s['average_marks'] >= 60:
            grade = 'B'
        else:
            grade = 'C'
        print(f"{s['name']}'s Grade: {grade}")
    
while True:
    print("\nSmart Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Average Marks")
    print("4. Student Grades")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case '1':
            add_student()
        case '2':
            display_students()
        case '3':
            if not students:
                print("No students available to calculate average.")
            else:
                for s in students:
                    print(f"{s['name']}'s Average Marks: {s['average_marks']}")
        case '4':
            grade_student()
        case '5':
            print("Exiting program.....")
            break
        case _:
            print("Invalid choice! Please try again.")


        