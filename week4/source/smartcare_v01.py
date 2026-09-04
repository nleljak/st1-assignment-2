# assumed use of code from handout, then modifications to only task 1 enhanced as in handout responses

# Create and run a simple Python file with basic input,output statements
# print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
# patient1_name = 'Alice Smith'
# practitioner1_name = 'Dr. John Doe'
# appointment1_time = '2024-07-20 10:00 AM'
# print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")
#
# # Second Appointment
# patient2_name = 'Bob Johnson'
# practitioner2_name = 'Dr. Jane Roe'
# appointment2_time = '2024-07-20 11:30 AM'
# print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

# task 1 enhanced
# Use lists, dictionaries and functions to enhance the Python file

appointments = []


def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("appointment time cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    if not check_double_booking(appointment):
        appointments.append(appointment)


# check for double booking when booking an appointment
def check_double_booking(appointment_data):
    if not appointments:
        return
    for appointment in appointments:
        if appointment['time'] == appointment_data['time']:
            print(f"There is a double booking!")
            return True


def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']}"
            f"Practitioner: {appointment['practitioner']}"
            f" Time: {appointment['time']}")


print("Welcome to SmartCare: The Clinical Appointment Booking System!")

# user input
patient_user_input: str = input("Enter The Patient's Name")
practitioner_user_input: str = input("Enter The Practitioner's Name")
time_user_input: str = input("Enter The Booking's Date and Time [YYYY-MM-DD HH:MM AM/PM")

# book with user input
book_appointment(patient_user_input, practitioner_user_input, time_user_input)

# book with only function and test double booking function
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')

# display appointments
display_appointments()
