import tkinter as tk
import customtkinter as ctk

class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ctk.set_default_color_theme("dark-blue")
        
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
        janelaAdd = ctk.CTkToplevel(self)
        janelaAdd.title("Add Residentes")
        janelaAdd.geometry(f"{400}x{400}")
        
    
    
    def carregar_dados(self):
        janeleCarregar = ctk.CTkToplevel(self)
        janeleCarregar.title("Carregar Dados")
        janeleCarregar.geometry(f"{400}x{400}")
        