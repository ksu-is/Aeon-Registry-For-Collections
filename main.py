import tkinter as tk
from tkinter import messagebox
import database # This imports the code you just wrote above!

class AeonRegistryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aeon Registry: Specimen Inventory")
        self.root.geometry("400x500")

        # Labels and Entry Boxes
        tk.Label(root, text="Aeon Specimen Registry", font=("Arial", 16, "bold")).pack(pady=10)

        self.create_input("Common Name (e.g. Crow Feather):", "name")
        self.create_input("Scientific Name:", "sci")
        self.create_input("Location Found:", "loc")

        tk.Label(root, text="Additional Details:").pack()
        self.details_entry = tk.Text(root, height=5, width=35)
        self.details_entry.pack(pady=5)

        # Button to Save
        tk.Button(root, text="Register Finding", command=self.save_data, 
                  bg="#27ae60", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

    def create_input(self, label_text, var_name):
        tk.Label(self.root, text=label_text).pack()
        entry = tk.Entry(self.root, width=40)
        entry.pack(pady=5)
        setattr(self, f"{var_name}_input", entry)

    def save_data(self):
        # Get data from the UI
        name = self.name_input.get()
        sci = self.sci_input.get()
        loc = self.loc_input.get()
        details = self.details_entry.get("1.0", tk.END).strip()

        if not name:
            messagebox.showwarning("Input Error", "Common Name is required!")
            return

        try:
            database.insert_specimen(name, sci, loc, details)
            messagebox.showinfo("Success", f"'{name}' recorded in the registry!")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Could not save to database: {e}")

    def clear_fields(self):
        self.name_input.delete(0, tk.END)
        self.sci_input.delete(0, tk.END)
        self.loc_input.delete(0, tk.END)
        self.details_entry.delete("1.0", tk.END)

if __name__ == "__main__":
    database.create_table() # Ensure table exists on startup
    root = tk.Tk()
    app = AeonRegistryApp(root)
    root.mainloop()
