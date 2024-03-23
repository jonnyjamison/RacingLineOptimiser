from PIL import ImageTk
from PIL.Image import open as pil_open
from tkinter import PhotoImage
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from gui.upload_features import *
from gui.export_button import ExportButton
from gui.optimisation_features import OptimisationFeatures

class GUI(tk.Tk):
    """Class to build all features upon the GUI"""
    
    def __init__(self,rlo):
        super().__init__()
        
        # Load Icon
        icon = PhotoImage(file='images/icon.png')
        self.iconphoto(False, icon)
        
        # Configure the main window
        self.title('Racing Line Optimser')
        self.geometry(rlo.settings.window_size)
        
        # Load and place logo 
        logo_image = pil_open('images/logo.png')
        self.logo = ImageTk.PhotoImage(logo_image)
        self.image_label = tk.Label(self, image=self.logo)
        self.image_label.grid(row=0, column=0, sticky='nw') 

        # Create a Frame to hold the plot
        self.plot_frame = tk.Frame(self)
        self.plot_frame.grid(row=1, column=0, rowspan=4, padx=10, pady=10, sticky="nsew")

        # Create a Matplotlib figure
        self.figure, self.ax = plt.subplots()
        self.ax.set_title('Track Coordinates')

        # Create a FigureCanvasTkAgg to display the figure in tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=1, column=0, rowspan=3, sticky="nsew")

        # Set grid weights to allow resizing
        self.plot_frame.grid_rowconfigure(1, weight=1)
        self.plot_frame.grid_rowconfigure(2, weight=1)
        self.plot_frame.grid_columnconfigure(0, weight=1)

        # Bind the window resize event to update_figure_size function
        self.bind("<Configure>", self.update_figure_size)
 
        # Create instance of UploadFeatures
        self.upload_features = UploadFeatures(self)
        
        # Create instance of OptimisationFeatures
        self.optimisation_features = OptimisationFeatures(self,self.upload_features)
        
        # Create an instance of ExportButton
        export_button = ExportButton(self, self.upload_features, self.optimisation_features)
        

    def start(self):
        # Start the Tkinter main loop
        self.mainloop()
        
    def update_figure_size(self, event):
        # Get the new size of the plot area
        new_width = self.plot_frame.winfo_width()
        new_height = self.plot_frame.winfo_height()

        # Update the figure size to match the new plot area size
        self.figure.set_size_inches(new_width / self.figure.dpi, new_height / self.figure.dpi)
        self.canvas.draw()
        
        