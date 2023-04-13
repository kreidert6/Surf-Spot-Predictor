import tkinter as tk
from tkinter import *
from unicodedata import name

from pygments import highlight

class GUI: 
    

    def __init__(self):
        self.spotList = []
        self.filteredList = []
        self.spotFeatures = {}
        
        
        # Create window. uses tkinter module to access method from Tk object. Creating object attributes for the method
        self.window = tk.Tk()  
        self.window.title("Surf Recommendor")
        self.window.geometry("700x500")
        self.window.configure(bg = "grey")
        
        
        """Filter by Country label"""
        self.label1 = tk.Label(self.window, text = "Filter by county", fg = "black", bg = "grey")
        self.label1.grid(row = 0, column = 0)


        
    

        self.OCButton = tk.Button(self.window, text = "Orange County", padx= 45, fg = "black", highlightbackground = "grey", width = 5, command = self.OC)
        self.OCButton.grid(row = 1, column = 0)
        self.SDButton = tk.Button(self.window, text = "San Diego County", padx= 45, fg = "black", highlightbackground = "grey", width = 5, command = self.SD)
        self.SDButton.grid(row = 2, column = 0)
        
        
        self.blankLine = tk.Label(self.window, text = "", fg = "black", bg = "grey")
        self.blankLine.grid(row = 3, column = 0)

        self.label2 = tk.Label(self.window, text = "Filter by wave type", fg = "black", bg = "grey")
        self.label2.grid(row = 4, column = 0)

        self.RightsButton = tk.Button(self.window, text = "Rights", padx= 45, fg = "black", highlightbackground= "grey",  width = 5, command = self.getRights)
        self.RightsButton.grid(row = 5, column = 0)

        self.LeftsButton = tk.Button(self.window, text = "Lefts", padx= 45, fg = "black", highlightbackground= "grey", width = 5, command = self.getLefts)
        self.LeftsButton.grid(row = 6, column = 0)



        


        self.my_text = Label(self.window, bg = "grey")
        self.my_text.grid(row = 0, column = 1, rowspan = 5)

        
        self.window.mainloop()
    
    
    
    def listSpots(self, location): 
        
        if location == 0:
             fname = "OrangeCountySurfSpots.txt"
        elif location == 1:
             print("Entered")
             fname = "SanDiegoSurfSpots.txt"
        
        spotFeatures = {}
        
        with open(fname, "r") as f:
            self.names = ""
            for line in f:
                split = line.split(":")
                print(split)
                
                self.spotFeatures[split[0]] = split[1] 
                self.names = self.names + split[0] + "\n"
        


            
            print(self.spotFeatures)
            print("names: " + self.names)
            
        self.my_text.configure(text = self.names)
        
    def filterWaveDirection(self, direction):
        nameList = self.names.split("\n")
        nameList.remove('')
        print(nameList)
        self.names = ""
        for item in nameList:
            print(direction + " " + self.spotFeatures[item])
            if direction in self.spotFeatures[item]:
                
                self.names = self.names + item + "\n"
        print("NAMES: " + self.names)
        self.my_text.configure(text = self.names)
            


    def OC(self):
        
        self.listSpots(0)
        
    def SD(self):
        self.listSpots(1)

    def getRights(self):
        
        self.filterWaveDirection("rights")

    def getLefts(self):
        self.add_button4.configure(fg = "blue")
        self.add_button3.configure(fg = "black")
        self.filterWaveDirection("lefts")

        
        



        
            
            
    
        
        
    
    



if __name__ == "__main__":
    GUI()
