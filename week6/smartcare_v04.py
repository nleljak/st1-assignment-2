class Patient:

    def __init__(self, name, address, phone_number, date_of_birth, sex, identified_gender):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.identified_gender = identified_gender

    def add_patient(self):
        pass

    def update_patient(self):
        pass

    def remove_patient(self):
        pass


class Practitioner:
    def __init__(self, name, phone_number, availability="available"):
        self.name = name
        self.phone_number = phone_number
        self.availability = availability

    def availability_status(self):
        pass

    def update_availability_status(self):
        pass


class Appointment:

    def __init__(self, patient, practitioner, appointment_time):
        self.patient = patient
        self.practitioner = practitioner
        self.appointment_status = ''
        self.appointment_time = appointment_time

    def update_appointment_status(self):
        pass

    def book_appointment(self):
        pass

    def view_appointments(self):
        pass

    def cancel_appointment(self):
        pass

