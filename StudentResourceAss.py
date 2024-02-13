from fastapi import FastAPI, Path



app = FastAPI()


# For data storage, use an in-memory storage (Python dictionary). This is shown below:
students = {}

# A Student resource. Each student with the following:
# Id (int)
# Name(str)
# Age (int)
# Sex (str)
# Height (float)
# answer shown below:

class Student:
    def __init__(self, name, age, sex, height):
        self.id = len(students) + 1
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height


# Creating an Home Page
@app.get("/")
def Home():
    return {"Message": "Welcome to Student Resouce Assignment Homepage",
            "With": "Enpoints to Retrieve all students and a single student using student ID",
            "Also": "Enpoint to Create student resource, Update student resource by studentID",
            "And": "Delete a student resource by Student ID, using basic Python without pydantic type Enforcement"}

# To Retrieve all student
@app.get("/students")
def get_student():
    return (f"The list of student stored in the dictionary are shown below:", list(students.values()))

# To Retrieve a Student by ID
@app.get("/student/{student_id}")
def get_student_by_id(
    student_id: int = Path(
        description = "Please provide ID of the student you want to view below!", gt = 0
        )
    ):
    student = students[student_id]
    return (f" Student with ID No. {student_id} is shown below", student)
# Creating a student 
@app.post("/student/")
def create_student(
    name: str,
    age: int,
    sex: str,
    height: float
):
    student = Student(name, age, sex, height)
    students[student.id] = student
    return "Student successfully created"

# To update a student by ID
@app.put("/Update-student/{student_id}")
def update_student(
    student_id: int,
    name: str,
    age: int,
    sex: str,
    height: float
):
    student = students.get(student_id)

    student.name = name
    student.age = age
    student.sex = sex
    student.height = height

    # return {"Your student details has been successfully updated"}
    return (f"The student with ID No. {student_id} has been successfully updated")

# To delete a student by ID
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    student = students.get(student_id)
    if not student:
        return (f"Error: Student not found")
    
    del students[student_id]
    # return {"message": "Student deleted successfully"}
    return (f"Successfully deleted student with ID No. {student_id} from the list of students")