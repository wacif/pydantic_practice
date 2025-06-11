from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import Optional, List, Dict

class Patient(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    married: Optional[bool] = False # Optional field with default value
    weight: float # Weight in kg
    height: float # Height in m
    patient_record_URL: AnyUrl
    alergies: List[str]
    contact_details: Dict[str, str]  # Dictionary for contact details

    @computed_field
    @property
    def bmi(self) -> float:
        """Calculate Body Mass Index (BMI)"""
        if self.height <= 0:
            raise ValueError("Height must be greater than zero to calculate BMI.")
        return round(self.weight / (self.height ** 2), 2)
    
# Example

def patient_data_view(patient_data):
    print("Patient Data:")
    print(f"ID: {patient_data.id}")
    print(f"Name: {patient_data.name}")
    print(f"Age: {patient_data.age}")
    print(f"Email: {patient_data.email}")
    print(f"Married: {patient_data.married}")
    print(f"Weight: {patient_data.weight} kg")
    print(f"Height: {patient_data.height} m")
    print(f"BMI: {patient_data.bmi}")
    print(f"Patient Record URL: {patient_data.patient_record_URL}")
    print(f"Alergies: {', '.join(patient_data.alergies)}")
    print("Contact Details:")
    for key, value in patient_data.contact_details.items():
        print(f"{key}: {value}")

patient_1 = {
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "married": True,
    "weight": 70.5,
    "height": 1.75,
    "patient_record_URL": "http://example.com/patient/1",
    "alergies": ["penicillin", "nuts"],
    "contact_details": {
        "phone": "123-456-7890",
        "address": "123 Main St, Anytown, USA"
    }
}

# Create a Patient instance
patient_instance = Patient(**patient_1)
# Display patient data
patient_data_view(patient_instance)