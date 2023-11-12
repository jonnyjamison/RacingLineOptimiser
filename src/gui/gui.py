from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from settings import Settings 
from gui.upload_button import UploadButton
from gui.export_button import ExportButton

class GUI(tk.Tk):
    def __init__(self,rlo):
        super().__init__()
        
        # Configure the main window
        self.title('Racing Line Optimser')
        self.geometry(rlo.settings.window_size)
        
        # Load and place logo 
        logo_image = Image.open('images/logo.png')
        self.logo = ImageTk.PhotoImage(logo_image)
        self.image_label = tk.Label(self, image=self.logo)
        self.image_label.grid(row=0, column=0, sticky='nw') 

        # Create a Matplotlib figure to plot Track Coordinates
        self.figure, self.ax = plt.subplots(figsize=(7, 6)) # width, height
        self.ax.set_title('Track')

        # Create a FigureCanvasTkAgg for plotting Track Coords
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().grid(row=1, column=0, sticky='nsew')

        # Create an instance of UploadButton
        upload_button = UploadButton(self, upload_callback=self.upload_coordinates)
        upload_button.grid(row=1, column=1, pady=40, padx=10, sticky='ne')

        # Create an instance of ExportButton
        export_button = ExportButton(self, export_callback=self.export_coordinates)
        #export_button.place(x=300, y=200)
        #export_button.grid_propagate(False)

    def upload_coordinates(self, file_path):
        # Forward the call to the RacingLineOptimiser's method
        upload_button.upload_coordinates(file_path)
        
    def export_coordinates(self, file_path):
        # Forward the call to the RacingLineOptimiser's method
        export_button.export_coordinates(file_path)

    def start(self):
        # Start the Tkinter main loop
        self.mainloop()
