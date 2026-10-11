import os
from dotenv import load_dotenv
from task import  show_task, add_task


load_dotenv()
admin_password = os.getenv("TASK_MANAGER_ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode? yes/no: ")
if open_admin.lower() == "yes":
    entered_password = input("enter admin password: ")

    if entered_password == admin_password:
        print("admin, hello")
    else:
        print("wrong password")


name = input("please enter your name : ")
print("welcome", name) 

tasks = []
while True:

    task = input("enter a task or enter exit: ")
    if task == "exit":
        break
    else:
        priority = input("Enter  priority (low/medium/high):")
        
        add_task(task, priority)
        continue

show_task()



with   open("tasks.txt", "a") as file:
    file.write(f"{name} - {task}\n")