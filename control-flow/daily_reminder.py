task = input("Enter your task: ")
priority = input("task’s priority (high, medium, low): ")
time_bound = input("he task is time-bound (yes or no:) ")

match task:
    case "priority":
        if priority == "high" and time_bound =="yes":
            print("Reminder: {task} is a high priority task that requires immediate attention today!")
        elif priority == "low" and time_bound =="low":
            print("Note: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("invalid task")
            
    