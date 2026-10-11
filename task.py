tasks = []
def add_task(task, priority):
    tasks.append(task + " , " +   priority)
    print("your task and their priorities ", tasks, priority, "added")


def show_task():
    if not tasks:
        print("there isnt any task")
    else:
        print("your tasks: ")
        for i in tasks:
            print(i)