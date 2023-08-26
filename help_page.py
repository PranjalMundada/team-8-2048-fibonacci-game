import tkinter as tk
  
class HelpPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#EB984E")
        self.controller = controller
        
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        T =tk.Text(self, height = 60, width = 200,fg='#17202A', bg='#FFAACC', font = ('Helvetica',25))
        
        l = tk.Label(self, text = "ABOUT THE GAME",fg='#7D3C98',bg="#ADFF2F", font=('Times New Roman bold',70),justify="center")
       
        
        Fact = """
        Swipe to move the numbers around the board. 
        
        Combine numbers that are next to each other in the Fibonacci sequence (1,2,3,5,8,13,20...). 
        
        See if you can get to 2584! 

        The Fibonacci numbers are a list (called a "sequence") of numbers that is built in a very special way.
        
        It starts with 1,1... and then you add 1 + 1 to get to the next number.
        
        That gives 1,1,2... Then you add 1+2 to get the next number...
        
        That gives 1,1,2,3... Then you add 2+3 to get the next number...
        
        That gives 1,1,2,3,5 ... Then you add 3+5 to get the next number...
        
        That gives 1,1,2,3,5,8... Then you add 5+8 and you keep going!
        
        1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
        
        Fibonacci numbers are important because they reflect many patterns found in nature - for example, the pattern of petals on flowers.
        
        Learn more about Fibonacci numbers.
        
        This version is based on the 2048 game by Gabriele Cirulli."""
        l.pack()
        T.pack()
        

        T.insert(tk.END, Fact)
        
    def on_key_press(self, event):
        pass      
        