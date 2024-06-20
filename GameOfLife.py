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
        self.canvas.bind("<Button-1>", self.toggle_cell)
        self.master.bind("<space>", self.toggle_running)

    def create_row(self, cols):
        "Create a row of cells."
        return [Cell() for _ in range(cols)]

    def create_grid(self, rows, cols): #create the grid calling the function create row
        "Creates a complete grid of cells"
        return [self.create_row(cols) for _ in range(rows)]
    