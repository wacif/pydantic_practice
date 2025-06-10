from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

def user_validation(user_data):
    try:
        user = User(**user_data)
        print("User data is valid.")
        return user
    except Exception as e:
        return str(e)
    
# Example usage
user_1 = {
        "id": "one", # This will raise a validation error because "one" is not an integer
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

user_2 = {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }

print("Validating user data...\n\n")

print("User 1:\n")
print(user_validation(user_1))

print("User 2:")
print(user_validation(user_2))
