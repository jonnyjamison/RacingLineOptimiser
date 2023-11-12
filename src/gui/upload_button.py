import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os


class UploadButton(ttk.Button):
    """A class for handling the uploading of Track Coordinates"""
    
    def __init__(self, master, upload_callback, **kwargs):
        super().__init__(master, text='Upload Coordinates', command=self.upload, **kwargs)
        self.upload_callback = upload_callback
        self.file_path_label = tk.Label(master, text="Please Select File")
        self.file_path_label.grid(row=1, column=2, pady=40, padx=5, columnspan=2, sticky='ne')

        self.file_path_label.grid_propagate(False)
        
    def upload(self):
        file_path = filedialog.askopenfilename(title='Select Coordinates File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if file_path:
           
            # Update file path label
            filename = os.path.basename(file_path)
            self.file_path_label.config(text=f"File: {filename}")
            
            # Call the upload_coordinates callback with file path
            self.upload_coordinates(file_path)
            

    def upload_coordinates(self, file_path):
        # Method to handle the uploaded coordinates file path
   
        try:
            with open(file_path, 'r') as file:
                
                print("TODO - handle coordinates upload")
                # Read each line from the file
                #for line in file:
                    # Split the line into x and y coordinates
                    #x, y = map(float, line.split())
                    
                    
                    #print(f"Extracted coordinates: x={x}")
                    
            # Call the provided callback with the extracted coordinates
            #self.upload_callback(file_path)
            
        except Exception as e:
            # Handle any exceptions that may occur during file processing
            print(f"Error processing file: {e}")