import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from matplotlib.lines import Line2D
import numpy as np

class UploadFeatures: 
    
    def __init__(self,master):
        
        self.master = master

        # Initialise variables
        self.track_coordinates = 0
        self.track_inner_coords = 0
        self.track_outer_coords = 0
        self.trackwidth = 0

        # Create label frame for upload track options        
        self.upload_label_frame = LabelFrame(master, text='1. Please Select Track Coordinates', width=35)
        self.upload_label_frame.grid(row=1, column=1, columnspan=1, rowspan=1, pady=10, padx=0, sticky='')
        
        # Configure column weights to make them of even sizes
        # Makes sure widgets are exactly in the middle 
        # col_uniform stops columns from resizing elements are updated
        self.upload_label_frame.columnconfigure(0, weight=1, uniform="col_uniform")
        self.upload_label_frame.columnconfigure(1, weight=1, uniform="col_uniform")
                
        # Create an Upload button 
        self.upload_button = Button(self.upload_label_frame, text= 'Upload', command=self.upload_coordinates)
        self.upload_button.grid(row=0, column=0,sticky='', pady=5, padx=2)

        # Create a label which updates to display track
        self.filepath_label = Label(self.upload_label_frame, text="Please Select File")
        self.filepath_label.grid(row=0, column=1, sticky='w')

        # Create a label for Track Width
        self.trackwidth_label = Label(self.upload_label_frame, text="Track Width:")
        self.trackwidth_label.grid(row=1, column=0, sticky='e') 

        # Create input box for Track Width
        self.trackwidth = tk.IntVar()
        self.trackwidth_input = tk.Entry(self.upload_label_frame, textvar=self.trackwidth, width=3)
        self.trackwidth_input.grid(row=1, column=1, sticky='w', padx = 10)
        
        # Create button to plot track
        self.plot_button = Button(self.upload_label_frame, text= 'Generate', command=self.plot_coordinates)
        #self.plot_button.grid_propagate(False)
        self.plot_button.grid(row=2, column=0, columnspan=2, sticky='nsew', pady=5, padx=130)


    def upload_coordinates(self):
        # Use file dialoug for user to select track coordinates
        file_path = filedialog.askopenfilename(title='Select Coordinates File', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        
        if file_path:

            # Update file path label
            filename = os.path.basename(file_path)
            
            # Shorten filename if it is too long
            if len(filename) > 20:
                filename = filename[:17]
                filename += "..."
            
            self.filepath_label.config(text=f"File: {filename}")
            
            # Call the upload_coordinates callback with file path
            self.process_coordinates(file_path)
            
            
    def process_coordinates(self,file_path):
        # Method to process the uploaded coordinates
   
        try:
            with open(file_path, 'r') as file:
                
                # Skip the header line
                next(file)
                
                # Initialize track_coordinates as an empty list
                self.track_coordinates = []
                                
                # Load track coordinates into NumPy array
                self.track_coordinates = np.loadtxt(file, skiprows=0, usecols=(0, 1))

        except Exception as e:
            # Handle any exceptions that may occur during file processing
            print(f"Error processing file: {e}")


    def plot_coordinates(self):
        # Check if track coordinates are available
        if self.track_coordinates.size and self.trackwidth.get() > 0:
            
            # Clear the plot
            self.master.ax.clear()
                        
            # Clear the legend
            self.master.ax.legend().remove()

            # Plot centre line
            centre_line = self.master.ax.plot(*zip(*self.track_coordinates), label='Centre Line', color='blue', linestyle='--', dashes=(5, 2))
            
            # Determine track boundaries
            self.get_track_boundaries()
                        
            inside_line = self.master.ax.plot(self.track_inner_x, self.track_inner_y, label='Inside Line', color='red', linestyle='-')
            outside_line = self.master.ax.plot(self.track_outer_x, self.track_outer_y, label='Outside Line', color='red', linestyle='-')

            # Redraw canvas
            self.master.canvas.draw()
            
        else:
            print("Invalid track coordinates or track width. Upload coordinates and set track width first.")


    def get_track_boundaries(self):
   
        # Get the track width
        track_width = self.trackwidth.get()
        
        # Seperate track coordinates into x and y
        self.track_x = self.track_coordinates[:,0]
        self.track_y = self.track_coordinates[:,1]

        # Normal direction of each vertex
        dx = np.gradient(self.track_x)
        dy = np.gradient(self.track_y)
        
        # Euclidean distance at each point
        dL = np.hypot(dx,dy)
                
        # Calculate inner & outer coordinates
        self.track_outer_x = (track_width/2) * (dy/dL) + self.track_x
        self.track_outer_y = (-1 * (track_width/2)) * (dx/dL) + self.track_y
        self.track_inner_x = (-1 * (track_width/2)) * (dy/dL) + self.track_x
        self.track_inner_y = (track_width/2) * (dx/dL) + self.track_y
        
        # Combine outer and inner coordinates
        self.track_outer_coords = np.column_stack((self.track_outer_x, self.track_outer_y))
        self.track_inner_coords = np.column_stack((self.track_inner_x, self.track_inner_y))
        