from tkinter import * # import all widgets from module tkinter

from generator import generate_password

def put_password():
    password = generate_password(long.get())
    clear_password()
    text_password.insert(END,password)

def clear_password():
    text_password.delete("1.0",END)

def build_gui():
    """Function to build all widgets and position

    Returns:
        Tk: Return the main window
    """    
    root = Tk()
    root.resizable(0,0)
    root.title("Password Generator - MK85")
    root["background"] = "#dddddd"
    
    btn_width = 10
    
    root.columnconfigure(3)
    root.rowconfigure(4)
    
    ## Config the font size and the font
    Label(root, text="Password Generator", font =("Hack", 20)).grid(column=0, row=0, ipadx=4, ipady=4, padx=16, pady=16, columnspan=3)
    
    Label(root, text="Long").grid(row=1, column=0,  sticky=W, ipadx=4, padx=16)
    
    global long
    long = IntVar()
    long.set(4)
    input_long = Entry(root, borderwidth=2, bg="#ccd466", textvariable=long)
    input_long.grid(row=1, column=1,sticky=W)
    input_long.focus() # al iniciar la app que este activo
    # input_long.insert(END,"4") # coloca el numero 4 en el entry
    
    btn_generate = Button(root,text="Generate", width=btn_width, command=put_password)
    btn_generate.grid(row=1, column=2, padx=16, sticky=W)
    
    global text_password
    text_password = Text(root, height=3, width=56, borderwidth=2)
    text_password.grid(row=2, column=0, columnspan=3, sticky=W, ipady=4, padx=16, pady=16)
    # text_password["state"]=DISABLED
    
    btn_clear = Button(root, text="Clear", width=btn_width, command=clear_password)
    btn_clear.grid(row=3, column=0, padx=16, pady=16, sticky=E)
    
    btn_copy = Button(root, text="Copy", width=btn_width)
    btn_copy.grid(row=3, column=2,padx=16, pady=16, sticky=W)
    
    return root
    

def init_app():
    """Function main to invoke the build gui
    """    
    # print(generate_password(20) )
    build_gui().mainloop()
    

if __name__ == "__main__":
    init_app()
    
# https://realpython.com/python-gui-tkinter/