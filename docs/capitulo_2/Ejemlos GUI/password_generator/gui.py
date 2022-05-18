from tkinter import *
from tkinter import messagebox # import all widgets from module tkinter

from generator import generate_password

def put_password():
    long_gui = long.get()
    if not long_gui.isnumeric():
        messagebox.showerror("Error", "Solo se pueden introducir números")
        return

    password = generate_password(int(long_gui))
    clear_password()
    text_password.insert(END,password)

def clear_password():
    text_password.delete("1.0",END)

def send_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(text_password.get("1.0",END))
    root.update()

def build_gui():
    """Function to build all widgets and position

    Returns:
        Tk: Return the main window
    """
    global root
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
    long = StringVar() # Es el objeto que maneja el contenido dentro del widget, elijo String porque asi manejare el error de dato
    long.set(8) # le coloco el numero 8 cuando inicia la aplicación
    input_long = Entry(root, borderwidth=2, bg="#ccd466", textvariable=long)
    input_long.grid(row=1, column=1,sticky=W)
    input_long.focus() # al iniciar la app que este activo

    btn_generate = Button(root,text="Generate", width=btn_width, command=put_password)
    btn_generate.grid(row=1, column=2, padx=16, sticky=W)

    global text_password
    text_password = Text(root, height=3, width=56, borderwidth=2)
    text_password.grid(row=2, column=0, columnspan=3, sticky=W, ipady=4, padx=16, pady=16)
    # text_password["state"]=DISABLED

    btn_clear = Button(root, text="Clear", width=btn_width, command=clear_password)
    btn_clear.grid(row=3, column=0, padx=16, pady=16, sticky=E)

    btn_copy = Button(root, text="Copy", width=btn_width, command=send_to_clipboard)
    btn_copy.grid(row=3, column=2,padx=16, pady=16, sticky=W)

    return root


def init_app():
    """Function main to invoke the build gui
    """
    build_gui().mainloop()


if __name__ == "__main__":
    """To the the app
    """
    init_app()
