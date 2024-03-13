from queue import Queue


patients = Queue()
current_patient = None

while True:
    print("""Desk Manager - Patient Registration and Appoinment System\n
          1. Register Patient
          2. Remove Patient after Meeting Doctor
          3. Display Patient Queue
          4. Exit""")
    you = input("Enter any option no. mentioned above:")

    if you == "1":
        patients_register = input("Enter patient's name:")
        patients.put(patients_register)
        current_patient = (patients_register)
        print(f"{patients_register} is successfully registered\n")

    elif you == "2":
        patients.get()
        print(f"{current_patient} has been removed\n")

    elif you == "3":
        print("The current patient queue is:")
        for patients in patients.queue:
            print(patients)

    elif you == "4":
        print("Exited")
        break

    else:
        print("Invalid input")