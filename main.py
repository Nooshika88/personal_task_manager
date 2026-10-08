user_name = input("Please enter your name : ")
print("Welcome ", user_name)

user_tasks = []
while True:
    task = input("Please enter your task(If you don't want to enter any task(done)) : ")

    if task.lower() == "done":
        break
    user_tasks.append(task)

print("your task : ")
for task in user_tasks:
    print("- ", task)    

