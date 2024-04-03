def input_student():
    student_id = input("ID: ")
    name = input("name: ")
    english_score = int(input("En score: "))
    c_score = int(input("C score: "))
    python_score = int(input("Python score: "))
    print("Student added\n")
    return {'id': student_id, 'name': name, 'en': english_score, 'c': c_score, 'python': python_score}

def calculate_total_average(student):
    total = student['en'] + student['c'] + student['python']
    average = total / 3
    return total, average

def calculate_grade(student):
    _, average = calculate_total_average(student)
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_rank(students):
    students.sort(key=lambda x: calculate_total_average(x)[0], reverse=True)
    for i, student in enumerate(students):
        student['rank'] = i + 1
    return students

def print_students(students):
    for student in students:
        total, average = calculate_total_average(student)
        grade = calculate_grade(student)
        print(f"ID: {student['id']}, Name: {student['name']}, Total: {total}, Average: {average}, Grade: {grade}, Rank: {student['rank']}\n")

def insert_student(students):
    student = input_student()
    students.append(student)
    return students

def delete_student(students):
    student_id = input("ID to delete: ")
    students = [student for student in students if student['id'] != student_id]
    print("Student deleted\n")
    return students

def search_student(students):
    search_id = input("ID or name for search: ")
    for student in students:
        if student['id'] == search_id or student['name'] == search_id:
            return student
    return None

def sort_students(students):
    print("sortintg complete\n")
    return sorted(students, key=lambda x: calculate_total_average(x)[0], reverse=True)

def count_students_above_80(students):
    count = 0
    for student in students:
        if calculate_total_average(student)[1] >= 80:
            count += 1
    return count

def main():
    students = []
    while True:
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Sort")
        print("5. Print")
        print("6. Number of students with average above 80:")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            students = insert_student(students)
        elif choice == 2:
            students = delete_student(students)
        elif choice == 3:
            student = search_student(students)
            if student:
                print(f"ID: {student['id']}, Name: {student['name']}, En: {student['en']}, C: {student['c']}, Python: {student['python']}\n")
            else:
                print("No student found\n")
        elif choice == 4:
            students = sort_students(students)
        elif choice == 5:
            students = calculate_rank(students)
            print_students(students)
        elif choice == 6:
            count = count_students_above_80(students)
            print(f"Number of students with average above 80: {count}\n")
        elif choice == 7:
            break
        else:
            print("Invalid choice\n")
            
main()