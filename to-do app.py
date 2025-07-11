def task():
    tasks=[]
    print("------welcome to the task management-----")

    total_task = int(input("enter how many task you want to add"))
    for i in range(1,total_task+1):
        task_name=input(f"enter the task{i}=")
        tasks.append(task_name)

    print(f"today's task are\n{tasks}")

    while True:
        operation = int(input("enter 1-add\n2-update\n3-delet\n4-view\n5-exit/stop"))
        if operation==1:
            add=input("enter task you want to add=")
            tasks.append(add)
            print(f"task {add} has been added successfully added...")

        elif operation ==2:
            update_val=input("enter the task name you want to update=")
            if update_val in tasks:
                up =input("enter the new task")
                idx = tasks.index(update_val)
                print(f"update task{up}")

        elif operation==3:
            del_val = input("which task you want to delete=")
            if del_val in tasks:
                idx=tasks.index(del_val)
                del tasks[idx]
                print(f"task {del_val} has been deleted..")

        elif  operation ==4:
            print(f"total tasks={tasks}")

        elif operation==5:
            print("closing the program.....")
            break
        else:
            print("invalid input")

task()   


                  