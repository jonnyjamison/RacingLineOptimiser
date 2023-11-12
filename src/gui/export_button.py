import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class ExportButton(ttk.Button):
    """A class for handling the exporting of Racing Line"""
    
    def __init__(self, master, export_callback, **kwargs):
        super().__init__(master, text='Export Racing Line', command=self.export, **kwargs)
        
        self.export_callback = export_callback
        
        
        self.button_width = self.winfo_reqwidth()
        self.button_height = self.winfo_reqheight()
        self.x_position = self.winfo_screenwidth() - self.button_width - 400
        self.y_position = self.winfo_screenheight() - self.button_height - 250
        self.place(x=self.x_position, y=self.y_position)
                
    
    def export(self):
        file_path = filedialog.askopenfilename(title='Select Output Destination', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if file_path:
            # Call the provided callback with the selected file path
            self.export_coordinates(file_path)   
            
            
    def export_callback(self):
        print("TODO - Configure export functionality")
    
    