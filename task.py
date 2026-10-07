tasks = []
def add_task(task):
    tasks.append(task)
    print("your task ", tasks, "added")


def show_task():
    if not tasks:
        print("there isnt any task")
    else:
        for i in tasks:
            print(i)