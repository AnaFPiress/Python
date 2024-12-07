from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculadora")
# Frame para os botões
frm = ttk.Frame(root, padding=10)
frm.grid()

# variável para o display
display = StringVar()

# Campo de entrada do display
ttk.Entry(frm, textvariable= display, justify='right', font=('Arial', 16)).grid(column=0, row=0, columnspan=4,sticky='we', padx=5, pady=5)


# Botões de números
ttk.Button(frm, text="7", command=lambda: display.set(display.get() + "7")).grid(column=0, row=1)
ttk.Button(frm, text="8", command=lambda: display.set(display.get() + "8")).grid(column=1, row=1)
ttk.Button(frm, text="9", command=lambda: display.set(display.get() + "9")).grid(column=2, row=1)

ttk.Button(frm, text="4", command=lambda: display.set(display.get() + "4")).grid(column=0, row=2)
ttk.Button(frm, text="5", command=lambda: display.set(display.get() + "5")).grid(column=1, row=2)
ttk.Button(frm, text="6", command=lambda: display.set(display.get() + "6")).grid(column=2, row=2)

ttk.Button(frm, text="1", command=lambda: display.set(display.get() + "1")).grid(column=0, row=3)
ttk.Button(frm, text="2", command=lambda: display.set(display.get() + "2")).grid(column=1, row=3)
ttk.Button(frm, text="3", command=lambda: display.set(display.get() + "3")).grid(column=2, row=3)

ttk.Button(frm, text="0", command=lambda: display.set(display.get() + "0")).grid(column=1, row=4)

# Botões para as operações
ttk.Button(frm, text='+', command=lambda: display.set(display.get() + '+')).grid(column=3, row=1)
ttk.Button(frm, text='-', command=lambda: display.set(display.get() + '-')).grid(column=3, row=2)
ttk.Button(frm, text='*', command=lambda: display.set(display.get() + '*')).grid(column=3, row=3)
ttk.Button(frm, text='/', command=lambda: display.set(display.get() + '/')).grid(column=3, row=4)

# Botão de igual
ttk.Button(frm, text='=', command=lambda: display.set(str(eval(display.get()))if display.get() else "")).grid(column=2, row=4, sticky="we")

# Botão de limpar
ttk.Button(frm, text="C", command=lambda: display.set("")).grid(column=0, row=4, sticky="we")

# Inicia o loop principal
root.mainloop()