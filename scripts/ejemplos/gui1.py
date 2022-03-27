from tkinter import Tk, Label, RIDGE

root = Tk()

courses = ['C','C++','Python','Java','Unix','DevOps'] 
r = ['course'] 

for c in courses:
    Label(root,text=c, width=15).grid(column=0)
    Label(root,text=r, relief=RIDGE, width=15).grid(column=1)


root.mainloop()
#https://www.educba.com/tkinter-grid/
# https://www.pythontutorial.net/tkinter/tkinter-grid/
# https://www.youtube.com/watch?v=y69rqjEfwYI&list=PLqlQ2-9ypflQQEepQJvGQ6RJ8llnzk6Kj&index=4&t=178s