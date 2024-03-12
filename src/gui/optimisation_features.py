import tkinter as tk
from tkinter import *
from tkinter import LabelFrame, Radiobutton
from optimisation_functions.gradient_descent import gradient_descent



class OptimisationFeatures: 
    
    def __init__(self,master,upload_features):
        
        self.master = master
        self.upload_features = upload_features
        
        # Create label frame for optimisation options        
        self.optimisation_label_frame = LabelFrame(master, text='2. Please Configure Optimisation')
        self.optimisation_label_frame.grid(row=5, column=4, columnspan=10, rowspan=4, sticky='nsew', padx=100)
        
        # Radio Buttons for selecting optimisation methods
        self.GD_selected = tk.IntVar()
        self.GA_selected = tk.IntVar()
        self.PS_selected = tk.IntVar()
        
        self.GD_button = Radiobutton(self.optimisation_label_frame, text="Gradient Descent", variable=self.GD_selected, value=1)
        self.GD_button.grid(row=0, column=0)
        
        self.GA_button = Radiobutton(self.optimisation_label_frame, text="Genetic Algorithm", variable=self.GA_selected, value=1)
        self.GA_button.grid(row=0, column=1)
        
        self.PS_button = Radiobutton(self.optimisation_label_frame, text="Particle Swarm", variable=self.PS_selected, value=1)
        self.PS_button.grid(row=0, column=2)
        
        # Maximum iterations button
        self.max_iterations_label = Label(self.optimisation_label_frame, text="Maximum Iterations:")
        self.max_iterations_label.grid(row=1, column=0) 
        
        self.max_iterations = tk.IntVar()
        self.max_iterations_input = tk.Entry(self.optimisation_label_frame, textvar=self.max_iterations)
        self.max_iterations_input.grid(row=1, column=1, sticky='w', padx = 10)
        
        # Create Optimisation Button
        self.optimise_button = Button(self.optimisation_label_frame, text= 'Optimise', command=self.optimise_track_coordinates)
        self.optimise_button.grid_propagate(False)
        self.optimise_button.grid(row=2, column=1, pady=5, padx=25) 
        
        
    def optimise_track_coordinates(self): #, GD_selected, GA_selected, PS_selected

        
        if self.GD_selected.get():
            print("Performing Gradient Descent Optimisation")
            
            # Perform Optimisation
                # Call GD function
                # inputs -> inner & outer bounds, max iterations
            # Plot results
            gradient_descent(self.upload_features.track_outer_coords, self.upload_features.track_inner_coords, self.max_iterations.get())
            
        if self.GA_selected.get():
            print("Performing Genetic Algorithm Optimisation")
            
        if self.PS_selected.get():
            print("Performing Particle Swarm Optimisation")
            
            
            
        
        
        
        
        
        
        
        
        
         