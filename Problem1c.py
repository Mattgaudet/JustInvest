import tkinter as tk

#Define role names and their authorized actions
roles = {
    "Client": {"p1", "p2", "p3"},
    "PremiumClient": {"p1", "p2", "p3", "p4", "p5"},
    "Employee": {"p1", "p2"},
    "FinancialAdvisor": {"p1", "p2", "p6"},
    "FinancialPlanner": {"p1", "p2", "p6", "p7"},
    "Teller": {"p1", "p2", "p8"},
    "Admin": {"p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9"}     
}

#Define names of each action for the display
role_actions = {
    "p1": "1. View account balance",
    "p2": "2. View investment portfolio",
    "p3": "3. View Financial Advisor contact info",
    "p4": "4. Modify investment portfolio",
    "p5": "5. View Financial Planner contact info",
    "p6": "6. View private customer instruments",
    "p7": "7. View money market instruments",
    "p8": "8. Process transactions",
    "p9": "9. Manage user roles"
}

#Create a string from a dictionary
def dict_to_str(d):
    return "\n".join(str(value) for value in d.values())

#Display options
def display_options(root):
    role_display = dict_to_str(role_actions)
    return tk.Label(root, text=role_display, font=("Helvetica", 12), anchor="w", justify="left")


