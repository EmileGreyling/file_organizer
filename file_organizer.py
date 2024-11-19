import os
import shutil
from tkinter import filedialog, messagebox

import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


# Main Organizer class
class FileOrganizerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window title and size
        self.title("File Organizer")
        self.geometry("500x300")

        # Configure grid
        self.grid_columnconfigure(0, weight=1)

        # Heading
        self.label = ctk.CTkLabel(
            self, text="Select Folder To Organize", font=("Arial", 20)
        )
        self.label.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="ew")

        # Folder path entry, triggers file dialog on click
        self.folder_path_var = ctk.StringVar()
        self.entry = ctk.CTkEntry(self, textvariable=self.folder_path_var, width=400)
        self.entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.entry.bind("<Button-1>", lambda e: self.browse_folder())

        # Organize files button
        self.organize_button = ctk.CTkButton(
            self, text="Organize Files", command=self.organize_files
        )
        self.organize_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # Open folder button
        self.open_button = ctk.CTkButton(
            self, text="Open Folder", command=self.open_folder
        )
        self.open_button.grid(row=3, column=0, padx=10, pady=(5, 20), sticky="ew")

    # Open folder selection dialog when entry is clicked
    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path_var.set(folder_selected)

    # Organize files by extension
    def organize_files(self):
        folder_path = self.folder_path_var.get()
        if not folder_path or not os.path.isdir(folder_path):
            messagebox.showerror("Error", "Please select a valid folder.")
            return

        # Go through each file in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                # Get the file extension
                file_extension = os.path.splitext(filename)[1][1:]  # Remove the dot
                if file_extension:  # Ignore files without an extension
                    destination_folder = os.path.join(
                        folder_path, file_extension.upper()
                    )
                    os.makedirs(destination_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(destination_folder, filename))

        messagebox.showinfo("Success", "Files organized by extension.")

    # Open the organized folder in the file explorer
    def open_folder(self):
        folder_path = self.folder_path_var.get()
        if folder_path and os.path.isdir(folder_path):
            os.startfile(
                folder_path
            )  # This works on Windows; adjust for other OS if needed
        else:
            messagebox.showerror("Error", "Please select a valid folder to open.")


if __name__ == "__main__":
    app = FileOrganizerApp()
    app.mainloop()
