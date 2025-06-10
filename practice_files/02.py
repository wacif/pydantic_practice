from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int
    email: str


def student_data_view(student_data):

    print("Student Data:")
    print(f"ID: {student_data.id}")
    print(f"Name: {student_data.name}")
    print(f"Age: {student_data.age}")
    print(f"Email: {student_data.email}")

student_1 = {
    "id": 1,
    "name": "Alice Johnson",
    "age": 20,
    "email": "alice.johnson@example.com"
}

student_2 = {
    "id": 2,
    "name": "Bob Smith",
    "age": 22,
    "email": "bob.smith@example.com"
}

# validate and create Student instances
student_1_instance = Student(**student_1)
student_2_instance = Student(**student_2)
# view student data
print("Viewing student data...\n\n")

print("Student 1:")
student_data_view(student_1_instance)

print("\nStudent 2:")
student_data_view(student_2_instance)