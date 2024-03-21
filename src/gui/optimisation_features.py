import tkinter as tk
from tkinter import *
from tkinter import LabelFrame, Radiobutton
from optimisation_functions.gradient_descent import gradient_descent
from optimisation_functions.genetic_algorithm import genetic_algorithm

class OptimisationFeatures: 
    
    def __init__(self,master,upload_features):
        
        self.master = master
        self.upload_features = upload_features
        
        # Create label frame for optimisation options        
        self.optimisation_label_frame = LabelFrame(master, text='2. Please Configure Optimisation')
        self.optimisation_label_frame.grid(row=2, column=1, columnspan=1, sticky='', padx=10)
        
        # Ensure all columns are eqaal width 
        self.optimisation_label_frame.columnconfigure(0, weight=1, uniform="col_uniform")
        self.optimisation_label_frame.columnconfigure(1, weight=1, uniform="col_uniform")
        self.optimisation_label_frame.columnconfigure(2, weight=1, uniform="col_uniform")
        
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
        
        # Add deselected state value
        self.GD_button.deselect()
        self.GA_button.deselect()
        self.PS_button.deselect()
        
        # Maximum iterations label
        self.max_iterations_label = Label(self.optimisation_label_frame, text="Maximum Iterations:")
        self.max_iterations_label.grid(row=1, column=0, columnspan=2, sticky = '') 
        
        # Maximum iterations input
        self.max_iterations = tk.IntVar()
        self.max_iterations_input = tk.Entry(self.optimisation_label_frame, textvar=self.max_iterations, width = 4)
        self.max_iterations_input.grid(row=1, column=2, sticky='w', padx = 10)
        
        # Create Optimisation Button
        self.optimise_button = Button(self.optimisation_label_frame, text= 'Optimise', command=self.optimise_track_coordinates)
        self.optimise_button.grid_propagate(False)
        self.optimise_button.grid(row=2, column=1, pady=5, padx=25) 
                
        # Disable Optimise button until track coordinates uploaded
        # if hasattr(self.upload_features, 'track_inner_coords') and self.upload_features.track_inner_coords is not None:
        #     self.optimise_button.config(state=tk.NORMAL)
        # else:
        #     self.optimise_button.config(state=tk.DISABLED)
        
        
    def optimise_track_coordinates(self): #, GD_selected, GA_selected, PS_selected

        print(len(self.upload_features.track_inner_coords))
        
        if self.GD_selected.get():
            print("Performing Gradient Descent Optimisation")
            tk.messagebox.showinfo("Please wait", "Gradient Descent optimisation in progress...")
            
            # Perform Gradient Descent Optimisation            
            self.GD_coordinates = gradient_descent(self.upload_features.track_coordinates,  
            self.upload_features.track_inner_coords, self.upload_features.track_outer_coords, self.max_iterations.get())
            
            print(self.upload_features.track_coordinates - self.GD_coordinates)
                                    
            # Plot results on main GUI
            GD_plot = self.master.ax.plot(*zip(*self.GD_coordinates), label='Gradient Descent', color='magenta', linestyle='-')
            
            # Redraw canvas
            self.master.canvas.draw()
            
            self.master.after(0, tk.messagebox.showinfo, "Calculation Completed", "Gradient Descent completed!")
            
        if self.GA_selected.get():
            print("Performing Genetic Algorithm Optimisation")
            tk.messagebox.showinfo("Please wait", "Genetic Algorithm optimisation in progress...")
            
            # Perform Gradient Descent Optimisation            
            self.GA_coordinates = genetic_algorithm(self.upload_features.track_coordinates,  
            self.upload_features.track_inner_coords, self.upload_features.track_outer_coords, self.max_iterations.get())
            
            print(self.upload_features.track_coordinates - self.GA_coordinates)
                                    
            # Plot results on main GUI
            GA_plot = self.master.ax.plot(*zip(*self.GA_coordinates), label='Genetic Algorithm', color='yellow', linestyle='-')
            
            # Redraw canvas
            self.master.canvas.draw()
            
            self.master.after(0, tk.messagebox.showinfo, "Calculation Completed", "Genetic Algorithm completed!")
            
        if self.PS_selected.get():
            print("Performing Particle Swarm Optimisation")
            
        
        
        
        
        
        
        
         