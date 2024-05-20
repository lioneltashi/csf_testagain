student_list = []
student_dict = {}

name = input("Enter your name:")
age = input("Enter your age:")
grade = input("Enter your grade:")

student_list.append(name)
student_dict[name]= {"age": age, "grade": grade}


print("Student info added")
print(student_dict.items())

print("student details:")

searchname = input("Search name : ")

for item in student_list:
    if searchname == item:
        print (name,age,grade)
        print("Done")
    else:
        print("student not found")

nameremove = input("enter name to remove:")
 
for item in student_list:
    if  item == nameremove:
        student_list.remove(nameremove)
        del student_dict[nameremove]
        print("student removed")
    else:
        print("not found")

    #print(f"name:{student_dict[name]}, age:{student_dict[]}")
    

        
