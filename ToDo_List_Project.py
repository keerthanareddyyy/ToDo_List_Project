#!/usr/bin/env python
# coding: utf-8

# # 📝 To-Do List Project
# A simple console-based to-do list application using Python. It allows users to add, view, and delete tasks. Tasks are stored in a text file for persistence.
# 

# In[3]:


FILENAME = "tasks.txt"


# In[2]:


def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


# In[4]:


def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


# In[5]:


def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


# In[6]:


tasks = load_tasks()
while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")


# In[ ]:




