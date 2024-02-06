def inputStudent():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    sex = input("Enter student sex: ")
    department = input("Enter student department: ")
    marks = float(input("Enter student marks: "))
    return f"{student_id},{name},{sex},{department},{marks}\n"

def highScorer(filename, department):
    highest_scorer = {"marks": 0}

    with open(filename, "r") as file:
        for line in file:
            student_id, name, sex, dept, marks = line.strip().split(',')
            marks = float(marks)

            if dept.lower() == department.lower() and marks > highest_scorer["marks"]:
                highest_scorer = {"id": student_id, "name": name, "marks": marks}

    return highest_scorer

record=int(input("Enter number of students: "))
with open("student.dat", "a") as file:
    for _ in range(record):
        file.write(inputStudent())
    print("Student records have been saved.")
    file.close()
dept=input("Enter department to search in : ")
result = highScorer("student.dat", dept)

if result["marks"] > 0:
    print(f"Highest scorer in {dept} department:")
    print(f"ID: {result['id']}, Name: {result['name']}, Marks: {result['marks']}")
else:
    print(f"No records found for {dept} department.")
