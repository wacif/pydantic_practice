from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import Optional, List, Dict, Annotated

class Patient(BaseModel):
    id: int
    name: Annotated[str, Field(max_length=30, title="Patient Name", description="The name of the patient, max length 30 characters", examples=["John Doe", "Jane Smith"], strict=True)]
    age: Annotated[int, Field(gt=0, title="Patient Age", description="The age of the patient in years", strict=True)]
    email: Annotated[EmailStr, Field(title="Patient Email", description="The email address of the patient", strict=True)]
    married: Optional[bool] = False # Optional field with default value
    weight: Annotated[float, Field(gt=0, title="Patient Weight", description="The weight of the patient in kg", strict=True)]
    height: Annotated[float, Field(gt=0, title="Patient Height", description="The height of the patient in meters", strict=True)]
    patient_record_URL: Annotated[AnyUrl, Field(title="Patient Record URL", description="The URL of the patient's medical record", strict=True)]
    alergies: Annotated[List[str], Field(title="Patient Allergies", description="List of allergies the patient has", strict=True)]
    contact_details: Annotated[Dict[str, str], Field(title="Patient Contact Details", description="Contact details of the patient", strict=True)]  # Dictionary for contact details


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