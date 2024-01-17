import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox, ttk
from resitic import Residencia
from icecream import ic

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Resitic")
        self.geometry(f"{400}x{400}")
        
        
        self.residencia = Residencia()
        self.residencia.add_trilha("python")
        self.residencia.add_trilha("dotnet")
        self.residencia.add_trilha("java")
        
        
        # configure grid layout (4x4)
        self.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((1, 2, 3, 4), weight=1)
        
        
        # create buttons
        self.btnAddResidentes = ctk.CTkButton(self, text="Add Residentes", command=self.select_trilha)
        self.btnAddResidentes.grid(row=2, column=2)
        
        self.btnCarregarDados = ctk.CTkButton(self, text="Carregar Dados", command=self.carregar_dados)
        self.btnCarregarDados.grid(row=2, column=3)
        
        self.btnExibirResidentes = ctk.CTkButton(self, text="Exibir Residentes", command=self.exibir_residentes)
        self.btnExibirResidentes.grid(row=3, column=2)
        
    
    def select_trilha(self):
        self.janelaAdd = ctk.CTkToplevel(self)
        self.janelaAdd.title("Adicionar Residentes")
        self.janelaAdd.geometry(f"{550}x{650}")
        
        self.janelaAdd.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
        self.janelaAdd.grid_rowconfigure((1, 2, 3, 4), weight=1)
        
        self.janelaAdd.btnTrilhaPython = ctk.CTkButton(self.janelaAdd, text="Trilha Python", command=lambda: self.add_residentes("python"))
        self.janelaAdd.btnTrilhaPython.grid(row=2, column=2)

        self.janelaAdd.btnTrilhaDotNet = ctk.CTkButton(self.janelaAdd, text="Trilha .NET", command=lambda: self.add_residentes("dotnet"))
        self.janelaAdd.btnTrilhaDotNet.grid(row=2, column=3)

        self.janelaAdd.btnTrilhaJava = ctk.CTkButton(self.janelaAdd, text="Trilha Java", command=lambda: self.add_residentes("java"))
        self.janelaAdd.btnTrilhaJava.grid(row=2, column=4)
        
        
    def add_residentes(self, trilha):
        self.janelaAdd.btnTrilhaPython.destroy()
        self.janelaAdd.btnTrilhaDotNet.destroy()
        self.janelaAdd.btnTrilhaJava.destroy()
        
        self.janelaAdd.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=0, pad=20)
        
        areasFormacao = ["Formação técnica", "Formação técnica graduação em andamento", "Graduação em andamento", "Graduação concluída"]
        areasFormacaoGeral = ["Engenharia", "Computação"]
        experienciaPrevia = ["Sim", "Não"]
        areasEspeficas = []
                
        
        # create variables
        varCPF = ctk.StringVar()
        varAnoNasc = ctk.StringVar()
        varIdade = ctk.StringVar()
        varFormacao = ctk.StringVar()
        varFormacaoGeral = ctk.StringVar()
        varFormacaoEspecifica = ctk.StringVar()
        varAndamentoGraduacao = ctk.StringVar()
        varTempoFormacao = ctk.StringVar()
        varExperienciaPrevia = ctk.StringVar()
        variaveis = {"cpf": varCPF, "anoNasc": varAnoNasc, "idade": varIdade, "formacao": varFormacao, 
                     "formacaoGeral": varFormacaoGeral, "formacaoEspecifica": varFormacaoEspecifica, 
                     "andamentoGraduacao": varAndamentoGraduacao, "tempoFormacao": varTempoFormacao, 
                     "experienciaPrevia": varExperienciaPrevia}
        
        
        # create labels
        self.janelaAdd.lblCPF = ctk.CTkLabel(self.janelaAdd, text="CPF:")
        self.janelaAdd.lblCPF.grid(row=1, column=2)
        
        self.janelaAdd.lblAnoNasc = ctk.CTkLabel(self.janelaAdd, text="Ano de Nascimento:")
        self.janelaAdd.lblAnoNasc.grid(row=2, column=2)
        
        self.janelaAdd.lblIdade = ctk.CTkLabel(self.janelaAdd, text="Idade:")
        self.janelaAdd.lblIdade.grid(row=3, column=2)
        
        self.janelaAdd.lblFormacao = ctk.CTkLabel(self.janelaAdd, text="Formação:")
        self.janelaAdd.lblFormacao.grid(row=4, column=2)
        
        self.janelaAdd.lblFormacaoGeral = ctk.CTkLabel(self.janelaAdd, text="Formação Geral:")
        self.janelaAdd.lblFormacaoGeral.grid(row=5, column=2)
        
        self.janelaAdd.lblFormacaoEspecifica = ctk.CTkLabel(self.janelaAdd, text="Formação Específica:")
        self.janelaAdd.lblFormacaoEspecifica.grid(row=6, column=2)
        
        self.janelaAdd.lblAndamentoGraduacao = ctk.CTkLabel(self.janelaAdd, text="Andamento da Graduação:")
        self.janelaAdd.lblAndamentoGraduacao.grid(row=7, column=2)
        
        self.janelaAdd.lblTempoFormacao = ctk.CTkLabel(self.janelaAdd, text="Tempo de Formação:")
        self.janelaAdd.lblTempoFormacao.grid(row=8, column=2)
        
        self.janelaAdd.lblExperienciaPrevia = ctk.CTkLabel(self.janelaAdd, text="Experiência Prévia:")
        self.janelaAdd.lblExperienciaPrevia.grid(row=9, column=2)
        
        
        # create inputs
        self.janelaAdd.inpCPF = ctk.CTkEntry(self.janelaAdd, textvariable=varCPF)
        self.janelaAdd.inpCPF.grid(row=1, column=3)
        self.janelaAdd.inpCPF.bind("<FocusOut>", lambda event: Interface.verificar_entrada_numero(self.janelaAdd.inpCPF))

        
        self.janelaAdd.inpAnoNasc = ctk.CTkEntry(self.janelaAdd, textvariable=varAnoNasc, validate="key", validatecommand=(self.register(Interface.validar_numero), "%P"))
        self.janelaAdd.inpAnoNasc.grid(row=2, column=3)
        
        self.janelaAdd.inpIdade = ctk.CTkEntry(self.janelaAdd, textvariable=varIdade)
        self.janelaAdd.inpIdade.grid(row=3, column=3)
        
        self.janelaAdd.inpFormacao = ctk.CTkComboBox(self.janelaAdd, values=areasFormacao,
                                    width=200, command=None, variable=varFormacao, state="readonly")
        self.janelaAdd.inpFormacao.grid(row=4, column=3)
        
        self.janelaAdd.inpFormacaoGeral = ctk.CTkComboBox(self.janelaAdd, values=areasFormacaoGeral,
                                    command=self.set_formacao_geral, variable=varFormacaoGeral, state="readonly")
        self.janelaAdd.inpFormacaoGeral.grid(row=5, column=3)
        
        self.janelaAdd.inpFormacaoEspecifica = ctk.CTkComboBox(self.janelaAdd, width=200,
                                                               command=None, values=areasEspeficas, 
                                                               variable=varFormacaoEspecifica, state="readonly")
        self.janelaAdd.inpFormacaoEspecifica.grid(row=6, column=3)
        
        self.janelaAdd.inpAndamentoGraduacao = ctk.CTkEntry(self.janelaAdd, textvariable=varAndamentoGraduacao)
        self.janelaAdd.inpAndamentoGraduacao.grid(row=7, column=3)
        
        self.janelaAdd.inpTempoFormacao = ctk.CTkEntry(self.janelaAdd, textvariable=varTempoFormacao)
        self.janelaAdd.inpTempoFormacao.grid(row=8, column=3)
        
        self.janelaAdd.inpExperienciaPrevia = ctk.CTkComboBox(self.janelaAdd, values=experienciaPrevia,
                                    command=None, variable=varExperienciaPrevia, state="readonly")
        self.janelaAdd.inpExperienciaPrevia.grid(row=9, column=3)
        
        
        # create buttons
        self.janelaAdd.btnAdcionar = ctk.CTkButton(self.janelaAdd, fg_color="green", command=lambda: self.adicionar(trilha, variaveis))
        self.janelaAdd.btnAdcionar.grid(row=11, column=2)
        self.janelaAdd.btnAdcionar.configure(text="Adcionar")
        
        self.janelaAdd.btnVoltar = ctk.CTkButton(self.janelaAdd, fg_color="transparent", text_color="red", command=self.voltar)
        self.janelaAdd.btnVoltar.grid(row=11, column=3)
        self.janelaAdd.btnVoltar.configure(text="Voltar")
    
    
    def voltar(self) -> None:
        self.janelaAdd.destroy()
        
    def adicionar(self, trilha: str, variaveis: dict) -> None:
        formacoes = {"Formação técnica" : 0, "Formação técnica graduação em andamento": 1,
                      "Graduação em andamento": 2, "Graduação concluída": 3}
        
        formacoesGerais = {"Engenharia": 0, "Computação": 1}
        
        id = variaveis['cpf'].get()[:3] + variaveis['anoNasc'].get()[2:]

        formacaoGeral = variaveis['formacaoGeral'].get() or None

        if formacaoGeral:
           formacaoGeral = formacoesGerais[formacaoGeral] 

        formacaoEspecifica = variaveis['formacaoEspecifica'].get() or None
        andamentoGraduacao = variaveis['andamentoGraduacao'].get()

        if andamentoGraduacao:
            andamentoGraduacao = float(andamentoGraduacao)
        else:
            andamentoGraduacao = None

        tempoFormacao = variaveis['tempoFormacao'].get() or None

        if tempoFormacao:
            tempoFormacao = int(tempoFormacao)
        else:
            tempoFormacao = None
        
        residente = {
            'identificador': id,
            'idade': int(variaveis['idade'].get()),
            'formacao': formacoes[variaveis['formacao'].get()],
            'formacaoGeral': formacaoGeral,
            'formacaoEspecifica': formacaoEspecifica,
            'andamentoGraduacao': andamentoGraduacao,
            'tempoFormacao': tempoFormacao,
            'experienciaPrevia': True if variaveis['experienciaPrevia'].get() == "Sim" else False
        }
        
        try:
          self.residencia.add_residente(trilha, residente)
        except ValueError as e:
            print(e)
        
        ic(self.residencia.trilhas[0].residentes)
    
    def carregar_dados(self) -> None:
        file = ctk.filedialog.askopenfilename(title="Carregar Dados", filetypes=[("CSV", "*.csv")])
        
        if file:
            self.residencia.load(file)
        else:
            ctk.CTkMessageBox.showerror("Erro", "Arquivo não selecionado")
            
    
    def exibir_residentes(self) -> None:
        self.janelaResidentes = ctk.CTkToplevel(self)
        self.janelaResidentes.title("Residentes")
        self.janelaResidentes.geometry(f"{800}x{400}")
                
        residentes = self.residencia.get_residentes()
        
        # Criar um Treeview para exibir os dados
        tree = ttk.Treeview(self.janelaResidentes)
        tree["columns"] = tuple(residentes.columns)
        tree["show"] = "headings"

        # Adicionar colunas ao Treeview
        for column in residentes.columns:
            tree.heading(column, text=column)
            tree.column(column, anchor="center", width=100)

        # Adicionar linhas ao Treeview
        for index, row in residentes.iterrows():
            tree.insert("", "end", values=tuple(row))

        # Adicionar Scrollbars
        yscroll = ttk.Scrollbar(self.janelaResidentes, orient="vertical", command=tree.yview)
        yscroll.grid(row=0, column=1, sticky="ns")
        tree.configure(yscrollcommand=yscroll.set)

        xscroll = ttk.Scrollbar(self.janelaResidentes, orient="horizontal", command=tree.xview)
        xscroll.grid(row=1, column=0, sticky="ew")
        tree.configure(xscrollcommand=xscroll.set)

        tree.grid(row=0, column=0, sticky="nsew")

        # Configurar pesos das linhas e colunas para que o Treeview expanda conforme necessário
        self.janelaResidentes.grid_rowconfigure(0, weight=1)
        self.janelaResidentes.grid_columnconfigure(0, weight=1)
    
        
    def set_formacao_geral(self, formacao: str) -> None:
        if formacao == "Computação":
            areasEspeficas = ["Ciência da Computação", "Sistemas de Informação", "Análise e Desenvolvimento de Sistemas", "Engenharia de Software", "Outro"]
        elif formacao == "Engenharia":
            areasEspeficas = ["Engenharia de Computação", "Engenharia Química", "Engenharia de Produção", "Engenharia Mecânica", "Engenharia Elétrica", 
                                             "Engenharia Civil", "Engenharia de Alimentos", "Engenharia Ambiental", "Engenharia Aeroespacial", "Engenharia Nuclear", 
                                             "Engenharia de Materiais", "Outro"]
        else:
            areasEspeficas = []
        
        self.janelaAdd.inpFormacaoEspecifica.configure(values=areasEspeficas)
        
    def validar_texto(entrada):
        return entrada.isalpha()

    def validar_numero(entrada):
        if entrada == "":
            return True
        
        return entrada.isdigit()

    def verificar_entrada_texto(input):
        valor = input.get()
        
        if not Interface.validar_texto(valor):
            messagebox.showerror("Erro de validação", "A entrada deve conter apenas letras.")

    def verificar_entrada_numero(input):
        valor = input.get()
        
        if not Interface.validar_numero(valor):
            messagebox.showerror("Erro de validação", "A entrada deve conter apenas números.")
            input.delete(0, tk.END)
