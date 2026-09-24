from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List


app = FastAPI(
    title="Doctor and Patient Management API",
    description="REST API for managing doctors and patients",
    version="1.0.0"
)


# -----------------------------
# Pydantic Models
# -----------------------------

class Doctor(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


class Patient(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    phone: str


# -----------------------------
# In-memory storage
# -----------------------------

doctors = []
patients = []


# -----------------------------
# Doctor APIs
# -----------------------------

@app.post("/doctors", status_code=201)
def create_doctor(doctor: Doctor):
    doctor_id = len(doctors) + 1

    doctor_data = {
        "id": doctor_id,
        "name": doctor.name,
        "specialization": doctor.specialization,
        "email": doctor.email,
        "is_active": doctor.is_active
    }

    doctors.append(doctor_data)

    return {
        "message": "Doctor created successfully",
        "doctor": doctor_data
    }


@app.get("/doctors")
def get_doctors():
    return {
        "count": len(doctors),
        "doctors": doctors
    }


@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):

    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor

    raise HTTPException(
        status_code=404,
        detail="Doctor not found"
    )


# -----------------------------
# Patient APIs
# -----------------------------

@app.post("/patients", status_code=201)
def create_patient(patient: Patient):
    patient_id = len(patients) + 1

    patient_data = {
        "id": patient_id,
        "name": patient.name,
        "age": patient.age,
        "phone": patient.phone
    }

    patients.append(patient_data)

    return {
        "message": "Patient created successfully",
        "patient": patient_data
    }


@app.get("/patients")
def get_patients():
    return {
        "count": len(patients),
        "patients": patients
    }