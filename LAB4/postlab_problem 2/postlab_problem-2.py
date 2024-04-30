# # postlab_problem 2
# Explore the Tkinter.filedialog module to get the name of a text file

from tkinter import *
from tkinter import filedialog

def browseFiles():
	filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
	
	label_file_explorer.configure(text="File Opened: "+filename)
		
root = Tk()
root.title("File Explorer")

root.geometry("800x450")
root.config(background = "white")

label_file_explorer = Label(root, 
							text = "File Explorer using Tkinter",
							width = 100, height = 4, 
							fg = "black")

btn_explore = Button(root, 
						text = "Browse Files",
						command = browseFiles) 

btn_exit = Button(root, 
					text = "Exit",
					command = exit) 

label_file_explorer.pack(pady=20)
btn_explore.pack(pady=10)
btn_exit.pack(pady=10)

root.mainloop()
