import tkinter as tk
from PIL import ImageTk, Image
from tkmacosx import Button


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#D2B4DE")
        self.controller = controller
        
        temp_image = Image.open('ScreenshotWallPaper.png')
        temp_image = temp_image.resize((1770, 270))

        img = ImageTk.PhotoImage(temp_image)

        label1 =tk.Label(self, image = img, height=250, width=1000)
        label1.pack(fill='x')
        label1.image = img
        
        label2 = tk.Label(self, text="2048 FIBONACCI GAME",fg='#CD6155',bg="#283747",height=4, font=('Times New Roman bold',60))
        label2.pack(side="top", fill="x", pady=10)
        
        button1 = Button(self, text=" 4 x 4 GRID ", fg='#1B4F72',bg='green', width=600,height=50, font=('Times New Roman bold',30), command=lambda: controller.show_frame_with_matrix('GamePage', [4,4]), bd = '10')
        button1.pack(pady=10)
        #button1.configure(activebackground='#ffb3fa', activeforeground='#ffb3fa' )
        button2 = Button(self, text=" 5 x 5 GRID ",fg='#1B4F72',bg='#20B2AA',width=600,height=50, font=('Times New Roman bold',30), command= lambda: controller.show_frame_with_matrix("GamePage", [5,5]), bd = '10')
        button2.pack(pady=10)
        button3 =Button(self, text=" 6 x 6 GRID ",fg='#1B4F72',bg='#D8BFD8', width=600,height=50, font=('Times New Roman bold',30), command=lambda: controller.show_frame_with_matrix("GamePage", [6,6]),bd = '10')
        button3.pack(pady=10)
        button4 = Button(self, text=" ABOUT GAME ",fg='#1B4F72',bg='#BC8F8F', width=600, height=50, font=('Times New Roman bold',30), command=lambda: controller.show_frame("HelpPage"),bd = '10')
        button4.pack(pady=10)
    
    def on_key_press(self, event):
        pass

