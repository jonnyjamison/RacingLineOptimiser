from PIL import ImageTk
from PIL.Image import open as pil_open
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label, LabelFrame, Style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
#from settings import Settings 
from gui.upload_features import *
from gui.export_button import ExportButton
from gui.optimisation_features import OptimisationFeatures

class GUI(tk.Tk):
    def __init__(self,rlo):
        super().__init__()
        
        # Configure the main window
        self.title('Racing Line Optimser')
        self.geometry(rlo.settings.window_size)
                
        # Load and place logo 
        logo_image = pil_open('images/logo.png')
        self.logo = ImageTk.PhotoImage(logo_image)
        self.image_label = tk.Label(self, image=self.logo)
        self.image_label.grid(row=0, column=0, sticky='nw') 

        # Create a Matplotlib figure to plot Track Coordinates
        self.figure, self.ax = plt.subplots(figsize=(3, 3)) # width, height
        self.ax.set_title('Track')

        # Create a FigureCanvasTkAgg for plotting Track Coords
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().grid(row=1, column=0, rowspan=8, columnspan=2, sticky='nsew')
        
        # Create instance of UploadFeatures
        self.upload_features = UploadFeatures(self)
        
        # Create instance of OptimisationFeatures
        self.optimisation_features = OptimisationFeatures(self,self.upload_features)
        
        # Create an instance of ExportButton
        export_button = ExportButton(self, export_callback=self.export_coordinates)


    def export_coordinates(self, file_path):
        # Forward the call to the RacingLineOptimiser's method
        rlo.export_coordinates(file_path)

    def start(self):
        # Start the Tkinter main loop
        self.mainloop()
