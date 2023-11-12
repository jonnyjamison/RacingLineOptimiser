#TODO
#Dynamic placement - update everything to use x y coords, update with window
# size

from settings import Settings
from gui.gui import GUI

class RacingLineOptimiser:
    """Overall class to manage app's assets and behavior."""
    
    def __init__(self):
        # Create Settings instance
        self.settings = Settings()
        
        # Create instance of GUI
        self.gui = GUI(self)

    def run(self):
        # Start the GUI main loop
        self.gui.mainloop()

            
if __name__ == '__main__':
    #Create instance of the App
    rlo = RacingLineOptimiser()
    rlo.run()
    
    