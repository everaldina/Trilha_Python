import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox, ttk
from resitic18.Residencia import Residencia
from datetime import date
import re
import os

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Resitic")
        self.geometry(f"{400}x{400}")
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.residencia = Residencia(["python", "dotnet", "java"])
        
        self.carregar_dados()
        
        # configure grid layout (4x4)
        self.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((1, 2, 3, 4), weight=1)
        
        # create buttons
        self.btnAddResidentes = ctk.CTkButton(self, text="Add Residentes", command=self.select_trilha)
        self.btnAddResidentes.grid(row=2, column=2)
        
        self.btnExibirResidentes = ctk.CTkButton(self, text="Exibir Residentes", command=self.exibir_residentes)
        self.btnExibirResidentes.grid(row=2, column=3)
        
        self.btnSalvarDados = ctk.CTkButton(self, text="Salvar Dados", command=self.salvar_dados)
        self.btnSalvarDados.grid(row=3, column=2)
        
        self.btnCarregarDados = ctk.CTkButton(self, text="Carregar Dados", command=self.carregar_dados)
        self.btnCarregarDados.grid(row=3, column=3)
        
        
    def select_trilha(self):
        self.janelaAdd = ctk.CTkToplevel(self)
        self.janelaAdd.title("Adicionar Residentes")
        self.janelaAdd.geometry(f"{500}x{600}")
        
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
        experienciaPrevia = ["Nenhuma", "Conhecimento básico", "Conhecimento intermediário", "Conhecimento avançado"]
        
        
        # create variables
        varCPF = ctk.StringVar()
        varAnoNasc = ctk.StringVar()
        varIdade = ctk.StringVar()
        varFormacao = ctk.StringVar()
        varFormacaoGeral = ctk.StringVar()
        varFormacaoEspecifica = ctk.StringVar()
        varAndamentoGraduacao = ctk.IntVar()
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
        
        self.janelaAdd.lblAndamentoGraduacao = ctk.CTkLabel(self.janelaAdd, text="Andamento da Graduação (%):")
        self.janelaAdd.lblAndamentoGraduacao.grid(row=7, column=2)
        
        self.janelaAdd.lblTempoFormacao = ctk.CTkLabel(self.janelaAdd, text="Tempo de Formação (anos):")
        self.janelaAdd.lblTempoFormacao.grid(row=9, column=2)
        
        self.janelaAdd.lblExperienciaPrevia = ctk.CTkLabel(self.janelaAdd, text="Experiência Prévia:")
        self.janelaAdd.lblExperienciaPrevia.grid(row=10, column=2)
        
        
        # create inputs
        self.janelaAdd.inpCPF = ctk.CTkEntry(self.janelaAdd, textvariable=varCPF)
        self.janelaAdd.inpCPF.grid(row=1, column=3)
        
        self.janelaAdd.inpAnoNasc = ctk.CTkEntry(self.janelaAdd, textvariable=varAnoNasc, validate="key", validatecommand=(self.register(Interface.validar_numero), "%P"))
        self.janelaAdd.inpAnoNasc.grid(row=2, column=3)
        
        self.janelaAdd.inpIdade = ctk.CTkEntry(self.janelaAdd, textvariable=varIdade, validate="key", validatecommand=(self.register(Interface.validar_numero), "%P"))
        self.janelaAdd.inpIdade.grid(row=3, column=3)
        self.janelaAdd.inpIdade.bind("<FocusOut>", lambda event: Interface.verificar_idade(self.janelaAdd.inpIdade, self.janelaAdd.inpAnoNasc.get()))
        
        self.janelaAdd.inpFormacao = ctk.CTkComboBox(self.janelaAdd, values=areasFormacao,
                                    width=200, command=self.set_formacao, variable=varFormacao, state="readonly")
        self.janelaAdd.inpFormacao.grid(row=4, column=3)
        
        self.janelaAdd.inpFormacaoGeral = ctk.CTkComboBox(self.janelaAdd, values=[],
                                    command=self.set_formacao_geral, variable=varFormacaoGeral, state="readonly")
        self.janelaAdd.inpFormacaoGeral.grid(row=5, column=3)
        
        self.janelaAdd.inpFormacaoEspecifica = ctk.CTkComboBox(self.janelaAdd, width=200,
                                                               command=None, values=[], 
                                                               variable=varFormacaoEspecifica, state="readonly")
        self.janelaAdd.inpFormacaoEspecifica.grid(row=6, column=3)
        
        self.janelaAdd.inpAndamentoGraduacao = ctk.CTkEntry(self.janelaAdd, textvariable=varAndamentoGraduacao, state="readonly")
        self.janelaAdd.inpAndamentoGraduacao.grid(row=7, column=3)
        self.janelaAdd.inpAndamentoGraduacaoSlider = ctk.CTkSlider(self.janelaAdd, from_=0, to=99, variable=varAndamentoGraduacao)
        self.janelaAdd.inpAndamentoGraduacaoSlider.grid(row=8, column=3)
        
        self.janelaAdd.inpTempoFormacao = ctk.CTkEntry(self.janelaAdd, textvariable=varTempoFormacao, validate="key", validatecommand=(self.register(Interface.validar_numero), "%P"))
        self.janelaAdd.inpTempoFormacao.grid(row=9, column=3)
        
        self.janelaAdd.inpExperienciaPrevia = ctk.CTkComboBox(self.janelaAdd, values=experienciaPrevia,
                                    command=None, variable=varExperienciaPrevia, state="readonly")
        self.janelaAdd.inpExperienciaPrevia.grid(row=10, column=3)
        
        
        # create buttons
        self.janelaAdd.btnAdicionar = ctk.CTkButton(self.janelaAdd, text="Adicionar", fg_color="green", command=lambda: self.adicionar(trilha, variaveis))
        self.janelaAdd.btnAdicionar.grid(row=11, column=2)
        
        self.janelaAdd.btnLimpar = ctk.CTkButton(self.janelaAdd, fg_color="transparent", text="Limpar", text_color="blue", command=self.limpar)
        self.janelaAdd.btnLimpar.grid(row=11, column=3)
        
        self.janelaAdd.btnVoltar = ctk.CTkButton(self.janelaAdd, text="Voltar", fg_color="transparent", text_color="red", command=self.voltar)
        self.janelaAdd.btnVoltar.grid(row=12, column=3)
    
    def voltar(self) -> None:
        self.janelaAdd.destroy()
        
    def limpar(self) -> None:
        self.janelaAdd.inpCPF.delete(0, tk.END)
        self.janelaAdd.inpAnoNasc.delete(0, tk.END)
        self.janelaAdd.inpIdade.delete(0, tk.END)
        self.janelaAdd.inpFormacao.set("")
        self.janelaAdd.inpFormacaoGeral.set("")
        self.janelaAdd.inpFormacaoEspecifica.set("")
        self.janelaAdd.inpAndamentoGraduacaoSlider.set(0)
        self.janelaAdd.inpTempoFormacao.delete(0, tk.END)
        self.janelaAdd.inpExperienciaPrevia.set("")
        
    def adicionar(self, trilha: str, variaveis: dict) -> None:
        formacoes = {"Formação técnica" : 0, "Formação técnica graduação em andamento": 1,
                      "Graduação em andamento": 2, "Graduação concluída": 3}
        
        formacoesGerais = {"Engenharia": 0, "Computação": 1}
        
        experienciaPrevia = {"Nenhuma": 0, "Conhecimento básico": 1, "Conhecimento intermediário": 2, "Conhecimento avançado": 3}
        
        formacaoGeral = variaveis['formacaoGeral'].get() or None
        formacaoEspecifica = variaveis['formacaoEspecifica'].get() or None
        andamentoGraduacao = variaveis['andamentoGraduacao'].get() or None
        tempoFormacao = variaveis['tempoFormacao'].get() or None
        formacao = variaveis['formacao'].get() or None
        cpf = variaveis['cpf'].get()
        ano = variaveis['anoNasc'].get()
        idade = variaveis['idade'].get()
        
        # validando campos
        if not Interface.validar_cpf(cpf):
            messagebox.showerror("Erro", "CPF inválido.")
            return
        
        if len(ano) != 4 or ano == '':
            messagebox.showerror("Erro", "Ano inválido.")
            return
        
        if idade == "":
            messagebox.showerror("Erro", "Idade não preenchida.")
            return
        else:
            idade = int(idade)
        
        ano_atual = date.today().year
        if idade == "" or (ano_atual - int(ano) != idade and ano_atual - int(ano) != idade +1):
            messagebox.showerror("Erro", "Idade inválida.")
            return
        
        if not formacao:
            messagebox.showerror("Erro  de formação", "Campo formação nao preenchido.")
            return
        formacao = formacoes[formacao]
        
        try:
            andamentoGraduacao = float(andamentoGraduacao)
        except:
            andamentoGraduacao = None
            
        erro_formatacao = Interface.validar_formacao(formacao, formacaoGeral, formacaoEspecifica, andamentoGraduacao, tempoFormacao)
        if erro_formatacao:
            messagebox.showerror("Erro de formação", erro_formatacao)
            return
        
        if formacaoGeral:
            formacaoGeral = formacoesGerais[formacaoGeral]
        if tempoFormacao:
            tempoFormacao = int(tempoFormacao)
    
        residente = {
            'identificador': cpf[:3] + ano[2:],
            'idade': int(variaveis['idade'].get()),
            'formacao': formacoes[variaveis['formacao'].get()],
            'formacaoGeral': formacaoGeral,
            'formacaoEspecifica': formacaoEspecifica,
            'andamentoGraduacao': andamentoGraduacao,
            'tempoFormacao': tempoFormacao,
            'experienciaPrevia': experienciaPrevia[variaveis['experienciaPrevia'].get()]
        }
        
        try:
            self.residencia.add_residente(trilha, residente)    
            
            self.janelaAdd.inpCPF.delete(0, tk.END)
            self.janelaAdd.inpAnoNasc.delete(0, tk.END)
            self.janelaAdd.inpIdade.delete(0, tk.END)
            self.janelaAdd.inpFormacao.set("")
            self.janelaAdd.inpFormacaoGeral.set("")
            self.janelaAdd.inpFormacaoEspecifica.set("")
            self.janelaAdd.inpAndamentoGraduacaoSlider.set(0)
            self.janelaAdd.inpTempoFormacao.delete(0, tk.END)
            self.janelaAdd.inpExperienciaPrevia.set("")
        except ValueError as e:
            messagebox.showerror("Erro", e)
        
    def carregar_dados(self) -> None:
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        caminho_dados = os.path.join(diretorio_atual, 'data')

        if not os.path.exists(caminho_dados):
            os.makedirs(caminho_dados)

        caminho_csv = os.path.join(caminho_dados, 'residencia.csv')
        
        try:
            self.residencia.load(caminho_csv)
        except ValueError as e:
            print(e)
            
    def salvar_dados(self) -> None:
        self.residencia.save()
    
    def exibir_residentes(self) -> None:
        self.janelaResidentes = ctk.CTkToplevel(self)
        self.janelaResidentes.title("Residentes")
        self.janelaResidentes.geometry(f"{1000}x{400}")
                
        residentes = self.residencia.get_residentes()
        
        columns = residentes.index.names + list(residentes.columns)
        
        # Criar um Treeview para exibir os dados
        tree = ttk.Treeview(self.janelaResidentes)
        tree["columns"] = columns
        tree["show"] = "headings"

        for column in columns:
            tree.heading(column, text=column)
            tree.column(column, anchor="center", width=100)

        for index, row in residentes.iterrows():
            tree.insert("", "end", values=tuple(index) + tuple(row))

        yscroll = ttk.Scrollbar(self.janelaResidentes, orient="vertical", command=tree.yview)
        yscroll.grid(row=0, column=1, sticky="ns")
        tree.configure(yscrollcommand=yscroll.set)

        xscroll = ttk.Scrollbar(self.janelaResidentes, orient="horizontal", command=tree.xview)
        xscroll.grid(row=1, column=0, sticky="ew")
        tree.configure(xscrollcommand=xscroll.set)

        tree.grid(row=0, column=0, sticky="nsew")

        self.janelaResidentes.grid_rowconfigure(0, weight=1)
        self.janelaResidentes.grid_columnconfigure(0, weight=1)
        
    def set_formacao(self, formacao: str) -> None:
        areasFormacaoGeral = ["Computação", "Engenharia", ""]
        
        if formacao == "Formação técnica":
            self.janelaAdd.inpFormacaoGeral.set("")
            self.janelaAdd.inpFormacaoEspecifica.set("")
            self.janelaAdd.inpAndamentoGraduacaoSlider.set(0)
            self.janelaAdd.inpTempoFormacao.delete(0, tk.END)
            
            self.janelaAdd.inpFormacaoGeral.configure(state="disabled")
            self.janelaAdd.inpFormacaoEspecifica.configure(state="disabled")
            self.janelaAdd.inpAndamentoGraduacaoSlider.configure(state="disabled")
            self.janelaAdd.inpTempoFormacao.configure(state="disabled")
            
            self.janelaAdd.inpFormacaoGeral.configure(values=[])
            self.janelaAdd.inpFormacaoEspecifica.configure(values=[])
        elif formacao == "Formação técnica graduação em andamento" or formacao == "Graduação em andamento":
            self.janelaAdd.inpTempoFormacao.delete(0, tk.END)
            
            self.janelaAdd.inpFormacaoGeral.configure(state="readonly")
            self.janelaAdd.inpFormacaoEspecifica.configure(state="readonly")
            self.janelaAdd.inpAndamentoGraduacaoSlider.configure(state="normal")
            self.janelaAdd.inpTempoFormacao.configure(state="disabled")
            
            self.janelaAdd.inpFormacaoGeral.configure(values=areasFormacaoGeral)
        elif formacao == "Graduação concluída":
            self.janelaAdd.inpAndamentoGraduacaoSlider.set(0)
            self.janelaAdd.inpAndamentoGraduacaoSlider.configure(state="disabled")
            self.janelaAdd.inpFormacaoGeral.configure(state="readonly")
            self.janelaAdd.inpFormacaoEspecifica.configure(state="readonly")
            self.janelaAdd.inpTempoFormacao.configure(state="normal")
            
            self.janelaAdd.inpFormacaoGeral.configure(values=areasFormacaoGeral)        

    def set_formacao_geral(self, formacao: str) -> None:
        if formacao == "Computação":
            areasEspeficas = ["Ciência da Computação", "Sistemas de Informação", "Análise e Desenvolvimento de Sistemas", "Engenharia de Software", "Outro"]
        elif formacao == "Engenharia":
            areasEspeficas = ["Engenharia da Computação", "Engenharia Química", "Engenharia de Produção", "Engenharia Mecânica", "Engenharia Elétrica", 
                                             "Engenharia Civil", "Engenharia de Alimentos", "Engenharia Ambiental", "Engenharia Aeroespacial", "Engenharia Nuclear", 
                                             "Engenharia de Materiais", "Outro"]
        else:
            areasEspeficas = []
        
        self.janelaAdd.inpFormacaoEspecifica.configure(values=areasEspeficas)
        self.janelaAdd.inpFormacaoEspecifica.set("")
        
    def validar_texto(entrada):
        return entrada.isalpha()

    def validar_numero(entrada):
        if entrada == "":
            return True
        
        return entrada.isdigit()

    def validar_float(entrada):
        if entrada == "" or entrada is None:
            return False
        
        try:
            float(entrada)
            return True
        except ValueError:
            return False

    def verificar_entrada_texto(input):
        valor = input.get()
        
        if not Interface.validar_texto(valor):
            messagebox.showerror("Erro de validação", "A entrada deve conter apenas letras.")
            
    def validar_cpf(cpf):
        if cpf == "":
            return False

        padrao = re.findall("^\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11}", cpf)
        
        if len(padrao) == 1 and len(padrao[0]) == len(cpf):
            return True
        else:
            return False
    
    def validar_formacao(formacao, formacaoGeral, formacaoEspecifica, andamentoGraduacao, tempoFormacao):
        if formacao == 0: # formação técnica
            if formacaoGeral:
                return "Não é possivel ter uma formação geral com formação técnica."
            if tempoFormacao:
                return "Não é possivel ter tempo de formação com formação técnica."
            if andamentoGraduacao:
                return "Não é possivel ter um andamento de graduação com formação técnica."
        else: # nivel superior
            if andamentoGraduacao and tempoFormacao:
                return "Não é possivel ter um andamento de graduação e um tempo de formação."
            if not formacaoEspecifica:
                return "Campo formação específica não preenchido."
            if not formacaoGeral:
                return "Campo formação geral não preenchido."
            
            if formacao == 1 or formacao == 2: # graduação em andamento
                if tempoFormacao:
                    return "Não é possivel ter um tempo de formação como graduando."
                if not andamentoGraduacao:
                    return "Campo andamento de graduação não preenchido."
                
            else: # graduação concluída
                if andamentoGraduacao:
                    return "Não é possivel ter um andamento de graduação com formação técnica."
                if not tempoFormacao:
                    return "Campo tempo de formação não preenchido."
        return None

    def verificar_idade(inpIdade, ano):
        idade = inpIdade.get()
        
        if idade == "":
            return
        
        if ano == "":
            messagebox.showerror("Erro", "Ano de nascimento não preenchido.")
            return
        
        idade = int(idade)
        ano_atual = date.today().year
        
        if idade == "" or (ano_atual - int(ano) != idade and ano_atual - int(ano) != idade +1):
            messagebox.showerror("Erro", "Idade inválida.")
            inpIdade.delete(0, tk.END)
            return
        
    def on_closing(self):
        self.salvar_dados()
        
        self.destroy()