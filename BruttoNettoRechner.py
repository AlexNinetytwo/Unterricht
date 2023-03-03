from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import ctypes
user32 = ctypes.windll.user32
SCRENNSIZE = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

winHeight = 200
winWidth = 400

xMid = (SCRENNSIZE[0] // 2) - (winWidth // 2)
yMid = (SCRENNSIZE[1] // 2) - (winHeight // 2)



def calcNetto():

  mwst, amount = getEntries()

  netto = round(amount / (100+mwst) * 100, 2)
  returnResult(netto)

def calcBrutto():

  mwst, amount = getEntries()

  brutto = round(amount / 100 * (100+mwst), 2)
  returnResult(brutto)

def getEntries():

  mwst = 0
  amount = 0

  try:
    mwst = int(mwstEntry.get())
    amount = float(amountEntry.get())

  except:
    messagebox.showerror('Brutto / Netto - Rechner', 'Ungültige Eingabe!')

  return mwst, amount
 
def returnResult(amount):
  outputEntry.configure(state="normal")
  outputEntry.delete(0, END)
  outputEntry.insert(0, str(amount))
  outputEntry.configure(state="disable")

win = Tk() # Fensterobjekt der Klasse Tk
win.wm_geometry(f"{winWidth}x{winHeight}+{xMid}+{yMid}")
win.title("Brutto / Netto - Rechner")
win.resizable(False,False)

frame = Frame(win)
frame.pack(padx=20,pady=20)


mwst = Frame(frame)
mwst.grid(row=1,column=1)

mwstLabel = ttk.Label(frame, text="MwSt:")
mwstLabel.grid(row=1,column=0)

mwstEntry = Entry(mwst, width=5)
mwstEntry.grid(row=0,column=0)
mwstEntry.insert(0,"19")

percentSign = ttk.Label(mwst, text="%")
percentSign.grid(row=0,column=1)


bruttoBtn = ttk.Button(frame, text="Berechne Brutto", command=calcBrutto)
bruttoBtn.grid(row=2,column=0,padx=10,pady=10)

nettoBtn = ttk.Button(frame, text="Berechne Netto", command=calcNetto)
nettoBtn.grid(row=2,column=1,padx=10,pady=10)

amount = Frame(frame)
amount.grid(row=0,column=3,padx=10,pady=10)

amountLabel = ttk.Label(amount, text="Betrag")
amountLabel.grid(row=0,column=0)

amountEntry = Entry(amount, width=10)
amountEntry.grid(row=1,column=0)

output = Frame(frame)
output.grid(row=2,column=3,padx=10,pady=10)

outputLabel = ttk.Label(output, text="Ausgabe")
outputLabel.grid(row=0,column=0)

outputEntry = Entry(output, width=10)
outputEntry.grid(row=1,column=0)
outputEntry.configure(state="disable")







win.mainloop()