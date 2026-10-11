import os 
from dotenv import load_dotenv
from tasks import add_tasks

load_dotenv()
admin_password= os.getenv("TASK_MANAGER_ADMIN_PASSWORD")
open_admin = input("Do you want to open admin mode (yes/no)? ")

if open_admin.lower() == "yes":
    entered_password = input("Enter password : ")
    print("Hello! Admin")
elif open_admin.lower() == "no":
    print("Alright!...")
else:
    print("Wrong password!")


user_name = input("Please enter your name : ")
print("Welcome ", user_name)

tasks = []
while True:
    task = add_tasks()
    if task.lower() == "done":
        break
    priority = input(f"Priority for {task} (high/medium/low): ")
    print(f"- {task} | {priority}")
    tasks.append(task)


print("your task: ")
for task in tasks:
    print("- ", task)    
    

with open("tasks.txt", "w") as file:
    file.write("\n".join(tasks))