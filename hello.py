import tkinter as tk
from tkinter import ttk

roles = ["guest", "admin", "user"]

class EndPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.frm = ttk.Frame(parent, padding=100)
        self.frm.grid()

        ttk.Label(self.frm, text="Nice").grid(column=0, row=2, padx=5, pady=5)

class LoginPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.frm = ttk.Frame(parent, padding=100)
        self.frm.grid()

        self.role = tk.StringVar()
        self.role.set(roles[1])

        # Name
        ttk.Label(self.frm, text="Name:").grid(column=0, row=0, padx=5, pady=5)
        self.nameEntry = ttk.Entry(self.frm)
        self.nameEntry.grid(column=1, row=0, padx=5, pady=5)

        # Role
        ttk.Label(self.frm, text="Role:").grid(column=0, row=1, padx=5, pady=5)
        role_menu = ttk.Combobox(self.frm, textvariable=self.role, values=roles)
        role_menu.grid(column=1, row=1, padx=5, pady=5)

        # Password
        ttk.Label(self.frm, text="Password:").grid(column=0, row=2, padx=5, pady=5)
        self.passwordEntry = ttk.Entry(self.frm, show="*")
        self.passwordEntry.grid(column=1, row=2, padx=5, pady=5)

        ttk.Button(self.frm, text="Login", command=self.buttonPress).grid(column=1, row=4)
    
    def buttonPress(self):
        self.frm.destroy()
        EndPage(self.parent)


def main():
    root = tk.Tk()
    root.title("Staff Login Form")
    LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
