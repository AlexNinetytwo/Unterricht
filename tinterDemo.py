from tkinter import *

def ausgabe():
    print("Button geklickt!")

win = Tk() # Fensterobjekt der Klasse Tk
win.wm_geometry("400x150")
win.title("Tkinter Demo")

label1 = Label(win, text="Hello Welt") # Label Objekt erzeugt
label1.pack(pady=20) # Positionieren des Labels mit 20 Pixel vertikaler Abstand

button1 = Button(win, text="Klick mich!", command=ausgabe)
button1.pack(pady=0)

win.mainloop()
