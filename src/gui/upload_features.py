import tkinter as tk
from tkinter import *
#from tkinter import filedialog
#from tkinter import Button
#from tkinter.ttk import Label, LabelFrame, Style
import os

class UploadFeatures: 
    
    def __init__(self,master):
        
        # Create a Style instance
        #self.style = ttk.Style()

        # Configure the style for the LabelFrame
        #self.style.configure('My.TLabelframe', background='aqua', font=('Arial', 12))

        # Create the LabelFrame with the configured style
        self.upload_label_frame = LabelFrame(master, text='Please Configure File for Upload')
        self.upload_label_frame.grid(row=1, column=3, columnspan=3, rowspan=4, sticky='ne', pady=40, padx=5)

        self.label_inside_frame = Label(self.upload_label_frame, text='Label inside the frame')
        self.label_inside_frame.grid(row=0, column=0)
        
        
        # Create an Upload button 
        # upload_button = UploadButton(self, upload_callback=self.upload_coordinates)
        # upload_button.grid(row=1, column=1, pady=40, padx=10, sticky='ne')
        
        self.upload_button = Button(self.upload_label_frame, text= 'Upload', command=self.upload_coordinates)
        self.upload_button.grid(row=1, column=0)
        
        
    def upload_coordinates(self):
        print("hello")