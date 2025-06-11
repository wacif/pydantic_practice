from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import Optional, List, Dict

class Patient(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    married: Optional[bool] = False # Optional field with default value
    weight: float
    height: float
    patient_record_URL: AnyUrl
    alergies: List[str]
    contact_details: Dict[str, str]  # Dictionary for contact details

    @model_validator(mode='after')
    def validate_contact(cls, model):
        if model.age > 60 and "emergency_contact" not in model.contact_details:
            raise ValueError("Emergency contact is required for patients over 60 years old.")
        else:
            return model


# Example No 1

def patient_data_view(patient_data):
    print("Patient Data:")
    print(f"ID: {patient_data.id}")
    print(f"Name: {patient_data.name}")
    print(f"Age: {patient_data.age}")
    print(f"Email: {patient_data.email}")
    print(f"Married: {patient_data.married}")
    print(f"Weight: {patient_data.weight} kg")
    print(f"Height: {patient_data.height} m")
    print(f"Patient Record URL: {patient_data.patient_record_URL}")
    print(f"Alergies: {', '.join(patient_data.alergies)}")
    print("Contact Details:")
    for key, value in patient_data.contact_details.items():
        print(f"{key}: {value}")


patient_1 = {
    "id": 1,
    "name": "John Doe",
    "age": 70,
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

patient_2 = {
    "id": 2,
    "name": "Jane Smith",
    "age": 28,
    "email": "jane.smith@example.com",
    "married": False,
    "weight": 60.0,
    "height": 1.65,
    "patient_record_URL": "http://example.com/patient/2",
    "alergies": ["latex"],
    "contact_details": {
        "phone": "987-654-3210",
        "address": "456 Elm St, Othertown, USA"
    }
}

# Validate and create Patient instances
patient_1_instance = Patient(**patient_1)
patient_2_instance = Patient(**patient_2)
# View patient data
print("Viewing patient data...\n\n")
print("Patient 1:")
patient_data_view(patient_1_instance)
print("\nPatient 2:")
patient_data_view(patient_2_instance)