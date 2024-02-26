from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from estacaometereologica.search import Search
from estacaometereologica.plot import get_plot
from tkinter import messagebox, ttk
import tkinter as tk
import matplotlib
import threading
import requests

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Estação Metereológica')
        self.resizable(False, False)
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

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

        self.frameEstacao.lblEstacao = tk.Label(self, text='Escollha a estação: ')
        self.frameEstacao.lblEstacao.grid(row=4, column=1, padx=5, pady=5)

        self.frameEstacao.inpEstacoes = ttk.Combobox(self, values=[], 
                                                     state='readonly', textvariable=self.estacaoSelecionada)
        self.frameEstacao.inpEstacoes.grid(row=4, column=2, padx=5, pady=5)

        self.frameEstacao.btnMostarGrafico = tk.Button(self, text='Mostar grafico', command=self.mostrar_grafico)
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
        self.frameEstacao.inpEstacoes['values'] = ['']
        self.estacaoSelecionada.set('')

        loading_popup = tk.Toplevel(self)
        loading_popup.title("Downloading...")
        loading_popup.protocol("WM_DELETE_WINDOW", self.on_closing_loading)

        label = tk.Label(loading_popup, text="Baixando dados...")
        label.pack()
        
        threading.Thread(target=self.download, args=(loading_popup,)).start()
    
    def download(self, loading_popup):
        if self.anoSelecionado.get() == '':
            self.frameEstacao.inpEstacoes['values'] = ['']
            self.estacaoSelecionada.set('')
        else:
            try:
                self.pesquisa.apagar_dados()
            except Exception as e:
                print(f'Erro: {e}')

            self.pesquisa.carregar_estacoes(self.anos[self.anoSelecionado.get()])
            
            self.estacoes = self.pesquisa.get_estacoes()
            self.estacoes = {k: v for k, v in sorted(self.estacoes.items(), key=lambda item: item[0])}
            
            self.frameEstacao.inpEstacoes['values'] = list(self.estacoes.keys())
            
        loading_popup.destroy()
    
    def mostrar_grafico(self):
        if self.estacaoSelecionada.get() == '':
            messagebox.showerror('Erro', 'Selecione uma estação')
            return

        self.janelaGraficos = tk.Toplevel(self)
        self.janelaGraficos.title('Gráficos')
        
        self.janelaGraficos.protocol("WM_DELETE_WINDOW", self.on_closing_janelaGraficos)
        
        caminho = self.estacoes[self.estacaoSelecionada.get()]
        
        try:
            self.fig = get_plot(caminho)
            
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.janelaGraficos)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        except Exception as e:
            print(f'Erro: {e}')
    
    def on_closing(self):
        try:
            self.pesquisa.apagar_dados()
        except Exception as e:
            print(f'Erro: {e}')
        
        self.destroy()

    def on_closing_janelaGraficos(self):
        matplotlib.pyplot.close('all')
        self.canvas.get_tk_widget().destroy()
        self.janelaGraficos.destroy()

    def on_closing_loading(self):
        pass