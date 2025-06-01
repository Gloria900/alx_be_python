# # """
# # Create a simplified Python script that uses conditional statements,
# # Match Case, and loops to remind the user about a single,
# # priority task for the day based on time sensitivity.
# #
# # Algorithm
# # #step 1
# #  Ask the useer to input task description and save it as task
# #  Ask for priority task and save it as priority task
# #  Ask if the task have a time bounce and save it to time_bounce variable have two answer (yes/no)
# #  #step 2
# #  Use a Match Case statement to react differently based on the task’s priority.
# # Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
# #
# # #step 3
# # Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
# # A message should be ‘that requires immediate attention today!’
# # PSEUDOCODE


# # task = input("Enter task description: ")
# Step 1: Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Match case for priority
match  priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task", end="")
        if time_bound == "yes":
            print(" that requires immediate attention today!")
        else:
            print(". Try to address it as soon as possible.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task. You can work on it later.")
        if time_bound == "yes":
            print(" it a medium priority task, But still need to be done .!")
        else:
            print(". Consider completing it later.")

    case "low":
        print(f"Reminder: '{task}' is a low priority task.", end="")
        if time_bound == "yes":
            print(" It still needs to be done today.")
        else:
            print(" Consider completing it when you have free time.")
    case _:
        print("Invalid priority. Please enter high, medium, or low.")