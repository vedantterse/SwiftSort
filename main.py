import tkinter as tk
from tkinter import filedialog
import os
import shutil
import zipfile
import sys

# Function to handle clutter removal
def clutter_remover(source_folder):
    try:
        
        if not os.path.exists(source_folder):
            raise FileNotFoundError("Source folder does not exist.")

         
        if not os.listdir(source_folder):
            raise ValueError("Source folder is empty.")

        
        file_types = {
            'png': 'PNG',
            'jpg': 'JPG',
            'pdf': 'PDF',
            'txt': 'Text',
            # Add more file types as needed
        }

        # Walk through the source folder and move files to their respective folders
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_name, file_extension = os.path.splitext(file)
                if file_extension.lower()[1:] in file_types:
                    destination_folder = file_types[file_extension.lower()[1:]]
                else:
                    destination_folder = file_extension.lower()[1:]  # Use the extension name as folder name
                destination_path = os.path.join(source_folder, destination_folder)
                os.makedirs(destination_path, exist_ok=True)
                destination_file = os.path.join(destination_path, file)

                # Check if destination file already exists
                if os.path.exists(destination_file):
                    new_file_name = file_name + "_duplicate" + file_extension
                    destination_file = os.path.join(destination_path, new_file_name)

                shutil.move(os.path.join(root, file), destination_file)

        return "Clutter removed successfully!"
    except (FileNotFoundError, OSError) as e:
        return f"Error: {e}"
    except ValueError as e:
        return f"Error: {e}"

# Function to handle folder zip
def folder_zip(source_folder):
    try:
         
        if not os.path.exists(source_folder):
            raise FileNotFoundError("Source folder does not exist.")

        
        zip_file_path = os.path.join(os.path.dirname(source_folder), 'organized_files.zip')
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(source_folder):
                for file in files:
                    zip_file.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), source_folder))

        return "Source folder compressed into organized_files.zip!"
    except (FileNotFoundError, OSError) as e:
        return f"Error: {e}"

# Function to handle PNG renaming
def rename_pngs(source_folder):
    try:
         
        if not os.path.exists(source_folder):
            raise FileNotFoundError("Source folder does not exist.")

        
        png_files = [file for file in os.listdir(source_folder) if file.lower().endswith('.png')]

        
        png_files.sort(key=lambda x: os.stat(os.path.join(source_folder, x)).st_mtime)

        # Rename PNG files sequentially
        for i, png_file in enumerate(png_files):
            new_name = str(i + 1) + '.png'
            os.rename(os.path.join(source_folder, png_file), os.path.join(source_folder, new_name))

        return "PNG files renamed successfully!"
    except (FileNotFoundError, OSError) as e:
        return f"Error: {e}"
 
def main():
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Clutter Manager Tool")
    root.geometry("300x350")  # Adjusted window size

     
    gradient_bg = "#64649f"
    root.configure(bg=gradient_bg)

    # Create a frame for the main content
    frame = tk.Frame(root, bg="#64649f", padx=20, pady=20)
    frame.pack(expand=True, fill="both")

    # Function to handle button clicks
    def handle_click(choice):
        source_folder = filedialog.askdirectory(title="Select Folder")
        if source_folder:
            message = ""
            if choice == 1:
                message = clutter_remover(source_folder)
            elif choice == 2:
                message = folder_zip(source_folder)
            elif choice == 3:
                message = rename_pngs(source_folder)
            # Display the message in the GUI
            result_label.config(text=message)

     
    button1 = tk.Button(frame, text="Clean Clutter", command=lambda: handle_click(1), bg="#FFD700", fg="black")
    button1.pack(pady=10)
    button2 = tk.Button(frame, text="Zip Folder", command=lambda: handle_click(2), bg="#FFD700", fg="black")
    button2.pack(pady=10)
    button3 = tk.Button(frame, text="Rename PNGs", command=lambda: handle_click(3), bg="#FFD700", fg="black")
    button3.pack(pady=10)

     
    result_label = tk.Label(frame, text="", bg="#64649f", font=("Arial", 14), wraplength=250, justify="left")
    result_label.pack(pady=20)

    
    root.mainloop()

 
if __name__ == "__main__":
    main()
