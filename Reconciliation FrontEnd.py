from tkinter import*
from tkinter.filedialog import askopenfilename

#Sets Tkinter
root = Tk()

def selectFiles():
    root.withdraw
    #User inputs for location of files and whether Sales or Stock for reconciliation
    BOReport = askopenfilename(parent=root,initialdir="/",title='Please select a BO Report')
    INCReport = askopenfilename(parent=root,initialdir="/",title='Please select an INC Report')

Label (root, text = "Sales or Stock").grid(row=0, sticky=W)
Sales = IntVar()
Checkbutton(root, text="Sales", variable = Sales).grid(row=1, sticky=W)
Stock = IntVar()
Checkbutton(root, text="Stock", variable = Stock).grid(row=2, sticky=W)
Button(root, text = 'Quit', command=root.quit).grid(row=4, sticky=W, pady=4)
Button(root, text = 'Next', command = selectFiles).grid(row=3, sticky=W, pady=4)
mainloop()





    
