from tkinter import Tk, Label, Entry, Button, W, E

# root window
root = Tk()
root.geometry("300x110")
root.title('Login')
root.resizable(0, 0) # se evita que se pueda cambiar el tamaño de la ventana

# se configura el grid, cada columna con un peso distinto para que midan en proporcion, se definen 2 columnas
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
# en total seria 4, es decir, el de peso de 1 tendria un 1/4 y el de 3 tendria 3/4 del espacio


# username
username_label = Label(root, text="Usuario:")
username_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

username_entry = Entry(root)
username_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)

# password
password_label = Label(root, text="Contraseña:")
password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

password_entry = Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

# login button
login_button = Button(root, text="Iniciar sesión")
login_button.grid(column=1, row=3, sticky=E, padx=5, pady=5)

root.mainloop()


# https://www.youtube.com/watch?v=y69rqjEfwYI&list=PLqlQ2-9ypflQQEepQJvGQ6RJ8llnzk6Kj&index=4&t=178s