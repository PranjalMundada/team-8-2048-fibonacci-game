import tkinter as tk
import random
import os

fibonacci_numbers=[ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 ]
   
def merge_tiles(row):
    
    for i in range(len(row)-1) :
        number = row[i] + row[i+1]
        if row[i] > 0 and number in fibonacci_numbers  :
                row[i] += row[i + 1]
                row[i + 1] = 0           

def move_left(board):  
    for row in board:
        merge_tiles(row)

def transpose_board(board):
    return [list(row) for row in zip(*board)]

def move_board(board, direction):
    if direction == "left":
        move_left(board)
        os.system('say left') 

    elif direction == "right":
        board = [row[::-1] for row in board]
        move_left(board)
        board = [row[::-1] for row in board]
        os.system('say right') 

    elif direction == "up":
        board = transpose_board(board)
        move_left(board)
        board = transpose_board(board)
        os.system('say up') 

    elif direction == "down":
        board = transpose_board(board)
        board = [row[::-1] for row in board]
        move_left(board)
        board = [row[::-1] for row in board]
        board = transpose_board(board)
        os.system('say down') 

    #os.system('say' + direction) 
    return board

class GamePage(tk.Frame):
    
    def __init__(self, parent_frame, controller ):
        self.stop_flag = False
        self.controller = controller
        grid = controller.matrix_size
        print('matrix_size size is :', grid)
        tk.Frame.__init__(self, parent_frame,bg="light blue")

        self.frame1 = tk.Frame(self,bg="#17202A",width=500,height=300)
        self.frame1.pack()
 
        self.board = self.initialize_board(grid)
        
        self.title_label=tk.Label(self.frame1,  text="ENJOY THE GAME", bg='black', fg = '#641E16', font=("Arial", 30, "bold"))
        self.title_label.grid(row=0, column=0, columnspan =4, pady=3)

        self.score_label=tk.Label(self.frame1,  text="2",fg='#17202A',bg="#FFAACC", font=("Arial", 130, "bold"),  height =7, width=25)
        self.score_label.grid(row=1, column=0, columnspan =4, pady=3)
        self.Score= 2
        
        self.score_label.config( text=("Score", self.Score), font=("light blue", 26))
        
        self.tiles = []
        self.create_widgets(grid)
        
        button = tk.Button(self.frame1, text="Go to the start page",command=lambda: controller.show_frame("StartPage"))
        button.grid(row=grid[0]+2, column=1, columnspan =2)
        
        self.update_board()     

    def initialize_board(self, grid):
        self.board = [[0 for _ in range(grid[0])] for _ in range(grid[1])]
        #print(board)
        self.add_random_tile()
        #print('board after first addition',board)
        self.add_random_tile()
        return self.board

    def create_widgets(self, grid):
        print("create_widgets: grid :", grid)
        for i in range(grid[0]):
            row_tiles = []
            for j in range(grid[1]):
                tile = tk.Label(self.frame1, width=8, height=4, text="",font=("Arial", 20, "bold"), bd=3, relief=tk.RAISED)
                tile.grid(row=i+2, column=j, padx=3, pady=3)
                row_tiles.append(tile)
            self.tiles.append(row_tiles)

    def update_board(self):
        size = len(self.board)
        print('update_board: size is : ', size )
        for i in range(size):
            for j in range(size):
                value = self.board[i][j]
                self.tiles[i][j].config(text=str(value) if value > 0 else "",fg = 'black', bg=self.get_tile_color(value),font=("Arial", 20, "bold"))
        self.check_game_over()

    def get_tile_color(self, value):
        colors = {
            0: "#CDC1B4",
            1: "#E6E6FA",
            2: "#ADFF2F",
            3: "#EE82EE",
            5: "#FF7F50",
            8: "#FFA500",
            13: "#FFD700",
            21: "#FF69B4",
            34: "#FA8072",
            55: "#DB7093",
            89: "#DC143C",
            144: "#D2691E",
            233: "#DDA0DD",
            377: "#CD5C5C",
            610: "#191970",
            987: "#A52A2A",
            1597: "#808000",
            2584: "#191970"    
        }
        return colors.get(value, "#FFFFFF")

    def on_key_press(self, event):
        if self.stop_flag == True:
            return
        print(event)
        direction = None
        if event.keysym in ("Left"):  
            direction = "left"
            
        elif event.keysym in ("Right"):
            direction = "right"
           
        elif event.keysym in ("Up"):
            direction = "up"
            
        elif event.keysym in ("Down"):
            direction = "down"
            
        if direction:
            sum=1
            self.board = move_board(self.board, direction)
            for row in self.board :
                for cell in row:
                    sum = sum + cell
            self.add_random_tile()
            self.update_board()
            self.score_label.config(text = ("Score : ",  sum))                     

    def add_random_tile(self):
        size = len(self.board)
        empty_cells = [(i, j) for i in range(size) for j in range(size) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = 1  
   
    def change(self): 
        self.value=merge_tiles()
        self.Score += self.value      
      
    def check_game_over(self):
        size = self.controller.matrix_size
        
        empty_cells = [(i, j) for i in range(size[0]) for j in range(size[1]) if self.board[i][j] == 0]
             
        if self.Score >= 2584:
            print("you win!")
            os.system('say you win. Your score is {self.score}' + self.Score)

        elif  empty_cells == []:
            print("you lose!")
            os.system('say you lose')     
            os.system('say you win. Your score is '+self.Score)
            self.stop_flag = True
            