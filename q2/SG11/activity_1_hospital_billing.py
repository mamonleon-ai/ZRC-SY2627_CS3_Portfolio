class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        print("Patient Type:Senior Citizen")


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


print("Hospital Billing System")
print("-----------------------")

patient1 = Patient("Juan Dela Cruz", 15000.0)
patient2 = SeniorPatient("Maria Santos", 15000.0)
patient3 = PhilHealthPatient("Pedro Reyes", 15000.0)

patient_list = [patient1, patient2, patient3]

for patient in patient_list:
    print(f"Patient Name:  {patient.get_name()}")
    patient.display_patient_type()
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")
    print()