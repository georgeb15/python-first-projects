import sys
def save_task(task, date, time):
    with open("tasks.txt", "a") as file:
        file.write(task + " " + date + " " + time + "\n")
print("welcome to the to do list app")
action = input("do you want to create or view the to do list (create/view): ")
if action == "view":
    print("your to do list is as follows:")
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No tasks found. Please create a task first.")
elif action == "create":
    print("please enter the following options")
    task = input("enter the task you want to do: ")
    if task == "eat lasagne":
        print("good food choice")
    print("your task is", task)
    date = input("enter the date you want to do the task: ")
    print("your task is", task, "and the date is", date)
    time = input(int("enter the time you want to do the task: "))
    print("your task is", task, "and the date is", date, "and the time is", time)
    save_task(task, date, time)
else:
    sys.exit("invalid action")
# This is a simple to do list app that allows you to create and view tasks. It uses a function called save_task to save the task, date, and time to a file called tasks.txt.
#  The app prompts the user to choose between creating a new task or viewing existing tasks,
#  and handles invalid input by displaying an error message and exiting the program.
#  The app also handles the case where no tasks are found in the tasks.txt file by displaying a message indicating that no tasks are found.
#  Overall, this app provides a basic interface for managing tasks and can be easily extended with additional features or functionality.