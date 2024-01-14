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
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 4), weight=1)
                
        # create buttons
        self.btnAddResidentes = ctk.CTkButton(self, command=self.add_residentes)
        self.btnAddResidentes.grid(row=1, column=1)
        self.btnAddResidentes.configure(text="Add Residentes")
        
        self.btnCarregarDados = ctk.CTkButton(self, command=self.carregar_dados)
        self.btnCarregarDados.grid(row=1, column=2)
        self.btnCarregarDados.configure(text="Carregar Dados")
        
        
    def add_residentes(self):
        areasFormacao = ["Formação técnica", "Formação técnica graduação em andamento", "Graduação em andamento", "Graduação concluída"]
        areasFormacaoGeral = ["Engenharia", "Computação"]
        
        janelaAdd = ctk.CTkToplevel(self)
        janelaAdd.title("Adicionar Residentes")
        janelaAdd.geometry(f"{500}x{800}")
        
        janelaAdd.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        # janelaAdd.grid_rowconfigure((0, 10), weight=1)
        janelaAdd.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=0, pad=20)
        
        
        # create labels
        janelaAdd.lblCPF = ctk.CTkLabel(janelaAdd)
        janelaAdd.lblCPF.grid(row=1, column=1)
        janelaAdd.lblCPF.configure(text="CPF (3 primeiros digitos):")
        
        janelaAdd.lblAnoNasc = ctk.CTkLabel(janelaAdd)
        janelaAdd.lblAnoNasc.grid(row=2, column=1)
        janelaAdd.lblAnoNasc.configure(text="Ano de Nascimento:")
        
        janelaAdd.lblIdade = ctk.CTkLabel(janelaAdd)
        janelaAdd.lblIdade.grid(row=3, column=1)
        janelaAdd.lblIdade.configure(text="Idade:")
        
        janelaAdd.lblFormacao = ctk.CTkLabel(janelaAdd)
        janelaAdd.lblFormacao.grid(row=4, column=1)
        janelaAdd.lblFormacao.configure(text="Formação:")
        
        janelaAdd.lblFormacaoGeral = ctk.CTkLabel(janelaAdd)
        janelaAdd.lblFormacaoGeral.grid(row=5, column=1)
        janelaAdd.lblFormacaoGeral.configure(text="Formação Geral:")
        
        janelaAdd.lblFormacaoEspecifica = ctk.CTkLabel(janelaAdd)
        janelaAdd.lblFormacaoEspecifica.grid(row=6, column=1)
        janelaAdd.lblFormacaoEspecifica.configure(text="Formação Específica:")
        
        janelaAdd.lblAndamentoGraduacao = ctk.CTkLabel(janelaAdd)
        janelaAdd.lblAndamentoGraduacao.grid(row=7, column=1)
        janelaAdd.lblAndamentoGraduacao.configure(text="Andamento da Graduação:")
        
        janelaAdd.lblTempoFormacao = ctk.CTkLabel(janelaAdd)
        janelaAdd.lblTempoFormacao.grid(row=8, column=1)
        janelaAdd.lblTempoFormacao.configure(text="Tempo de Formação:")
        
        janelaAdd.lblExperienciaPrevia = ctk.CTkLabel(janelaAdd)
        janelaAdd.lblExperienciaPrevia.grid(row=9, column=1)
        janelaAdd.lblExperienciaPrevia.configure(text="Experiência Prévia:")
        
        
        # create inputs
        janelaAdd.inpCPF = ctk.CTkEntry(janelaAdd)
        janelaAdd.inpCPF.grid(row=1, column=2)
        
        janelaAdd.inpAnoNasc = ctk.CTkEntry(janelaAdd)
        janelaAdd.inpAnoNasc.grid(row=2, column=2)
        
        janelaAdd.inpIdade = ctk.CTkEntry(janelaAdd)
        janelaAdd.inpIdade.grid(row=3, column=2)
        
        janelaAdd.inpFormacao = ctk.CTkComboBox(janelaAdd, values=areasFormacao,
                                    command=None)
        janelaAdd.inpFormacao.grid(row=4, column=2)
        
        janelaAdd.inpFormacaoGeral = ctk.CTkComboBox(janelaAdd, values=areasFormacaoGeral,
                                    command=None)
        janelaAdd.inpFormacaoGeral.grid(row=5, column=2)
        
        janelaAdd.inpFormacaoEspecifica = ctk.CTkEntry(janelaAdd)
        janelaAdd.inpFormacaoEspecifica.grid(row=6, column=2)
        
        janelaAdd.inpAndamentoGraduacao = ctk.CTkEntry(janelaAdd)
        janelaAdd.inpAndamentoGraduacao.grid(row=7, column=2)
        
        janelaAdd.inpTempoFormacao = ctk.CTkEntry(janelaAdd)
        janelaAdd.inpTempoFormacao.grid(row=8, column=2)
        
        self.expPrev = tk.BooleanVar(value=True)
        
        janelaAdd.rbExpPrevTrue = ctk.CTkRadioButton(janelaAdd, variable=self.expPrev, value=True)
        janelaAdd.rbExpPrevTrue.configure(text="Sim")
        janelaAdd.rbExpPrevTrue.grid(row=9, column=2)
        
        janelaAdd.rbExpPrevFalse = ctk.CTkRadioButton(janelaAdd, variable=self.expPrev, value=False)
        janelaAdd.rbExpPrevFalse.configure(text="Não")
        janelaAdd.rbExpPrevFalse.grid(row=9, column=3)
        
        
        
        # create buttons
        janelaAdd.btnAdcionar = ctk.CTkButton(janelaAdd, fg_color="green")
        janelaAdd.btnAdcionar.grid(row=11, column=1)
        janelaAdd.btnAdcionar.configure(text="Adcionar")
        
        janelaAdd.btnCancelar = ctk.CTkButton(janelaAdd, fg_color="transparent", text_color="red")
        janelaAdd.btnCancelar.grid(row=11, column=2)
        janelaAdd.btnCancelar.configure(text="Cancelar")
    
    
    def carregar_dados(self):
        janeleCarregar = ctk.CTkToplevel(self)
        janeleCarregar.title("Carregar Dados")
        janeleCarregar.geometry(f"{400}x{400}")
        