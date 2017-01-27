import tkinter as tk
import math
import random
import fileinput

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

matplotlib.use("TkAgg")
fenetre = tk.Tk()

eye_frame = tk.Frame(fenetre, borderwidth=2, relief=tk.GROOVE)
eye_frame.grid(row=1, column=1)

eye_info_frame = tk.Frame(fenetre, borderwidth=2, relief=tk.GROOVE)
eye_info_frame.grid(row=2, column=1)

canvas = tk.Canvas(eye_frame, width=400, height=400, background='white')

individuals = []

for line in fileinput.input():
    line = line.split()
    individuals.append(line)

current_index = 0


def refresh():
    global current_index
    individual = individuals[current_index]

    omega = float(individual[0])*200
    rhoc = float(individual[1])*200
    i = float(individual[2])*200
    phi1 = float(individual[3])
    n0 = float(individual[4])
    fitness = float(individual[5])

    #draw eye
    canvas.delete("all")


    cx, cy = 150, 150

    if rhoc == omega/2:
        xy = cx-rhoc, cy-rhoc, cx+rhoc, cy+rhoc
        canvas.create_arc(xy, start=180-phi1*180/math.pi, extent=180+2*phi1*180/math.pi, style=tk.ARC)
        Dx, Dy = cx + math.cos(phi1)*rhoc, cy - math.sin(phi1)*rhoc
        Fx, Fy = Dx-i, Dy
        canvas.create_line(Dx, Dy, Dx-i, Dy)
        Cx, Cy = cx + math.cos(math.pi-phi1)*rhoc, cy - math.sin(math.pi-phi1)*rhoc
        canvas.create_line(Cx, Cy, Cx+i, Dy)
        Ex, Ey = Cx+i, Cy

        # draw lense
        canvas.create_line(Fx, Fy, Ex, Ey, width=int((n0-1.35)/0.2*10), fill='blue')

    elif rhoc > omega/2:
        alpha = math.acos(omega/(2*rhoc))
        H = math.sqrt(rhoc*rhoc - omega*omega/4)
        xy = cx-rhoc, cy-H-rhoc, cx+rhoc, cy-H+rhoc
        canvas.create_arc(xy, start=180+alpha*180/math.pi, extent=180-2*alpha*180/math.pi, style=tk.ARC)
        Bx, By = cx + math.cos(alpha)*rhoc, cy
        Fx, Fy = Bx-i, By
        canvas.create_line(Bx, By, Fx, Fy)
        Ax, Ay = cx - math.cos(alpha)*rhoc, cy
        Ex, Ey = Ax+i, Ay
        canvas.create_line(Ax, Ay, Ex, Ey)

        # draw lense
        canvas.create_line(Fx, Fy, Ex, Ey, width=int((n0-1.35)/0.2*10), fill='blue')

    canvas.pack()

    # update eye info
    for child in eye_info_frame.winfo_children():
        child.destroy()
    text = tk.Text(eye_info_frame)
    text.insert(tk.INSERT, 'Fitness : {}\n'.format(fitness))
    text.insert(tk.INSERT, 'Rayon de courbure : {}\n'.format(rhoc))
    text.insert(tk.INSERT, 'Taille iris : {}\n'.format(i))
    text.insert(tk.INSERT, 'Angle phi1 : {}\n'.format(phi1))
    text.insert(tk.INSERT, 'Indice de réfraction : {}\n'.format(n0))
    text.pack()

    current_index += 1

    if current_index < len(individuals):
        fenetre.after(10, refresh)  # reschedule event in 2 seconds


fenetre.after(200, refresh)
fenetre.mainloop()
