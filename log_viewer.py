# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "log_viewer.py" program of Project
# of Programming Principles in Semester 1, 2022.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter files run smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the required modules.
import os
from  tkinter import * # Used to create the GUI.
from  tkinter import messagebox # Used to show pop-up information windows.
import json
from tkinter.font import Font # Used to convert between JSON-formatted text and Python variables. 


class ProgramGUI:
    def __init__(self, title):
        # This is the constructor of the class.
        # It is responsible for loading the log file data and creating the user interface.
        # See the "Constructor of the GUI Class of log_viewer.py" section of the assignment brief.
        self.main = Tk()
        self.main.title(title)
        self.main.geometry("400x150")
        
        self.customFont = Font(weight="bold")
        
        if os.path.exists("logs.txt"):
            with open("logs.txt", "r") as file:
                try:
                    self.logs = json.load(file)
                except ValueError as e:
                    messagebox.showerror("Error", "Invalid file")
                    self.main.destroy() 
                    return
                file.close()
        else:
            messagebox.showerror("Error", "Missing/Invalid file")
            self.main.destroy()
            return            
        
        # variable
        self.current_log = 0
        
        # create Frame widgets
        self.row1 = Frame(self.main, padx=8, pady=4)
        self.row2 = Frame(self.main, padx=8, pady=4)
        self.row3 = Frame(self.main, padx=8, pady=4)
        self.row4 = Frame(self.main, padx=8, pady=4)
        
        # define letters section
        self.lettersLabel = Label(self.row1, width=8, justify="right", text="Letters: ", font=self.customFont)
        self.letters = Label(self.row1, justify="left")
        
        # define used words list
        self.wordsLabel = Label(self.row2, width=8, justify="right", text="Words: ", font=self.customFont)
        self.wordsValues = Label(self.row2, justify="left" )
        
        # define scores section
        self.scoreLabel = Label(self.row3, width=8, justify="right", text="Score: ", font=self.customFont)
        self.scoreValue = Label(self.row3, justify="left")
        
        # pagination section
        self.prevButton = Button(self.row4, text="Previous", command=self.previous_log)
        self.pagination = Label(self.row4, text=f"Log {self.current_log + 1}/{len(self.logs)}")
        self.nextButton  = Button(self.row4, text="Next", command=self.next_log)
        
        self.lettersLabel.pack(side="left")
        self.letters.pack(side="right")
        
        self.wordsLabel.pack(side="left")
        self.wordsValues.pack(side="right")
        
        self.scoreLabel.pack(side="left")
        self.scoreValue.pack(side="right")
        
        self.prevButton.grid(row=0, column=1)
        self.pagination.grid(row=0, column=2)
        self.nextButton.grid(row=0, column=3)
        
        self.row1.pack(anchor="w")
        self.row2.pack(anchor="w")
        self.row3.pack(anchor="w")
        self.row4.pack()
        
        self.show_log()
        self.main.mainloop()
        pass


    # This method displays the current log
    def show_log(self):
        letters = self.logs[self.current_log]["letters"]
        words = self.logs[self.current_log]["words"]
        
        self.letters.config(text=", ".join(letters).upper())
        self.wordsValues.config(text=", ".join(words).upper())
        self.scoreValue.config(text=self.logs[self.current_log]["score"])
        self.pagination.config(text=f"Log {self.current_log + 1}/{len(self.logs)}")
        # This method displays the details of the current log in the GUI.
        # See Point 1 of the "Methods in the GUI class of fruit_test.py" section of the assignment brief.
        pass



    def previous_log(self):
        # This method is called when the user clicks the "Previous" button.
        # See Point 2 of the "Methods in the GUI class of fruit_test.py" section of the assignment brief.
        if self.current_log == 0:
            messagebox.showwarning("Warning", "No previous logs")
            return
        self.current_log -= 1
        self.show_log()
        pass



    def next_log(self):
        # This method is called when the user clicks the "Next" button.
        # See Point 3 of the "Methods in the GUI class of fruit_test.py" section of the assignment brief.
        if self.current_log == len(self.logs) - 1:
            messagebox.showwarning("Warning", "No next logs")
            return
        self.current_log += 1
        self.show_log()
        pass



gui = ProgramGUI("Word Find Log Viewer")