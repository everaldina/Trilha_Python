import tkinter as tk

root = tk.Tk()

root.title("Teste TKINTER")

frame = tk.Frame(root, width=300, height=200)


# criando widgets
lbl_mutavel = tk.Label(frame, text="Texto mutável")
input_text = tk.Entry(frame)
btn_set = tk.Button(frame, text="Setar label", command=lambda: lbl_mutavel.config(text=input_text.get()))
btn_clear = tk.Button(frame, text="Limpar entrada", command=input_text.delete(0, tk.END))
btn_exit = tk.Button(root, text="Sair", command=root.quit)


# posicionando widgets
lbl_mutavel.grid(column=0, row=0, pady=4)
input_text.grid(column=1, row=0, pady=4)
btn_set.grid(column=0, row=1)
btn_clear.grid(column=1, row=1)

frame.pack()
btn_exit.pack(anchor="n")

root.mainloop()



