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
        
        self.janelaAdd = ctk.CTkToplevel(self)
        self.janelaAdd.title("Adicionar Residentes")
        self.janelaAdd.geometry(f"{500}x{800}")
        
        self.janelaAdd.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        # self.janelaAdd.grid_rowconfigure((0, 10), weight=1)
        self.janelaAdd.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), weight=0, pad=20)
        
        
        # create labels
        self.janelaAdd.lblCPF = ctk.CTkLabel(self.janelaAdd)
        self.janelaAdd.lblCPF.grid(row=1, column=1)
        self.janelaAdd.lblCPF.configure(text="CPF (3 primeiros digitos):")
        
        self.janelaAdd.lblAnoNasc = ctk.CTkLabel(self.janelaAdd)
        self.janelaAdd.lblAnoNasc.grid(row=2, column=1)
        self.janelaAdd.lblAnoNasc.configure(text="Ano de Nascimento:")
        
        self.janelaAdd.lblIdade = ctk.CTkLabel(self.janelaAdd)
        self.janelaAdd.lblIdade.grid(row=3, column=1)
        self.janelaAdd.lblIdade.configure(text="Idade:")
        
        self.janelaAdd.lblFormacao = ctk.CTkLabel(self.janelaAdd)
        self.janelaAdd.lblFormacao.grid(row=4, column=1)
        self.janelaAdd.lblFormacao.configure(text="Formação:")
        
        self.janelaAdd.lblFormacaoGeral = ctk.CTkLabel(self.janelaAdd)
        self.janelaAdd.lblFormacaoGeral.grid(row=5, column=1)
        self.janelaAdd.lblFormacaoGeral.configure(text="Formação Geral:")
        
        self.janelaAdd.lblFormacaoEspecifica = ctk.CTkLabel(self.janelaAdd)
        self.janelaAdd.lblFormacaoEspecifica.grid(row=6, column=1)
        self.janelaAdd.lblFormacaoEspecifica.configure(text="Formação Específica:")
        
        self.janelaAdd.lblAndamentoGraduacao = ctk.CTkLabel(self.janelaAdd)
        self.janelaAdd.lblAndamentoGraduacao.grid(row=7, column=1)
        self.janelaAdd.lblAndamentoGraduacao.configure(text="Andamento da Graduação:")
        
        self.janelaAdd.lblTempoFormacao = ctk.CTkLabel(self.janelaAdd)
        self.janelaAdd.lblTempoFormacao.grid(row=8, column=1)
        self.janelaAdd.lblTempoFormacao.configure(text="Tempo de Formação:")
        
        self.janelaAdd.lblExperienciaPrevia = ctk.CTkLabel(self.janelaAdd)
        self.janelaAdd.lblExperienciaPrevia.grid(row=9, column=1)
        self.janelaAdd.lblExperienciaPrevia.configure(text="Experiência Prévia:")
        
        
        # create inputs
        self.janelaAdd.inpCPF = ctk.CTkEntry(self.janelaAdd)
        self.janelaAdd.inpCPF.grid(row=1, column=2)
        
        self.janelaAdd.inpAnoNasc = ctk.CTkEntry(self.janelaAdd)
        self.janelaAdd.inpAnoNasc.grid(row=2, column=2)
        
        self.janelaAdd.inpIdade = ctk.CTkEntry(self.janelaAdd)
        self.janelaAdd.inpIdade.grid(row=3, column=2)
        
        self.janelaAdd.inpFormacao = ctk.CTkComboBox(self.janelaAdd, values=areasFormacao,
                                    command=None)
        self.janelaAdd.inpFormacao.grid(row=4, column=2)
        
        self.janelaAdd.inpFormacaoGeral = ctk.CTkComboBox(self.janelaAdd, values=areasFormacaoGeral,
                                    command=None)
        self.janelaAdd.inpFormacaoGeral.grid(row=5, column=2)
        
        self.janelaAdd.inpFormacaoEspecifica = ctk.CTkEntry(self.janelaAdd)
        self.janelaAdd.inpFormacaoEspecifica.grid(row=6, column=2)
        
        self.janelaAdd.inpAndamentoGraduacao = ctk.CTkEntry(self.janelaAdd)
        self.janelaAdd.inpAndamentoGraduacao.grid(row=7, column=2)
        
        self.janelaAdd.inpTempoFormacao = ctk.CTkEntry(self.janelaAdd)
        self.janelaAdd.inpTempoFormacao.grid(row=8, column=2)
        
        self.expPrev = tk.BooleanVar(value=True)
        
        self.janelaAdd.rbExpPrevTrue = ctk.CTkRadioButton(self.janelaAdd, variable=self.expPrev, value=True)
        self.janelaAdd.rbExpPrevTrue.configure(text="Sim")
        self.janelaAdd.rbExpPrevTrue.grid(row=9, column=2)
        
        self.janelaAdd.rbExpPrevFalse = ctk.CTkRadioButton(self.janelaAdd, variable=self.expPrev, value=False)
        self.janelaAdd.rbExpPrevFalse.configure(text="Não")
        self.janelaAdd.rbExpPrevFalse.grid(row=9, column=3)
        
        
        
        # create buttons
        self.janelaAdd.btnAdcionar = ctk.CTkButton(self.janelaAdd, fg_color="green")
        self.janelaAdd.btnAdcionar.grid(row=11, column=1)
        self.janelaAdd.btnAdcionar.configure(text="Adcionar")
        
        self.janelaAdd.btnCancelar = ctk.CTkButton(self.janelaAdd, fg_color="transparent", text_color="red", command=self.voltar)
        self.janelaAdd.btnCancelar.grid(row=11, column=2)
        self.janelaAdd.btnCancelar.configure(text="Cancelar")
    
    
    def voltar(self):
        self.janelaAdd.destroy()
    
    def carregar_dados(self):
        janeleCarregar = ctk.CTkToplevel(self)
        janeleCarregar.title("Carregar Dados")
        janeleCarregar.geometry(f"{400}x{400}")
        