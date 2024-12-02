import tkinter as tk
from datetime import datetime
from Problem1c import *

#Display authorized options
def display_authorized_options(root, role):
    available_options = "Your authorized operations are: " + role_options(role)
    return tk.Label(root, text=available_options, font=("Helvetica", 12), anchor="w", justify="left")

#Get the authorized operations by role
def role_options(role):
    #If Teller, check that the time is between 9AM and 5PM
    if role == "Teller":
        current_time = datetime.now().time()
        if not (current_time.hour >= 9 and current_time.hour < 17):
            return "\nTeller operations only available between 9 AM and 5 PM"
    
    role_numbers = []
    for role_number in roles.get(role, set()):
        role_numbers.append(role_actions.get(role_number, "")[:1])
    role_numbers.sort()
    return ", ".join(role_numbers)