import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class ExportButton(ttk.Button):
    """A class for handling the exporting of Racing Line"""
    
    def __init__(self, master, upload_features, optimisation_features):
        super().__init__(master, text='Export Racing Line', command=self.export)
                
        # Create button to export track coordinates 
        self.plot_button = ttk.Button(master, text= 'Export Results', command=self.export, width=10)
        #self.plot_button.grid_propagate(False)
        self.plot_button.grid(row=3, column=1,  sticky='', pady=5, padx=25)
        
        # Get track from upload_features
        self.centre_line = upload_features.track_coordinates
        self.inner_bounds = upload_features.track_inner_coords
        self.outer_bounds = upload_features.track_outer_coords
        
        # Get results from optimisation features
        self.racing_line_results = optimisation_features.racing_line_results 
        
        # Process results       
        self.process_results()
   
   
    def process_results(self):
        
        # Add track coordinates to results
        self.racing_line_results['centre_line'] = self.centre_line
        self.racing_line_results['inner_line'] = self.inner_bounds
        self.racing_line_results['outer_line'] = self.outer_bounds
        
        
    def export(self):
        # Convert dictionary to txt file with x and y coordinates
                
        # Ask user for file path        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[('Text files', '*.txt'), ('All files', '*.*')], title='Select Output Destination')
        
        if file_path:
            with open(file_path, 'w') as file:
                # Write headers
                file.write('Key\tX\tY\n')

                # Iterate through dictionary items
                for key, values in file_path.items():
                    for idx, value in enumerate(values):
                        # Write key
                        file.write(f"{key}_{idx+1}\t")

                        # Split the numpy array into x and y coordinates
                        x, y = value
                        file.write(f"{x}\t{y}\n")
                        
            


