# Practical Work 1: Student Mark Management System


def input_students():
    n = int(input("Enter number of students: "))
    return [
        {
            "id": input(f"Student {i+1} ID: "),
            "name": input("Name: "),
            "dob": input("DoB: "),
        }
        for i in range(n)
    ]


def input_courses():
    n = int(input("Enter number of courses: "))
    return [
        {"id": input(f"Course {i+1} ID: "), "name": input("Name: ")}
        for i in range(n)
    ]


def input_marks(students, courses, marks):
    c_id = input("Enter Course ID to input marks: ")
    if not any(c["id"] == c_id for c in courses):
        print("Course not found!")
        return
    marks[c_id] = {
        s["id"]: float(input(f"Mark for {s['name']} ({s['id']}): "))
        for s in students
    }


def show_marks(students, marks):
    c_id = input("Enter Course ID to view marks: ")
    if c_id not in marks:
        print("No marks found!")
        return
    for s in students:
        if s["id"] in marks[c_id]:
            print(f"ID: {s['id']} | Name: {s['name']} | Mark: {marks[c_id][s['id']]}")


def main():
    students, courses, marks = [], [], {}
    while True:
        print(
            "\n1. Input Students  2. Input Courses  3. Input Marks"
            "\n4. List Courses    5. List Students  6. Show Marks  7. Exit"
        )
        choice = input("Select (1-7): ")
        if choice == "1":
            students = input_students()
        elif choice == "2":
            courses = input_courses()
        elif choice == "3":
            input_marks(students, courses, marks)
        elif choice == "4":
            print("\nCOURSES:", *[f"{c['id']}: {c['name']}" for c in courses], sep="\n")
        elif choice == "5":
            print(
                "\nSTUDENTS:",
                *[f"{s['id']} - {s['name']} ({s['dob']})" for s in students],
                sep="\n",
            )
        elif choice == "6":
            show_marks(students, marks)
        elif choice == "7":
            break


if __name__ == "__main__":
    main()