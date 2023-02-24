import sys
import os
import random
from PyQt5 import QtWidgets, QtGui, QtCore
import shutil


class SecureDeletionTool(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.selected_paths = []

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Secure File Deletion Tool")

        # add label
        label = QtWidgets.QLabel("Click the button to securely delete file(s).")

        # add button
        button = QtWidgets.QPushButton("Delete File(s)")
        button.clicked.connect(self.delete_file)

        # add browse file button
        browse_button = QtWidgets.QPushButton("Browse")
        browse_button.clicked.connect(self.browse_file)

        # add filename label
        filename_label = QtWidgets.QLabel("File name(s):")
        self.filename_field = QtWidgets.QTextEdit()
        self.filename_field.setReadOnly(True)

        # create layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(browse_button)
        layout.addWidget(filename_label)
        layout.addWidget(self.filename_field)
        layout.addWidget(button)

        self.setLayout(layout)

    def browse_file(self):
        # Open a file dialog to browse for the file or folder to encrypt/decrypt
        browse_type, ok = QtWidgets.QInputDialog.getItem(self, "Select browse type", "Select browse type:", ["File", "Folder"], 0, False)
        if ok:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            if browse_type == "File":
                file_paths, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Select file", "", "All Files (*)", options=options)
                if file_paths:
                    self.selected_paths += file_paths
                    self.selected_paths = list(set(self.selected_paths))
                    self.filename_field.setText("\n".join(self.selected_paths))
            elif browse_type == "Folder":
                dir_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select folder", "", options=options)
                if dir_path:
                    self.selected_paths.append(dir_path)
                    self.selected_paths = list(set(self.selected_paths))
                    self.filename_field.setText("\n".join(self.selected_paths))

    def overwrite_file(self, file_path):
        # generate random data
        data = os.urandom(os.path.getsize(file_path))

        # overwrite file with random data
        with open(file_path, 'wb') as f:
            f.write(data)

    def delete_directory(self, directory_path):
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            if os.path.isdir(file_path):
                self.delete_directory(file_path)
            else:
                self.overwrite_file(file_path)
                os.remove(file_path)
        os.rmdir(directory_path)

    def delete_file(self):
        # get file path(s)
        paths = self.filename_field.toPlainText().split("\n")

        # check if file(s) or folder(s) exist
        non_existent_paths = []
        for path in paths:
            if not os.path.exists(path):
                non_existent_paths.append(path)

        if len(non_existent_paths) > 0:
            QtWidgets.QMessageBox.warning(self, "File not found", f"The following file(s) or folder(s) could not be found:\n\n{chr(10).join(non_existent_paths)}")
            return

        # ask for confirmation before deleting files
        message_box = QtWidgets.QMessageBox.question(self, "Confirm Deletion", f"Are you sure you want to delete the selected file(s)?\n\n{chr(10).join(paths)}", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        
        if message_box == QtWidgets.QMessageBox.Yes:
            for path in paths:
                if os.path.isdir(path):
                    self.delete_directory(path)
                else:
                    self.overwrite_file(path)
                    os.remove(path)

            # clear filename field   
            self.filename_field.clear()

            # show message box
            QtWidgets.QMessageBox.information(self, "File(s) deleted", "The file(s) have been securely deleted.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tool = SecureDeletionTool()
    tool.show()
    sys.exit(app.exec_())
