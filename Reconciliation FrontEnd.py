import openpyxl
import tkinter
from tkinter.filedialog import askopenfilename

#Sets Tkinter test
root = tkinter.Tk()
#Removes root window to allow user access to file input
root.withdraw()

#User inputs for location of files and whether Sales or Stock for reconciliation
BOReport = askopenfilename(parent=root,initialdir="/",title='Please select a BO Report')
INCReport = askopenfilename(parent=root,initialdir="/",title='Please select an INC Report')
SalesOrStock = str.lower(input('Sales or Stock: '))

    if SalesOrStock != "sales" or SalesOrStock != "stock":
        SalesOrStock = str.lower(input('Was that Sales or Stock?: '))


    
