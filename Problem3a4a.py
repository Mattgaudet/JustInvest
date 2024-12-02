import tkinter as tk
from tkinter import messagebox
from Problem1c import *
from Problem2c import *
from Problem3b import *
from Problem4b import display_authorized_options

#Create login and signup page
def login_page(root):
    # Create a larger frame with padding and a border
    login_frame = tk.Frame(root, padx=50, pady=30, relief="raised", borderwidth=2)
    
    # Add a title label with larger font
    title_label = tk.Label(login_frame, text="justInvest Login", font=('Helvetica', 16, 'bold'))
    title_label.pack(pady=15)
    
    # Make the entry fields wider
    tk.Label(login_frame, text="Username:", font=('Helvetica', 10)).pack(pady=5)
    username_entry = tk.Entry(login_frame, width=30)
    username_entry.pack(pady=5)
    
    tk.Label(login_frame, text="Password:", font=('Helvetica', 10)).pack(pady=5)
    password_entry = tk.Entry(login_frame, show="*", width=30)
    password_entry.pack(pady=5)
    
    def handle_login():
        username = username_entry.get()
        password = password_entry.get()
        
        role = check_credentials(username, password)
        if role:  # If role is not None
            login_frame.destroy()
            show_main_content(root, username, role)
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def handle_signup():
        username = username_entry.get()
        password = password_entry.get()
        
        if username and password:
            username_error = validate_username(username)
            if(username_error):
                messagebox.showerror("Error", username_error)
                return
            password_error = validate_password(username, password)
            if password_error is None:  # Password is valid
                save_credentials(username, password, "Client")
                messagebox.showinfo("Success", "Account created successfully!")
            else:  # Password is invalid
                messagebox.showerror("Error", password_error)
        else:
            messagebox.showerror("Error", "Please fill in all fields!")

    tk.Button(login_frame, text="Login", command=handle_login).pack(pady=5)
    tk.Button(login_frame, text="Sign Up", command=handle_signup).pack(pady=5)
    
    return login_frame

def show_main_content(root, username, role):
    # Create main content frame
    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)
    
    # Welcome message
    welcome_label = tk.Label(main_frame, 
                           text=f"Welcome {username}!\n You are logged in as: {role}", 
                           font=('Helvetica', 14))
    welcome_label.pack(pady=20)
    
    if role == "Admin":
        show_admin_panel(root, username)
    else:
        # Display available options based on role
        options_label = display_options(main_frame)
        options_label.pack(pady=10)
        
        # Display authorized options for the role
        auth_options_label = display_authorized_options(main_frame, role)
        auth_options_label.pack(pady=10)

#Create admin panel for updating user roles
def show_admin_panel(root, admin_username):
    admin_frame = tk.Toplevel(root)
    admin_frame.title("User Role Management")
    admin_frame.geometry("400x500")
    
    # User list
    users_frame = tk.Frame(admin_frame)
    users_frame.pack(pady=20, padx=20, fill="both", expand=True)
    
    tk.Label(users_frame, text="User Management", font=('Helvetica', 14, 'bold')).pack()
    
    # Create listbox for users
    user_listbox = tk.Listbox(users_frame, width=40)
    user_listbox.pack(pady=10)
    
    # Role selection dropdown
    selected_role = tk.StringVar()
    role_dropdown = tk.OptionMenu(users_frame, selected_role, *roles.keys())
    role_dropdown.pack(pady=10)
    
    def refresh_user_list():
        user_listbox.delete(0, tk.END)
        users = get_all_users()
        for username, role in users:
            user_listbox.insert(tk.END, f"{username} - {role}")
    
    def update_role():
        selection = user_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a user")
            return
            
        username = user_listbox.get(selection[0]).split(' - ')[0]
        new_role = selected_role.get()
        
        if update_user_role(username, new_role):
            messagebox.showinfo("Success", f"Updated {username}'s role to {new_role}")
            refresh_user_list()
        else:
            messagebox.showerror("Error", "Failed to update role")
    
    update_button = tk.Button(users_frame, text="Update Role", command=update_role)
    update_button.pack(pady=10)
    
    refresh_user_list()

#Helper function for admin panel
def update_user_role(username, new_role):
    users = []
    # Read current users
    with open('passwd.txt', 'r') as file:
        users = [line.strip().split(',') for line in file]
    
    # Update role for matching username
    updated = False
    for i, user in enumerate(users):
        if user[0] == username:
            users[i][2] = new_role
            updated = True
            break
    
    if not updated:
        return False
        
    # Write back to file
    with open('passwd.txt', 'w') as file:
        for user in users:
            file.write(','.join(user) + '\n')
    return True

#Helper function for admin panel
def get_all_users():
    users = []
    with open('passwd.txt', 'r') as file:
        for line in file:
            username, _, role = line.strip().split(',')
            users.append((username, role))
    return users