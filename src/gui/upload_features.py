import tkinter as tk
from tkinter import *
from tkinter import filedialog
#from tkinter import Button
#from tkinter.ttk import Label, LabelFrame, Style
import os

class UploadFeatures: 
    
    def __init__(self,master):
        
        # Create a Style instance
        #self.style = ttk.Style()

        # Configure the style for the LabelFrame
        #self.style.configure('My.TLabelframe', background='aqua', font=('Arial', 12))
        
        self.upload_label_frame = LabelFrame(master, text='Please Configure File for Upload')
        self.upload_label_frame.grid(row=1, column=4, columnspan=10, rowspan=2, sticky='nsew', pady=40, padx=100)
        
        # Configure column weights to make the label frame expand
        for i in range(10):  # Assuming you have 6 columns, adjust as needed 
            master.columnconfigure(i, weight=1)

        # self.label_inside_frame = Label(self.upload_label_frame, text='Label inside the frame')
        # self.label_inside_frame.grid(row=0, column=0)
        
        
        
        # upload_button = UploadButton(self, upload_callback=self.upload_coordinates)
        # upload_button.grid(row=1, column=1, pady=40, padx=10, sticky='ne')
        
        # Create an Upload button 
        self.upload_button = Button(self.upload_label_frame, text= 'Upload', command=self.upload_coordinates)
        self.upload_button.grid(row=0, column=0,sticky='nw', pady=5, padx=10)
        self.filepath_label = Label(self.upload_label_frame, text="Please Select File")
        self.filepath_label.grid(row=0, column=1)
        
        
    def upload_coordinates(self):
        # Use file dialoug for user to select track coordinates
        file_path = filedialog.askopenfilename(title='Select Coordinates File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        
        if file_path:

            # Update file path label
            filename = os.path.basename(file_path)
            self.filepath_label.config(text=f"File: {filename}")
            
            # Call the upload_coordinates callback with file path
            self.process_coordinates(file_path)
            
    def process_coordinates(self,file_path):
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