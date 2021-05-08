from random import choice
from time import sleep
from turtle import *
from freegames import floor, square, vector

pattern = []
guesses = []
tiles = {
    vector(0, 0): ('red', 'dark red'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(-200, -200): ('yellow', 'khaki'),
}

def grid():
    "Draw grid of tiles."
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'dark blue')
    square(-200, 0, 200, 'dark green')
    square(-200, -200, 200, 'khaki')
    update()

def flash(tile):
    "Flash tile in grid."
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow)
    update()
    sleep(0.5)
    square(tile.x, tile.y, 200, dark)
    update()
    sleep(0.5)

def grow():
    "Grow pattern and flash tiles."
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        flash(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()

def tap(x, y):
    "Respond to screen tap."
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        exit()

    guesses.append(tile)
    flash(tile)

    if len(guesses) == len(pattern):
        grow()

    onscreenclick(tap)

def start(x, y):
    "Start game."
    grow()
    onscreenclick(tap) 
import tkinter as tk
import random

class Simon:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(self.parent, height=400, width=400)
        self.canvas.pack()
        self.dark = {'r':'darkred', 'g':'darkgreen', 'b':'darkblue', 'y':'darkgoldenrod'}
        self.light = {'r':'red', 'g':'green', 'b':'blue', 'y':'goldenrod'}
        self.squares = {'r':self.canvas.create_rectangle(0, 0, 200, 200,
                                              fill='darkred', outline='darkred'),
                        'g':self.canvas.create_rectangle(200, 0, 400, 200,
                                              fill='darkgreen', outline='darkgreen'),
                        'b':self.canvas.create_rectangle(0, 200, 200, 400,
                                              fill='darkblue', outline='darkblue'),
                        'y':self.canvas.create_rectangle(200, 200, 400, 400,
                                              fill='darkgoldenrod', outline='darkgoldenrod')}
        self.ids = {v:k for k,v in self.squares.items()}
        self.high_score = 0
        self.status = tk.Label(root, text='Let\'s go!')
        self.status.pack()
        self.parent.bind('<h>', self.score)
        self.draw_board()
        
    def draw_board(self):
        self.pattern = random.choice('rgby')
        self.selections = ''
        self.parent.after(1000, self.animate)
        
    def animate(self, idx=0):
        c = self.pattern[idx]
        self.canvas.itemconfig(self.squares[c], fill=self.light[c], outline=self.light[c])
        self.parent.after(500, lambda: self.canvas.itemconfig(self.squares[c],
                               fill=self.dark[c], outline=self.dark[c]))
        idx += 1
        if idx < len(self.pattern):
            self.parent.after(1000, lambda: self.animate(idx))
        else:
            self.canvas.bind('<1>', self.select)
    
    def select(self, event=None):
        id = self.canvas.find_withtag("current")[0]
        color = self.ids[id]
        self.selections += color
        self.canvas.itemconfig(id,
                               fill=self.light[color], outline=self.light[color])
        self.parent.after(800, lambda: self.canvas.itemconfig(id,
                               fill=self.dark[color], outline=self.dark[color]))
        if self.pattern == self.selections:
            self.canvas.unbind('<1>')
            self.status.config(text='Right!')
            self.parent.after(2000, lambda: self.status.config(text=''))
            self.pattern += random.choice('rgby')
            self.selections = ''
            self.high_score = max(self.high_score, len(self.pattern))
            self.parent.after(2000, self.animate)
        elif self.pattern[len(self.selections)-1] != color:
            self.canvas.unbind('<1>')
            self.status.config(text='Nope!')
            self.parent.after(2000, lambda: self.status.config(text=''))
            self.parent.after(2000, self.draw_board)
            
    def score(self, event=None):
        self.status.config(text=self.high_score)
        self.parent.after(2000, lambda: self.status.config(text=''))
        
root = tk.Tk()
simon = Simon(root)
root.mainloop()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(start)
done()