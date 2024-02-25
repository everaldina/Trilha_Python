import tkinter as tk
from tkinter import messagebox, ttk
from estacaometereologica.search import Search
import requests
import webbrowser

class Interface(tk.Tk):
    def __init__(self, anos = None):
        super().__init__()

        self.title('Estação Metereológica')
        self.resizable(False, False)

        self.anoSelecionado = tk.StringVar()
        self.estacaoSelecionada = tk.StringVar()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frameEstacao = tk.Frame(self)
        self.frameEstacao.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
        
        self.frameEstacao.grid_rowconfigure([1,2,3,4,5], weight=1)
        self.frameEstacao.grid_columnconfigure([1,2], weight=1)

        self.frameEstacao.lblAnos = tk.Label(self, text='Escollha o ano: ')
        self.frameEstacao.lblAnos.grid(row=2, column=1)

        self.frameEstacao.inpAnos = ttk.Combobox(self, values=[],
                                                  state='readonly', textvariable=self.anoSelecionado)
        self.frameEstacao.inpAnos.bind('<<ComboboxSelected>>', self.seleciona_ano)
        self.frameEstacao.inpAnos.grid(row=2, column=2, padx=5, pady=5)

        self.frameEstacao.btnCarregar = tk.Button(self, text='Carregar', command=self.carregar)
        self.frameEstacao.btnCarregar.grid(row=3, column=2, padx=5, pady=5)

        self.frameEstacao.lblEstacao = tk.Label(self, text='Escollha a estação: ')
        self.frameEstacao.lblEstacao.grid(row=4, column=1, padx=5, pady=5)

        self.frameEstacao.inpEstacoes = ttk.Combobox(self, values=[], 
                                                     state='readonly', textvariable=self.estacaoSelecionada)
        self.frameEstacao.inpEstacoes.bind('<<ComboboxSelected>>', self.seleciona_estacao)
        self.frameEstacao.inpEstacoes.grid(row=4, column=2, padx=5, pady=5)

        self.frameEstacao.btnMostarGrafico = tk.Button(self, text='Mostar grafico', command=None)
        self.frameEstacao.btnMostarGrafico.grid(row=5, column=2, padx=5, pady=5)

        self.carregar_anos()

    def carregar_anos(self):
        try:
            self.pesquisa = Search()
            self.anos = self.pesquisa.get_anos()
            self.anosList = list(self.anos.keys())
            self.anosList.insert(0, '')

            self.frameEstacao.inpAnos['values'] = self.anosList
        except ConnectionError:
            if messagebox.askretrycancel('Erro', 'Não foi possível conectar ao servidor'):
                self.carregar_anos()
            else:
                self.destroy()
        except requests.exceptions.ConnectionError:
            if messagebox.askretrycancel('Erro', 'Não foi possível conectar ao servidor'):
                self.carregar_anos()
            else:
                self.destroy()
        except Exception as e:
            messagebox.showerror('Erro', e)

    def seleciona_ano(self, event):
        if self.anoSelecionado.get() == '':
            self.frameEstacao.inpEstacoes['values'] = ['']
            
        else:
            self.pesquisa.carregar_estacoes(self.anos[self.anoSelecionado.get()])
            
            self.estacoes = self.pesquisa.get_estacoes()
            
            self.frameEstacao.inpEstacoes['values'] = list(self.estacoes.keys())
    
    def seleciona_estacao(self, event):
        pass
    
    def carregar(self):
        if self.anoSelecionado.get() == '':
            messagebox.showwarning('Aviso', 'Selecione um ano')
        else:
            popup = tk.Toplevel(self)
            popup.title(f"Link ano {self.anoSelecionado.get()}")
            
            label = tk.Label(popup, text=f"{self.anos[self.anoSelecionado.get()]}", fg="blue", cursor="hand2")
            label.pack(padx=20, pady=20)
            label.bind("<Button-1>", lambda e: webbrowser.open_new(self.anos[self.anoSelecionado.get()]))