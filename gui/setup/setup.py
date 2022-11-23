import os
import tkinter
from tkinter import messagebox

from ini import rINI, wINI

config_file = '../config/backup.ini'

root = tkinter.Tk()
# gui root

def setup_config():
   memcard_folder_end = PCSX2_Memcard_Path_Text.get( 1.0 , tkinter.END ).strip().replace("\n","").encode()
   backup_folder_end = P2MM_Backup_Path_Text.get( 1.0 , tkinter.END ).strip().replace("\n","").encode()
   # get memcard folder path and backup folder path from gui-text

   if memcard_folder_end and backup_folder_end:
      if not os.path.exists( memcard_folder_end ):
         messagebox.showerror( title = "Setup ERROR" , message = "PCSX2 Memcard Save Folder doesn't exist" )
         return
      # PCSX2 Memcard Save Folder doesn't exist, stop

      if not os.path.isdir( backup_folder_end ):
         messagebox.showerror( title = "Setup ERROR" , message = "PCSX2 Memcard Manager Backup Folder doesn't exist" )
         return
      # PCSX2 Memcard Manager Backup Folder doesn't exist, stop

      memcard_folder_str = memcard_folder_end.decode( "utf-8" )
      backup_folder_str = backup_folder_end.decode( "utf-8" )
      #print( memcard_folder_str )
      #print( backup_folder_str )
      wINI( config_file , 'PCSX2' , 'memcard_folder' , memcard_folder_str)
      wINI( config_file , 'PCSX2_Memcard_Manager' , 'backup_folder' , backup_folder_str )
      messagebox.showinfo( title = "Setup INFO" , message = "Configs have been written to config-files" )

   else:
      messagebox.showerror( title = "Setup ERROR" , message = "PCSX2 Memcard Save Folder or PCSX2 Memcard Manager Backup Folder Path not set" )

root.title( "PCSX2 Memcard Manager Setup Helper" ) # set window title
root.geometry( '500x115' ) # set window size
root.resizable( width = False , height = False ) # set window as not resizable
root.iconbitmap( 'setup.ico' )

frm_top = tkinter.Frame( root ) 
# top frame
frm_bottom = tkinter.Frame( root )
# bottom frame

PCSX2_Memcard_Path_Label = tkinter.Label( frm_top , text = "PCSX2 Memcard Save Folder" )
PCSX2_Memcard_Path_Text = tkinter.Text( frm_top , width = 60 , height = 1 )
PCSX2_Memcard_Path_Label.pack()
PCSX2_Memcard_Path_Text.pack()
# add PCSX2 Memcard Path Label and Text to top frame and pack them

P2MM_Backup_Path_Label = tkinter.Label( frm_bottom , text = "PCSX2 Memcard Manager Backup Folder" )
P2MM_Backup_Path_Text = tkinter.Text( frm_bottom , width = 60 , height = 1 )
P2MM_Backup_Path_Label.pack()
P2MM_Backup_Path_Text.pack()
# add P2MM Backup Path Label and Text to bottom frame and pack them

setup_button = tkinter.Button( root , text = "Setup" , bg = "lightblue" , command = setup_config )
# add setup button 

frm_top.pack()
frm_bottom.pack()
# pack top and bottom frame

setup_button.pack( side = tkinter.BOTTOM )
# pack setup button at the bottom of the window (root)

memcard_folder = rINI( config_file , 'PCSX2' , 'memcard_folder' )
if memcard_folder != "":
   PCSX2_Memcard_Path_Text.insert( 1.0 , memcard_folder )
# check / insert memcard_folder node

backup_folder = rINI( config_file , 'PCSX2_Memcard_Manager' , 'backup_folder' )
if backup_folder != "":
   P2MM_Backup_Path_Text.insert( 1.0 , backup_folder )
# check / insert backup_folder node

root.mainloop()
# get in main loop function (show gui window)
