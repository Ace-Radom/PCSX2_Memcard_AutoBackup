import tkinter
from tkinter import messagebox

root = tkinter.Tk()
# gui root

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello Runoob")

root.title( "PCSX2 Memcard Manager Setup-helper" )
root.geometry( '500x115' )
root.resizable( width = False , height = False )

frm_top = tkinter.Frame( root )
frm_bottom = tkinter.Frame( root )

PCSX2_Memcard_Path_Label = tkinter.Label( frm_top , text = "PCSX2 Memcard Save Folder" )
PCSX2_Memcard_Path_Text = tkinter.Text( frm_top , width = 60 , height = 1 )
PCSX2_Memcard_Path_Label.pack()
PCSX2_Memcard_Path_Text.pack()

P2MM_Backup_Path_Label = tkinter.Label( frm_bottom , text = "PCSX2 Memcard Manager Backup Folder" )
P2MM_Backup_Path_Text = tkinter.Text( frm_bottom , width = 60 , height = 1 )
P2MM_Backup_Path_Label.pack()
P2MM_Backup_Path_Text.pack()

setup_buttom = tkinter.Button( root , text = "Setup" , command = helloCallBack )

frm_top.pack()
frm_bottom.pack()

setup_buttom.pack( side = tkinter.BOTTOM )

root.mainloop()
# get in main loop function (show gui window)