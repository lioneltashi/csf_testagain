# learning
print("Newton's second law calculations") 
print("select a value:")
print("1. Mass (m)")
print("2. Accleration (a)")
print("3. Force (f)")

users_choice= input("Enter an above option number:")
if users_choice == "1":
    a= float(input("Enter the acceleration:"))
    f= float(input("Enter force:"))
    m= f/a
    print(f"Mass(m)={m}")

elif users_choice == "2":
    f= float(input("Enter the force:"))
    m= float(input("Enter mass:"))
    a= f/m
    print(f"Acceleration(a)={a}")

elif users_choice == "3":
    a= float(input("Enter acceleration:"))
    m= float(input("Enter mass:"))
    f= m*a
    print(f"Force(f)={f}")

else:
    print("Please select the above option number:")
    





