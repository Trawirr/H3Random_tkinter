from tkinter import *
from PIL import ImageTk
from os import listdir
from os.path import isfile, join
import numpy as np


class H3Picker:
    def __init__(self):
        self.root = Tk()
        self.root.title('Heroes 3 - Random Heroes Picker')
        self.root.geometry('1200x593')
        self.root.configure(background='red')

        background_image = ImageTk.PhotoImage(file='background3.png')
        width, height = background_image.width(), background_image.height()
        background_label = Label(self.root, image=background_image)
        background_label.place(x=0, y=20, relwidth=1, relheight=1)

        button = Button(self.root, text="Pick heroes", bg='gray', fg='black', command=(lambda: self.roll()))
        button.pack(side="bottom")

        top = Frame(self.root, width=1200, height=50)
        top.pack(side=TOP)

        self.ban1 = Text(self.root, width=75, height=1)
        self.ban1.pack(in_=top, side=LEFT)
        self.ban1.insert(END, 'Type numbers of towns to be banned for player 1')
        self.ban1.bind("<Button-1>", self.clear_text)

        self.ban2 = Text(self.root, width=75, height=1)
        self.ban2.pack(in_=top, side=RIGHT)
        self.ban2.insert(END, 'Type numbers of towns to be banned for player 2')
        self.ban2.bind("<Button-1>", self.clear_text)

        self.root.mainloop()

    def clear_text(self, event):
        event.widget.delete('1.0', END)

    def roll(self):
        banned1 = self.ban1.get('1.0', END)
        banned2 = self.ban2.get('1.0', END)
        print(banned1, banned2)
        print("roll")
        mypath = "heroes"
        heroes = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        if banned1 == '' or banned1 == 'Type numbers of towns to be banned for player 1\n':
            player1 = f"{mypath}/{heroes[np.random.randint(len(heroes))]}"
        else:
            while True:
                banned = False
                player1 = f"{mypath}/{heroes[np.random.randint(len(heroes))]}"
                if not banned1:
                    break
                for b in banned1:
                    #print(f'player1 - {b}, {player1}')
                    if b in player1:
                        banned = True
                        break
                if banned:
                    continue
                break

        if banned2 == '' or banned2 == 'Type numbers of towns to be banned for player 2\n':
            player2 = f"{mypath}/{heroes[np.random.randint(len(heroes))]}"
        else:
            while True:
                banned = False
                player2 = f"{mypath}/{heroes[np.random.randint(len(heroes))]}"
                if not banned2:
                    break
                for b in banned2:
                    #print(f'player2 - {b}, {player2}')
                    if b in player2:
                        banned = True
                        break
                if banned:
                    continue
                break

        if player1 == player2:
            self.roll()
            return
        hero_name1 = player1.replace(f'{mypath}/', '').replace('.png', '')[6:]
        hero_name2 = player2.replace(f'{mypath}/', '').replace('.png', '')[6:]

        img1 = ImageTk.PhotoImage(file=player1)
        img_label1 = Label(self.root, bg="white", image=img1)
        img_label1.photo = img1
        img_label1.place(x=297 - 58 / 2 - 2, y=296 - 64 / 2 + 20)

        img2 = ImageTk.PhotoImage(file=player2)
        img_label2 = Label(self.root, bg="white", image=img2)
        img_label2.photo = img2
        img_label2.place(x=901 - 58 / 2 - 2, y=296 - 64 / 2 + 20)

        print(f"Player 1 - {hero_name1}\nPlayer 2 - {hero_name2}")

if __name__ == '__main__':
    my_picker = H3Picker()