import random
import time
from tkinter import Tk , Button, DISABLED

def show_symbol(x,y):
    global first
    global previousx , previousy
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first:
        previousx = x
        previousy = y
        first = False
    elif previousx !=x or previousy != y:
        if buttons[previousx,previousy]['text'] != buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previousx,previousy]['text'] = ' '
            buttons[x,y]['text'] = ' '
        else:
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True



win = Tk()
win.title('MatchMaker')
win.resizable(width=False , height = False)
first = True
previousx= 0
previousy = 0
buttons = { }
button_symbols = {}
symbols = ['\U0001F600','\U0001F923','\U0001F642','\U0001F643','\U0001F607','\U0001F929',
           '\U0001F618','\U0001F61b','\U0001F92a','\U0001F911','\U0001F917','\U0001F62a',
           '\U0001F600','\U0001F923','\U0001F642','\U0001F643','\U0001F607','\U0001F929',
                      '\U0001F618','\U0001F61b','\U0001F92a','\U0001F911','\U0001F917','\U0001F62a']

random.shuffle(symbols)
#print('\U0001f62a')

for  x in range(6):
    for y in range(4):
        button = Button(command= lambda x=x, y=y: show_symbol(x,y), width= 10 , height = 8)
        button.grid(column = x ,row = y)
        buttons[x,y] = button
        button_symbols[x,y]=symbols.pop()


win.mainloop()
