import tkinter as tk
from tkextrafont import Font

window = tk.Tk()
#font = Font(file="imgs/THSarabunChula-Regular.ttf", family="THSarabun Chula")
#tk.Label(window, text="Hello ภวิต บุญรัตน์", font=font).pack()

tk.Label(window, text="Hello ภวิต บุญรัตน์", font=('Courier', 18)).pack()
#tk.Label(window, text="Hello ภวิต บุญรัตน์", font=('Yu Mincho', 18)).pack()

canvas = tk.Canvas(window, height=500, width=800)
canvas.pack()
window.mainloop()



#import tkinter as tk
#window = tk.Tk()
#greeting = tk.Label(text="Hello, Tkinter ภวิต บุญรัตน์")
#greeting.pack()
#window.mainloop()

