<div id="header" align="center">
<h1> PyQt5 SecureDeletion Tool </h1>
</div>



<div id="header" align="center">
  <img src="https://image.noelshack.com/fichiers/2023/08/5/1677260751-gui.jpg">
</div>

# Introduction
 
Secure File Deletion Tool is a simple GUI application that allows you to securely delete files and folders. The tool overwrites the files with random data before deleting them to ensure that they cannot be recovered.

With this tool, you can safely delete sensitive files and folders without worrying about anyone else accessing them.

# Installation
 
1. Clone the repository or download the zip file.
```bash
git clone https://github.com/busirus/PyQt5-SecureDeletion-Tool.git
```
2. Make sure that Python 3.x is installed.

3. Install the required libraries by running the following command in the terminal:
```bash
pip install PyQt5
```
4. Run the program by executing the following command:
```bash
python main.py
```

# Usage
1. Open the application by running the program.

2. Click on the "Browse" button to select the file(s) or folder(s) you want to delete.

3. Select either "File" or "Folder" from the drop-down list, and browse for the file(s) or folder(s) to delete.

4. Before deleting, you can review the selected file(s) or folder(s) in the "File name(s):" field.

5. Click the "Delete File(s)" button to securely delete the selected files, you can recheck selection and confirm the deletion.


# How it works
The Secure File Deletion Tool overwrites the selected file(s) or folder(s) with random data using the os.urandom function in Python's os library. This overwriting process ensures that the original file data is permanently erased and cannot be recovered using data recovery software. After overwriting the file, the tool then deletes it using the os.remove function.

If the selected item is a folder, the tool will recursively delete all files and folders within it before deleting the folder itself.

# License 
This project is licensed under the MIT License. 
