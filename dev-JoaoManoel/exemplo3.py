import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title('Exemplo 3')
    root.geometry('300x100')

    frame = tk.Frame(root)
    frame.pack()

    frame.grid_rowconfigure([1, 2, 3], weight=1)
    frame.grid_columnconfigure([1, 2, 3, 4, 5], weight=1)

    label = tk.Label(frame)
    label.grid(row=1, column=2, sticky='nsew')

    entry = tk.Entry(frame)
    entry.grid(row=1, column=4, sticky='nsew')

    button1 = tk.Button(frame, text='Passar texto', command=lambda: label.config(text=entry.get()))
    button1.grid(row=2, column=2, sticky='nsew')

    button2 = tk.Button(frame, text='Limpar', command=lambda: entry.delete(0, 'end'))
    button2.grid(row=2, column=4, sticky='nsew')

    button3 = tk.Button(frame, text='Sair', command=root.quit, bg='#ff0000', fg='#ffff00')
    button3.grid(row=3, column=2, columnspan=3, sticky='nsew')

    root.mainloop()

if __name__ == '__main__':
    main()