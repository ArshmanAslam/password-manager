from tkinter import *


screen = Tk()


image= PhotoImage(file='test.png')

screen.config(pady=80,padx=80)
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image=image)
canvas.grid(column=2,row=2)



screen.mainloop()

