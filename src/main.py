from tasks.task_manager import display_tasks, filter_tasks, task_generator

# Initial list of tasks
tasks = ["Buy groceries", "Finish project", "Call mom", "Send email", "Clean room"]

print("\nAll Tasks:")
display_tasks(tasks)
# in main.py, to test the filter_tasks function, add:
filter_tasks(tasks, "project") 

# Creating a generator for "project" tasks
project_tasks = task_generator(tasks, "project")

# Retrieving tasks lazily
print(next(project_tasks))  # Output: 'Finish project'