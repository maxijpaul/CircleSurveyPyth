import pygame
import time
from time import sleep
import csv
import math
import tkinter as tk
import glob
import pandas as pd

class App:
    def __init__(self):
        self.HEIGHT = 500
        self.WIDTH = 500    
        root = tk.Tk()
        root.width = self.WIDTH
        root.height = self.HEIGHT
        self.dialogroot = root
        self.strDialogResult = ""    
        self.canvas = tk.Canvas(root, height=self.HEIGHT, width=self.WIDTH)
        self.canvas.pack()    
        frame = tk.Frame(root, bg='#ffffff')
        frame.place(relx=0.5, rely=0.27, relwidth=0.7, relheight=0.5, anchor='n')  
        # Here is the button call to the InputBox() function
        buttonInputBox = tk.Button(frame, text="""  Dear user,
        welcome to CirlceSurvey by Max Paul.


        If you click on this text-screen,
        a window will pop up.
        There, please insert your first Name.
         

        Close this window afterwards,
        in order to start the game.""", bg='#ffffff', font=80, 
        command=lambda: self.InputBox())    
        buttonInputBox.place(relx=0.05, rely=0.1, relwidth=0.95, relheight=0.8)    
        root.mainloop()

    def InputBox(self):        
        dialog = tk.Toplevel(self.dialogroot)
        dialog.width = 500
        dialog.height = 500

        frame = tk.Frame(dialog,  bg='#ffffff', bd=5)
        frame.place(relwidth=1, relheight=1)

        entry = tk.Entry(frame, font=40)
        entry.place(relwidth=0.65, rely=0.02, relheight=0.20)
        entry.focus_set()

        submit = tk.Button(frame, text='OK', font=16, command=lambda: self.DialogResult(entry.get()))
        submit.place(relx=0.7, rely=0.02, relheight=0.2, relwidth=0.3)

        root_name = self.dialogroot.winfo_pathname(self.dialogroot.winfo_id())
        dialog_name = dialog.winfo_pathname(dialog.winfo_id())

        # These two lines show a modal dialog
        self.dialogroot.tk.eval('tk::PlaceWindow {0} widget {1}'.format(dialog_name, root_name))
        self.dialogroot.mainloop()

        #This line destroys the modal dialog after the user exits/accepts it
        dialog.destroy()

        name = str(self.strDialogResult)
        with open('nametex.txt', 'w+') as fh:
            fh.write(name)

    def DialogResult(self, result):
        self.strDialogResult = result
        #This line quits from the MODAL STATE but doesn't close or destroy the modal dialog
        self.dialogroot.quit()


# Launch ...
if __name__ == '__main__':
    app = App()

pygame.init()

gameDisplay = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

bg = pygame.image.load("/Users/maximilianpl/Downloads/wetransfer-13a45a/50p.png")

items = [".png"," (5).png", " (6).png", " (7).png", " (8).png"]

def display(z, e):
        gameDisplay.blit(bg, (z, e))

for item in items:

    textb = pygame.image.load("/Users/maximilianpl/Downloads/wetransfer-e6b811/Untitled" + item)

    x, y = 200, 200

    a, b = 250, 250

    u, v = 250, 250

    z, e = 0, 0

    def textbox(x, y):
        gameDisplay.blit(textb, (x, y))

    done = False

    start_time = pygame.time.get_ticks()

    dragging = False

    while not done:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
            elif event.type == pygame.MOUSEMOTION:
                firstrect = pygame.Rect(u, v, 0.001, 0.001)
                slow_radius = 100
                superslow_radius = 195
                firstcorners = [firstrect.bottomleft, firstrect.bottomright, firstrect.topleft, firstrect.topright]
                distone = [math.sqrt((p[0] - a) ** 2 + (p[1] - b) ** 2) for p in firstcorners]
                p_norm = [i for i, d in enumerate(distone) if d < slow_radius]
                p_slow = [i for i, d in enumerate(distone) if slow_radius < d < superslow_radius]
                if dragging:
                    if any(p_norm):
                        x += 1*(event.rel[0])
                        y += 1*(event.rel[1])
                        u += 1*(event.rel[0])
                        v += 1*(event.rel[1])
                    elif any(p_slow):
                        x += 1*(event.rel[0])
                        y += 1*(event.rel[1])
                        u += 1*(event.rel[0])
                        v += 1*(event.rel[1])
                    else:
                        x += 1*(event.rel[0])
                        y += 1*(event.rel[1])
                        u += 1*(event.rel[0])
                        v +=  1*(event.rel[1])

        secondrect = pygame.Rect(u, v, 0.001, 0.001)
        radius = 200
        secondcorners = [secondrect.bottomleft, secondrect.bottomright, secondrect.topleft, secondrect.topright]
        dist = [math.sqrt((p[0] - a) ** 2 + (p[1] - b) ** 2) for p in secondcorners]
        p_out = [i for i, d in enumerate(dist) if d > radius]

        if any(p_out):
            position = str((x,y))
            end_time = pygame.time.get_ticks()
            time = str((end_time - start_time) )
            with open("data" + item +".csv", "w", newline= "") as datalist:
                thewriter = csv.writer(datalist)
                thewriter.writerow(["Item","position", "time"])
                thewriter.writerow([1, position, time])
            break

        display(z, e)
        textbox(x, y)
        pygame.display.flip()
    sleep(0.4)

all_filenames = ["data (1).png.csv", "data (2).png.csv", "data (3).png.csv", "data (4).png.csv", "data (5).png.csv", "data (6).png.csv", "data (7).png.csv", "data (8).png.csv"]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
name = open('nametex.txt', 'r').read()
combined_csv.to_csv( "fileof" + name + ".csv", index=False, encoding='utf-8-sig')

pygame.quit()
quit()