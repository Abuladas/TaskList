"""
Task list App by Sarey Abuladas, #414275

This program allows the user to view, add, and remove tasks in a simple command-line interface. The tasks are stored in
    a list, and the program provides functions for viewing the tasks, adding a task to the list, and removing a task
    from the list. The program also uses a while loop to repeatedly prompt the user for input and perform the appropriate
    action based on the user's choice.
"""


tasks = []

'''
A simple function to to view the tasks, the first part is if there are no tasks to show.
Then a simple for loop to show each task in the list and the enumerate is built in function to index them automatically
'''
def view_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(tasks):
            print("{}. {}".format(i + 1, task))
'''
A simple function to to add a task to the list,  it just uses append list function to add the strings to the list
'''
def add_task(task):
    tasks.append(task)
    print("Task added.")
'''
A simple function to to add a task to the list,  it just uses pop (the -1 because in python indexing start with 0 to 
    keep it more user friendly) list function to remove the strings(tasks) to the list
'''
def remove_task(index):
    try:
        task = tasks.pop(index - 1)
        print("Task '{}' removed.".format(task))
    except IndexError:
        print("Invalid task index.")
'''
 the save_to_file function takes in two arguments: the tasks list and the filename to save the list to. 
 The function uses the open function to open the specified file in write mode ('w') and assigns the file object to 
    the variable f.
Then, it iterates through the tasks list and writes each task to the file, followed by a newline character ('\n') 
    using the write method.
Finally, it closes the file using the with open statement and prints a message indicating that the tasks have been 
    saved to the specified file.

Please be aware that this code will overwrite the file if the file already exists.
'''
def save_to_file(tasks, filename):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(task + '\n')
    print("Tasks saved to {}".format(filename))
'''
load_from_file function takes in a single argument: the filename to load the list from. The function uses the open 
    function to open the specified file in read mode ('r') and assigns the file object to the variable f.
Then, it reads the content of the file using the read() method and splits the content of the file into a list of lines
    using the splitlines() method, and assigns the result to the variable tasks.
The function finally returns the tasks list.

It's important to keep in mind that if the file doesn't exist or the file can't be opened in read mode, the open 
    function will raise an exception. So it's a good practice to add a try-except block to handle this possibility.
'''
def load_from_file(filename):
    try:
        with open(filename, 'r') as f:
            tasks = f.read().splitlines()
            return tasks
    except :
        print("An error occurred trying to read the file.")

while True:
    choice = input("\nEnter \n1 to view tasks, \n2 to add a task, \n3 to remove a task, \n4 save the tasks list, \n5 to load the tasks list, or \n6 to exit: ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '3':
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == '4':
        filenamw=input("Enter the list name (it is NOT case sensitive)\n")
        fileName=filenamw+".txt"
        save_to_file(tasks, fileName)
    elif choice == '5':
        rem=input("The current task will be replaced by the loaded task are you sure you want to continue? (Y for yes and N for no)\n")
        if rem.upper()=="Y":
            filenamR=input("Enter the list name (it is NOT case sensitive)\n")
            fileNameR=filenamR+".txt"
            tasks = load_from_file(fileNameR)
            print("List loaded successfully:")
            view_tasks()
    elif choice == '6':
        break
    else:
        print("Invalid choice.")
