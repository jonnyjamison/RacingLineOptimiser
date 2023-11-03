import tkinter as tk
from tkinter import ttk
from tkinter import filedialog



class UploadButton(ttk.Button):
    """A class for handling the uploading of Track Coordinates"""
    
    def __init__(self, master, upload_callback, **kwargs):
        super().__init__(master, text='Upload Coordinates', command=self.upload, **kwargs)
        self.upload_callback = upload_callback
        
    def upload(self):
        file_path = filedialog.askopenfilename(title='Select Coordinates File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if file_path:
            # Call the provided callback with the selected file path
            self.upload_coordinates(file_path)

    def upload_coordinates(self, file_path):
        # Method to handle the uploaded coordinates file path
        # You can add your logic to process the file path here
        print(f"Uploaded coordinates file: {file_path}")