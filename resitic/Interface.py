import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Resitic")
        self.geometry(f"{400}x{400}")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((1, 2, 3, 4), weight=1)
                
        # create buttons
        self.btnAddResidentes = ctk.CTkButton(self, text="Add Residentes", command=self.select_trilha)
        self.btnAddResidentes.grid(row=2, column=2)
        
        self.btnCarregarDados = ctk.CTkButton(self, text="Carregar Dados", command=self.carregar_dados)
        self.btnCarregarDados.grid(row=2, column=3)
        
    
    def select_trilha(self):
        self.janelaAdd = ctk.CTkToplevel(self)
        self.janelaAdd.title("Adicionar Residentes")
        self.janelaAdd.geometry(f"{600}x{700}")
        
        self.janelaAdd.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.janelaAdd.grid_rowconfigure((1, 2, 3, 4), weight=1, pad=20)
        
        self.janelaAdd.btnTrilhaPython = ctk.CTkButton(self.janelaAdd, text="Trilha Python", command=lambda: self.add_residentes("python"))
        self.janelaAdd.btnTrilhaPython.grid(row=2, column=1)

        self.janelaAdd.btnTrilhaDotNet = ctk.CTkButton(self.janelaAdd, text="Trilha .NET", command=lambda: self.add_residentes("dotnet"))
        self.janelaAdd.btnTrilhaDotNet.grid(row=2, column=2)

        self.janelaAdd.btnTrilhaJava = ctk.CTkButton(self.janelaAdd, text="Trilha Java", command=lambda: self.add_residentes("java"))
        self.janelaAdd.btnTrilhaJava.grid(row=2, column=3)
        
        
    def add_residentes(self, trilha):
        self.janelaAdd.btnTrilhaPython.destroy()
        self.janelaAdd.btnTrilhaDotNet.destroy()
        self.janelaAdd.btnTrilhaJava.destroy()
        
        self.janelaAdd.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=0, pad=20)
        
        areasFormacao = ["Formação técnica", "Formação técnica graduação em andamento", "Graduação em andamento", "Graduação concluída"]
        areasFormacaoGeral = ["Engenharia", "Computação"]
        experienciaPrevia = ["Sim", "Não"]
        # areasEspeficas = []
        
        
        # create variables with self
        self.janelaAdd.varCPF = ctk.StringVar()
        self.janelaAdd.varAnoNasc = ctk.StringVar()
        self.janelaAdd.varIdade = ctk.StringVar()
        self.janelaAdd.varFormacao = ctk.StringVar()
        self.janelaAdd.varFormacaoGeral = ctk.StringVar()
        self.janelaAdd.varFormacaoEspecifica = ctk.StringVar()
        self.janelaAdd.varAndamentoGraduacao = ctk.StringVar()
        self.janelaAdd.varTempoFormacao = ctk.StringVar()
        self.janelaAdd.varExperienciaPrevia = ctk.StringVar()
        
        
        # create variables
        # varCPF = ctk.StringVar()
        # varAnoNasc = ctk.StringVar()
        # varIdade = ctk.StringVar()
        # varFormacao = ctk.StringVar()
        # varFormacaoGeral = ctk.StringVar()
        # varFormacaoEspecifica = ctk.StringVar()
        # varAndamentoGraduacao = ctk.StringVar()
        # varTempoFormacao = ctk.StringVar()
        # varExperienciaPrevia = ctk.StringVar()
        
        
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
        self.janelaAdd.inpCPF = ctk.CTkEntry(self.janelaAdd, textvariable=self.janelaAdd.varCPF)
        self.janelaAdd.inpCPF.grid(row=1, column=3)
        
        self.janelaAdd.inpAnoNasc = ctk.CTkEntry(self.janelaAdd, textvariable=self.janelaAdd.varAnoNasc)
        self.janelaAdd.inpAnoNasc.grid(row=2, column=3)
        
        self.janelaAdd.inpIdade = ctk.CTkEntry(self.janelaAdd, textvariable=self.janelaAdd.varIdade)
        self.janelaAdd.inpIdade.grid(row=3, column=3)
        
        self.janelaAdd.inpFormacao = ctk.CTkComboBox(self.janelaAdd, values=areasFormacao,
                                    width=200, command=None, variable=self.janelaAdd.varFormacao, state="readonly")
        self.janelaAdd.inpFormacao.grid(row=4, column=3)
        
        self.janelaAdd.inpFormacaoGeral = ctk.CTkComboBox(self.janelaAdd, values=areasFormacaoGeral,
                                    command=self.set_formacao_geral, variable=self.janelaAdd.varFormacaoGeral, state="readonly")
        self.janelaAdd.inpFormacaoGeral.grid(row=5, column=3)
        
        self.janelaAdd.inpFormacaoEspecifica = ctk.CTkComboBox(self.janelaAdd, width=200,
                                                               command=None, variable=self.janelaAdd.varFormacaoEspecifica)
        self.janelaAdd.inpFormacaoEspecifica.grid(row=6, column=3)
        
        self.janelaAdd.inpAndamentoGraduacao = ctk.CTkEntry(self.janelaAdd, textvariable=self.janelaAdd.varAndamentoGraduacao)
        self.janelaAdd.inpAndamentoGraduacao.grid(row=7, column=3)
        
        self.janelaAdd.inpTempoFormacao = ctk.CTkEntry(self.janelaAdd, textvariable=self.janelaAdd.varTempoFormacao)
        self.janelaAdd.inpTempoFormacao.grid(row=8, column=3)
        
        self.janelaAdd.inpExperienciaPrevia = ctk.CTkComboBox(self.janelaAdd, values=experienciaPrevia,
                                    command=None, variable=self.janelaAdd.varExperienciaPrevia, state="readonly")
        self.janelaAdd.inpExperienciaPrevia.grid(row=9, column=3)
        
        
        # create buttons
        self.janelaAdd.btnAdcionar = ctk.CTkButton(self.janelaAdd, fg_color="green", command=lambda: self.adicionar(trilha))
        self.janelaAdd.btnAdcionar.grid(row=11, column=2)
        self.janelaAdd.btnAdcionar.configure(text="Adcionar")
        
        self.janelaAdd.btnVoltar = ctk.CTkButton(self.janelaAdd, fg_color="transparent", text_color="red", command=self.voltar)
        self.janelaAdd.btnVoltar.grid(row=11, column=3)
        self.janelaAdd.btnVoltar.configure(text="Voltar")
    
    
    def voltar(self):
        self.janelaAdd.destroy()
        
    def adicionar(self, trilha):
        # print(f"Variavel {self.janelaAdd.varCPF.get()}")
        print(f"Adicionar na trilha de {trilha}")
    
    def carregar_dados(self):
        janeleCarregar = ctk.CTkToplevel(self)
        janeleCarregar.title("Carregar Dados")
        janeleCarregar.geometry(f"{400}x{400}")
        
    def set_formacao_geral(self, formacao: str) -> None:
        if formacao == "Computação":
            areasEspeficas = ["Ciência da Computação", "Sistemas de Informação", "Análise e Desenvolvimento de Sistemas", "Engenharia de Software", "Outro"]
        elif formacao == "Engenharia":
            areasEspeficas = ["Engenharia de Computação", "Engenharia Química", "Engenharia de Produção", "Engenharia Mecânica", "Engenharia Elétrica", 
                                             "Engenharia Civil", "Engenharia de Alimentos", "Engenharia Ambiental", "Engenharia Aeroespacial", "Engenharia Nuclear", 
                                             "Engenharia de Materiais", "Outro"]
        else:
            areasEspeficas = []
        
        # self.janelaAdd.varFormacaoEspecifica.set("")
        self.janelaAdd.inpFormacaoEspecifica.configure(values=areasEspeficas)
        