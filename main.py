from tasks import add_tasks
user_name = input("Please enter your name : ")
print("Welcome ", user_name)

tasks = []
while True:
    task = add_tasks()
    tasks.append(task)
    if task.lower() == "done":
        break

print("your task : ")
for task in tasks:
    print("- ", task)    

