from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

 # to visit function
NoOfVisists = int(input("Enter the number of url history:"))
print("Enter URLs to visists:")
for i in range(NoOfVisists):
    url = input("URL:")
    print(f"Visiting {url}")
    backward_history.put(current_page)
    current_page = url

# display current page
    print(f"Current page:{current_page}")

#Go back

while input("do you want to go back?(yes/no):").lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"going back to {current_page}")
    else:
        print("no previous page available")

# go forward

while input("do you want to go forward?(yes/no):").lower() == 'yes':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = backward_history.get()
        print(f"going back to {current_page}")
    else:
        print("no forward page available")
    