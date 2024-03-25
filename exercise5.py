# part 1

multiplication_table = int(input("Enter the number for which you want the multiplication table:"))
numberlim = int(input("Enter the limit up to which you want the multiplication table generated:"))

for i in range(1, numberlim + 1):
    print(f"{multiplication_table} * {i} = {multiplication_table * i}\n")

# part 2
    
height = int(input("Enter the height of the right triangle:"))

for i in range(1,height + 1):
    print("*" * i)

# part 3

for i in range(1,10):
    if i == 3:
        print(f"skipping {i}")
        continue
    elif i == 7:
        print(f"reached {i} breaking loop")
        break
print(i)

    



