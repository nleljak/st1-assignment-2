from enum import Enum


class Patient:
    def __init__(self, name: str, contact_details: str):
        if not name:
            raise ValueError("name is required")
        if not contact_details:
            raise ValueError("contact details required")

        self.name: str = name
        self.contact_details: str = contact_details


class Practitioner:
    def __init__(self, name: str, specialty: str, availability: str = "available"):
        if not name:
            raise ValueError("name is required")
        if not specialty:
            raise ValueError("specialty is required")
        self.name: str = name
        self.specialty: str = specialty
        self.availability: str = availability

    def update_availability(self, availability):
        self.availability = availability


class AppointmentStatus(Enum):
    SCHEDULED = 'SCHEDULED',
    CANCELLED = 'CANCELLED',
    COMPLETED = 'COMPLETED'


class Appointment:
    def __init__(self, patient: Patient, practitioner: Practitioner, date_time: str):
        self.patient: Patient = patient
        self.practitioner: Practitioner = practitioner
        self.date_time: str = date_time
        self.status: Enum = AppointmentStatus.SCHEDULED

    def list_details(self):
        print(self.patient, self.practitioner, self.date_time)

    def update_status(self, status):
        self.status = status
