# Doctor and Patient Management API.

## Technologies Used

* Python 3.9+
* FastAPI
* Pydantic
* Uvicorn
* In-memory storage

## Features

### Doctor APIs

* POST `/doctors` - Create a doctor
* GET `/doctors` - List all doctors
* GET `/doctors/{doctor_id}` - Get doctor by ID

### Patient APIs

* POST `/patients` - Create a patient
* GET `/patients` - List all patients

## Validation

* Doctor email must be valid.
* Patient age must be greater than 0.
* Pydantic models are used for request validation.
* HTTPException is used for error handling.

## Project Structure

```text
doctor_patient_api
│
├── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone or download the project

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd doctor_patient_api

C:\Users\petaprasanth\Downloads\doctor_patient_api

### 2. Create virtual environment

python -m venv venv


### 3. Activate virtual environment

Windows:

C:\Users\petaprasanth\Downloads\doctor_patient_api>venv\Scripts\activate

### 4. Install dependencies

```bash

(venv) C:\Users\petaprasanth\Downloads\doctor_patient_api>pip install -r requirements.txt

### 5. Start the server

```bash
uvicorn main:app --reload
```

### 6. Open Swagger documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Use Swagger UI to test all API endpoints.

## Example Doctor Request

```json
{
  "name": "Dr. Raj Kumar",
  "specialization": "Cardiology",
  "email": "raj@example.com",
  "is_active": true
}
```

## Example Patient Request

```json
{
  "name": "Prasanth",
  "age": 25,
  "phone": "9876543210"
}
```

## Error Handling

If a doctor ID does not exist, the API returns:

```json
{
  "detail": "Doctor not found"
}
```

with HTTP status code `404`.

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```
