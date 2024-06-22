import tkinter as tk
from celda import *

class GameOfLife:
    def __init__(self,window, rows, cols, size):
        self.window = window
        self.rows = rows
        self.cols = cols
        self.size = size
        self.canvas = tk.Canvas(window, width=self.cols * self.size, height=self.rows * self.size, bg="white")
        self.canvas.pack()
        self.cells = self.create_grid(self.rows, self.cols) #create list of list of Object Cell
        self.running = False 

        self.canvas.bind("<Button-1>", self.toggle_cell)
        self.window.bind("<space>", self.toggle_running)

        self.draw_grid()
        self.update()

    def create_row(self, cols):
        "Create a row of cells."
        return [Cell() for _ in range(cols)]

    def create_grid(self, rows, cols): #create the grid calling the function create row
        "Creates a complete grid of cells"
        return [self.create_row(cols) for _ in range(rows)]
    
    def toggle_cell(self, event):
        "Change the state of a cell when you click"
        col = event.x // self.size
        row = event.y // self.size
        self.cells[row][col].state = not self.cells[row][col].state
        self.draw_grid()

    def toggle_running(self, event):
        "Start or stop the game "
        self.running = not self.running
        if self.running:
            self.update()

    def draw_grid(self):
        "Draw the grid in canvas "
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.size # x1 and y1 are the coordinates of the upper left corner of the rectangle.
                y1 = row * self.size
                x2 = x1 + self.size #x2 and y2 are the coordinates of the lower right corner of the rectangle.
                y2 = y1 + self.size
                color = "black" if self.cells[row][col].state else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def count_live_neighbors(self, row, col):
        "Count the neighbors that are alive."
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] #to know the neighbours of the cell select
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc #calculate the row and column
            if 0 <= r < self.rows and 0 <= c < self.cols and self.cells[r][c].state: #checked if the neighbor coordinates are within the grid boundaries and if the cell at that position is alive .
                count += 1
        return count
    
    def update(self):
        "Update the state of the game."
        if self.running:
            for row in range(self.rows):
                for col in range(self.cols):
                    live_neighbors = self.count_live_neighbors(row, col)
                    self.cells[row][col].following_state(live_neighbors)
                    
            for row in range(self.rows):
                for col in range(self.cols):
                    self.cells[row][col].update_state()

            self.draw_grid()
            self.master.after(100, self.update)
    

    