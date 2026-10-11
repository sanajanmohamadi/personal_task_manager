tasks = []
def add_task(task, priority):
    tasks.append(task + " , " +   priority)
    print("your task ", tasks, priority, "added")


def show_task():
    if not tasks:
        print("there isnt any task")
    else:
        for i in tasks:
            print(i)