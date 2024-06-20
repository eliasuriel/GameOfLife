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

        self.canvas.bind("<Button-1>", self.toggle_cell)
        self.master.bind("<space>", self.toggle_running)
    pass