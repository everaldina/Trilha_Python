import tkinter as tk
from tkinter import messagebox, ttk
from estacaometereologica.search import Search

class Interface(tk.Tk):
    def __init__(self, anos = None):
        super().__init__()

        self.title('Estação Metereológica')
        self.geometry('400x200')

        self.anoSelecionado = tk.StringVar()
        self.estacaoSelecionada = tk.StringVar()

        self.grid_columnconfigure([1,2], weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frameEstacao = tk.Frame(self)
        self.frameEstacao.grid(row=1, column=1, sticky='nsew')

        self.frameGrafico = tk.Frame(self)
        self.frameGrafico.grid(row=1, column=2, sticky='nsew')
        
        self.frameEstacao.grid_rowconfigure([1,2,3,4,5,6,7,8], weight=1)
        self.frameEstacao.grid_columnconfigure([1,2,3,4,5], weight=1)

        self.frameEstacao.lblAnos = tk.Label(self, text='Escollha a estação: ')
        self.frameEstacao.lblAnos.grid(row=0, column=1, padx=5, pady=5)

        self.frameEstacao.inpAnos = ttk.Combobox(self, values=[],
                                                  state='readonly', textvariable=self.anoSelecionado)
        self.frameEstacao.inpAnos.bind('<<ComboboxSelected>>', self.seleciona_ano)
        self.frameEstacao.inpAnos.grid(row=1, column=1, padx=5, pady=5)

        self.frameEstacao.btnCarregar = tk.Button(self, text='Carregar', command=self.carregar)
        self.frameEstacao.btnCarregar.grid(row=2, column=1, padx=5, pady=5)

        self.frameEstacao.lblEstacao = tk.Label(self, text='Escollha o ano: ')
        self.frameEstacao.lblEstacao.grid(row=3, column=1, padx=5, pady=5)

        self.frameEstacao.inpEstacoes = ttk.Combobox(self, values=[], 
                                                     state='readonly', textvariable=self.estacaoSelecionada)
        self.frameEstacao.inpEstacoes.bind('<<ComboboxSelected>>', self.seleciona_estacao)
        self.frameEstacao.inpEstacoes.grid(row=4, column=1, padx=5, pady=5)

        self.frameEstacao.btnMostarGrafico = tk.Button(self, text='Mostar grafico', command=None)
        self.frameEstacao.btnMostarGrafico.grid(row=5, column=1, padx=5, pady=5)

        self.carregar_anos()

    def carregar_anos(self):
        try:
            self.pesquisa = Search()
            self.anos = self.pesquisa.get_anos()
            self.anosList = list(self.anos.keys())

            self.frameEstacao.inpAnos['values'] = self.anosList
        except Exception as e:
            messagebox.showerror('Erro', f'Erro de conexão')

    def seleciona_ano(self, event):
        print('Ano selecionado:')
        print(self.anoSelecionado.get())

    def seleciona_estacao(self):
        pass

    def carregar(self):
        print(f"link: {self.anos[self.anoSelecionado.get()]}")