import tkinter as tk
from Problem3a4a import login_page

def main():
    root = tk.Tk()
    root.title("justInvest")
    
    # Set a minimum window size
    root.minsize(400, 300)
    
    # Center the window on the screen
    window_width = 450
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    # Show login page first
    login_frame = login_page(root)
    login_frame.pack(padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()