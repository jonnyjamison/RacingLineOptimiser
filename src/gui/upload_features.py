import tkinter as tk
from tkinter import *
from tkinter import filedialog
#from tkinter import Button
#from tkinter.ttk import Label, LabelFrame, Style
import os
from matplotlib.lines import Line2D

class UploadFeatures: 
    
    def __init__(self,master):
        
        self.master = master

        # Initialise variables
        self.track_coordinates = 0
        self.trackwidth = 0

        # Create label frame for upload track options        
        self.upload_label_frame = LabelFrame(master, text='1. Please Select Track Coordinates')
        self.upload_label_frame.grid(row=1, column=4, columnspan=10, rowspan=2, sticky='nsew', pady=40, padx=100)
        
        # Configure column weights to make the label frame expand
        for i in range(10):  # Assuming you have 6 columns, adjust as needed 
            master.columnconfigure(i, weight=1)
        
        # Create an Upload button 
        self.upload_button = Button(self.upload_label_frame, text= 'Upload', command=self.upload_coordinates)
        self.upload_button.grid(row=0, column=0,sticky='nw', pady=5, padx=10)

        # Create a label which updates to display track
        self.filepath_label = Label(self.upload_label_frame, text="Please Select File")
        self.filepath_label.grid(row=0, column=1)

        # Create a label for Track Width
        self.trackwidth_label = Label(self.upload_label_frame, text="Track Width:")
        self.trackwidth_label.grid(row=1, column=0) 

        # Create input box for Track Width
        self.trackwidth = tk.IntVar()
        self.trackwidth_input = tk.Entry(self.upload_label_frame, textvar=self.trackwidth)
        self.trackwidth_input.grid(row=1, column=1, sticky='w', padx = 10) 

        # Create button to plot track
        self.plot_button = Button(self.upload_label_frame, text= 'Plot', command=self.plot_coordinates)
        self.plot_button.grid_propagate(False)
        self.plot_button.grid(row=2, column=0, pady=5, padx=25)



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
        # Method to process the uploaded coordinates
   
        try:
            with open(file_path, 'r') as file:
                
                self.track_x = []
                self.track_y = []

                # Skip the header line
                next(file)
                
                # Initialize track_coordinates as an empty list
                self.track_coordinates = []

                for line in file:
                    # Split the line into x and y coordinates
                    values = line.split()

                    # Check if the line has at least two columns
                    if len(values) >= 2:
                        try:
                            # Convert the values to integers and append to track_coordinates
                            x = int(float(values[0]))
                            y = int(float(values[1]))
                            self.track_coordinates.append((x, y))
                        except ValueError as e:
                            print(f"Error converting values to integers: {e}")
                    else:
                        print("Skipping line with insufficient columns:", line.strip())

            
        except Exception as e:
            # Handle any exceptions that may occur during file processing
            print(f"Error processing file: {e}")


    def plot_coordinates(self):
        # Check if track coordinates are available
        if self.track_coordinates and self.trackwidth.get() > 0:
            # Clear the legend
            self.master.ax.legend().remove()

            # Plot centre line
            centre_line = self.master.ax.plot(*zip(*self.track_coordinates), label='Centre Line', color='red', linestyle='--', dashes=(5, 2))
            
            # Determine track boundaries
            self.get_track_boundaries(self)
            # THIS SHOULD ASSIGN INSIDE AND OUTSIDE TO ATTRIBUTES??
            
            
            # Redraw canvas
            self.master.canvas.draw()
            
            # Calculate outside track coordinates based on inside track coordinates and track width
            # outside_coordinates = [(x + self.trackwidth.get(), y) for x, y in self.track_coordinates]
            # outside_line = self.master.ax.plot(*zip(*outside_coordinates), label='Outside Track', color='blue')
                        
            # # Create Line2D object for the original line (dashed)
            # original_line = Line2D(*zip(*self.track_coordinates), label='Original Track', linestyle='--', color='green')

            # # Add the lines to the axes
            # self.master.ax.add_line(inside_line)
            # self.master.ax.add_line(outside_line)
            # self.master.ax.add_line(original_line)

            # # Set plot title
            # self.master.ax.set_title('Track')

            # # Redraw canvas
            # self.master.canvas.draw()
            
            # # Set axis limits based on track coordinates
            # min_x = min(min(self.track_coordinates, key=lambda x: x[0])[0], min(outside_coordinates, key=lambda x: x[0])[0])
            # max_x = max(max(self.track_coordinates, key=lambda x: x[0])[0], max(outside_coordinates, key=lambda x: x[0])[0])
            # min_y = min(min(self.track_coordinates, key=lambda x: x[1])[1], min(outside_coordinates, key=lambda x: x[1])[1])
            # max_y = max(max(self.track_coordinates, key=lambda x: x[1])[1], max(outside_coordinates, key=lambda x: x[1])[1])

            # self.master.ax.set_xlim(min_x, max_x)
            # self.master.ax.set_ylim(min_y, max_y)
        else:
            print("Invalid track coordinates or track width. Upload coordinates and set track width first.")


    def get_track_boundaries(self):
        # Check if track coordinates and track width are available
        if self.track_coordinates and self.trackwidth.get() > 0:
            
            # Get the track width
            track_width = self.trackwidth.get()

        else:
            print("Invalid track coordinates or track width. Upload coordinates and set track width first.")
            return []