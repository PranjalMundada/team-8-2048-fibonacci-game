import tkinter as tk
from start_page import StartPage
from game_page import GamePage
from help_page import HelpPage

class Controller():
    
    def __init__(self, root):
        self.root = root
        self.matrix_size = [4,4]
        self.initialize( self.matrix_size)
        self.show_frame("StartPage")

        
    def initialize(self, matrix):
        self.matrix_size = matrix
        print('initialize getting called', matrix )     

        self.container = tk.Frame(self.root, bg='blue')
        
        self.container.pack(side="top", fill="both", expand=True)
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
     
        for page in (StartPage, GamePage, HelpPage): 
            print(page)
            page_name = page.__name__
            frame = page(self.container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[page_name] = frame

    
    def show_frame(self, page_name):
        self.current_frame = self.frames[page_name]
        #print(self.current_frame)
        self.current_frame.tkraise()
        
    def show_frame_with_matrix(self, page_name, matrix):
        self.matrix_size = matrix
        
        if page_name == 'GamePage':
            temp_frame = GamePage(self.container, self)
            temp_frame.grid(row=0, column=0, sticky="nsew")
            
            print('Newly created frame is : ', temp_frame)
            self.frames['GamePage'] = temp_frame
            self.current_frame = self.frames[page_name]
        
        self.current_frame.tkraise()
        
    def on_key_press(self, event):
        print('Controller : on_key_press')
        self.current_frame.on_key_press( event)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fibonacci Number Game")
    controller = Controller(root)
    root.bind("<Key>", controller.on_key_press)

    root.mainloop()