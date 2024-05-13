class Person:
    def __init__(self, name, age, CID_number):
        self.name = name
        self.age = age
        self.CID_number = CID_number

    def Talk(self):
        print(self.name," is talking")

    def Walk(self):
        print(f"{self.name} is walking at age {self.age}")

    def Eat(self):
        print(f"{self.name} was eating, so I told him that your CID number is {self.CID_number} ")

    def Sleep(self):
        print(f"student named {self.name} with CID number {self.CID_number} got detention due to sleeping in class hours")
    
class student(Person):
    def __init__(self, name, age, CID_number, student_ID, course, year, GPA):
        self.name = name
        self.age = age
        self.CID_number = CID_number
        self.student_ID = student_ID
        self.course = course
        self.year = year
        self.GPA = GPA

    def study(self):
        print(f"{self.name} student ID {self.student_ID} is studying in {self.course}")
        
    def attend_class(self):
        print(f"Year {self.year} students will have to attend {self.course} course")

    def write_exam(self):
        print(f"{self.name} is trying to score a GPA of {self.GPA}")

class teacher(Person):
    def __init__(self, name, age, CID_number, subject, salary, department, designation):
        self.name = name
        self.age = age
        self.CID_number = CID_number
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"Miss {self.name} is teaching {self.subject} under {self.department} department.")

    def grade_students(self):
        print(f"{self.name} earn a salary of {self.salary} just by grading students.")

    def attend_meeting(self):
        print(f"{self.name} will have to attend meating as she is {self.designation}")

teacher1 = teacher("Tashi Pelden", "24", "10101000108", "CSF", "Nu. 5000000", "ECE", "Lecturer")
teacher1.Walk()
teacher1.Talk()
teacher1.teach()     

student1 = student("Pema Tashi", "18", "10101000107", "02230101", "ECE", "1", "4")
student1.Eat()
student1.study()
student1.write_exam()