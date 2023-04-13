import tkinter as tk
from tkinter import *
class GUI: 
    

    def __init__(self):
        self.spotList = []
        #self.spotString = self.listSpots

        
    
        # Create window. uses tkinter module to access method from Tk object. Creating object attributes for the method
        self.window = tk.Tk()  
        self.window.title("Surf Recommendor")
        self.window.geometry("700x500")
        self.window.configure(bg = "grey")
        
        
        """NAME PORTION"""
        #Name Label, labels the names through Label and StringVar method and assigns the correct column through grid method
        #self.name_string = tk.StringVar()
        self.name_label = tk.Label(self.window, text = "Filter by county", fg = "black", bg = "white", padx = 45)
        #self.name_label.place(relx=.5, rely=.5,anchor = CENTER)
        self.name_label.place(x=0, y = 0)


        
    #create menu options

        self.add_button1 = tk.Button(self.window, text = "Orange County", padx= 45, fg = "black", bg = "white", width = 5, command = self.OC)
        self.add_button1.place(x = 0, y = 10)
        self.add_button2 = tk.Button(self.window, text = "San Diego County", padx= 45, fg = "black", bg = "white", width = 5, command = self.SD)
        self.add_button2.place(x = 0, y = 20)
        
        # self.name_label2 = tk.Label(self.window, text = "", fg = "black", bg = "white")
        # #self.name_label.place(relx=.5, rely=.5,anchor = CENTER)
        # self.name_label2.place(x = 0, y = 30)

        # self.name_label3 = tk.Label(self.window, text = "Filter by wave type", fg = "black", bg = "white")
        
        # self.name_label3.place(x = 0, y = 40)
        # self.add_button3 = tk.Button(self.window, text = "Rights", padx= 45, fg = "black", bg = "white", width = 5, command = self.OC)
        # self.add_button3.place(x = 0, y = 50)
        # self.add_button4 = tk.Button(self.window, text = "Lefts", padx= 45, fg = "black", bg = "white", width = 5, command = self.SD)
        # self.add_button4.place(x = 0, y = 60)



        # # self.name_label3 = tk.Label(self.window, text = "......", fg = "black", bg = "white")
        # # self.name_label3.grid(row = 4, column = 0)

        


        # self.my_text = Label(self.window)
        # #self.my_text.pack()
        # self.my_text.place(x = 50, y = 0)

        
        
    #file_menu = Menu(my_men
    #my_menu.add_cascade(Label="Skill Level", menu=file_menu)
    # file_menu.add_command(Label = "Beginner", command = our_command)
    # file_menu.add_command(Label= "Intermediate", command = board.quit)
        
        self.window.mainloop()
    def our_command(self):
        pass
    
    
    def listSpots(self, location:int): 
        
        if location == 0:
            fname = "OrangeCountySurfSpots.txt"
        elif location == 1:
            print("Entered")
            fname = "SanDiegoSurfSpots.txt"
        
        with open(fname, "r") as f:
            
            stuff = f.read()
            print(stuff)

            
        self.my_text.configure(text = stuff)
        
        
    def OC(self):
        self.listSpots(0)
        
    def SD(self):
        self.listSpots(1)

        
        



        
            
            
    
        
        
    
    



if __name__ == "__main__":
    GUI()
