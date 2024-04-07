# Making Your Own .exe File with PyInstaller

Follow these steps to create your own .exe file using PyInstaller:

## Prerequisites
- Python installed on your system.
- PyInstaller package installed (you can install it using pip).

## Steps

### Step 1: Install PyInstaller
```bash
py -m pip install pyinstaller
```
Step 2: Navigate to Your Python File
Navigate to the directory containing your Python file that you want to convert to an executable.

Step 3: Run PyInstaller
Use the following command to convert your Python file to an executable:
```bash
py -m PyInstaller myfile.py
```
Replace myfile.py with the actual name of your Python file.

Step 4: Locate the .exe File
After PyInstaller has finished, navigate to the **dist** directory inside your project folder. You will find the .exe file there.

Step 5: Running the .exe File
You can run the .exe file by double-clicking on it. 


Step 6: Creating a Run.bat File
To create a batch file for easy execution, follow these steps:

Open a text editor (e.g., Notepad).
Paste the following code into the text editor:
```batch
@echo off
cd /d %~dp0
start "" myfile.exe
```
Replace myfile.exe with the actual name of your .exe file.

Save the file with the extension .bat, for example, run.bat.

Step 7: Running the Batch File
To run your application using the batch file, simply double-click on the run.bat file.
