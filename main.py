import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class SistemaAcademico:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Acadêmico")
        self.root.geometry("600x400")

        # Conectar ao banco de dados e criar as tabelas se não existirem
        self.conectar_banco_de_dados()

        # Frame principal
        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=10, fill="x", expand=True) #container responsivo no expand, fill faz com que o container expanda ao maximo na horizontal

        # Abas
        self.abas = ttk.Notebook(self.frame)
        self.abas.pack(fill="x", expand=True)

        self.aba_alunos = ttk.Frame(self.abas)
        self.aba_professores = ttk.Frame(self.abas)
        self.aba_cursos = ttk.Frame(self.abas)
        self.aba_registros = ttk.Frame(self.abas)

        self.abas.add(self.aba_alunos, text="Alunos") #add, adiciona uma nova aba ao notebook
        self.abas.add(self.aba_professores, text="Professores")
        self.abas.add(self.aba_cursos, text="Cursos")
        self.abas.add(self.aba_registros, text="Registros")

        # Formulário de Alunos
        self.label_nome_aluno = ttk.Label(self.aba_alunos, text="Nome:")
        self.label_nome_aluno.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome_aluno = ttk.Entry(self.aba_alunos)
        self.entry_nome_aluno.grid(row=0, column=1, padx=5, pady=5)

        self.label_email_aluno = ttk.Label(self.aba_alunos, text="Email:")
        self.label_email_aluno.grid(row=1, column=0, padx=5, pady=5)
        self.entry_email_aluno = ttk.Entry(self.aba_alunos)
        self.entry_email_aluno.grid(row=1, column=1, padx=5, pady=5)

        self.btn_salvar_aluno = ttk.Button(self.aba_alunos, text="Salvar", command=self.salvar_aluno)
        self.btn_salvar_aluno.grid(row=2, columnspan=2, pady=10)

        # Formulário de Professores
        self.label_nome_prof = ttk.Label(self.aba_professores, text="Nome:")
        self.label_nome_prof.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome_prof = ttk.Entry(self.aba_professores)
        self.entry_nome_prof.grid(row=0, column=1, padx=5, pady=5)

        self.label_email_prof = ttk.Label(self.aba_professores, text="Email:")
        self.label_email_prof.grid(row=1, column=0, padx=5, pady=5)
        self.entry_email_prof = ttk.Entry(self.aba_professores)
        self.entry_email_prof.grid(row=1, column=1, padx=5, pady=5)

        self.btn_salvar_prof = ttk.Button(self.aba_professores, text="Salvar", command=self.salvar_professor)
        self.btn_salvar_prof.grid(row=2, columnspan=2, pady=10)

        # Formulário de Cursos
        self.label_nome_curso = ttk.Label(self.aba_cursos, text="Nome:")
        self.label_nome_curso.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome_curso = ttk.Entry(self.aba_cursos)
        self.entry_nome_curso.grid(row=0, column=1, padx=5, pady=5)

        self.label_professor_curso = ttk.Label(self.aba_cursos, text="Professor:")
        self.label_professor_curso.grid(row=1, column=0, padx=5, pady=5)
        self.professor_combobox = ttk.Combobox(self.aba_cursos, values=self.obter_professores(), state="readonly")
        self.professor_combobox.grid(row=1, column=1, padx=5, pady=5)

        self.btn_salvar_curso = ttk.Button(self.aba_cursos, text="Salvar", command=self.salvar_curso)
        self.btn_salvar_curso.grid(row=2, columnspan=2, pady=10)

        self.criar_tabela_registros()

        #botao de atualização de Registros
        self.btn_atualizar = ttk.Button(self.aba_registros, text="Atualizar", command=self.atualizar_tabela)
        self.btn_atualizar.pack(pady=10)

    def criar_tabela_registros(self):
        self.tree = ttk.Treeview(self.aba_registros, columns=("Tipo", "Nome", "Email/Professor"), show="headings")
        self.tree.heading("Tipo", text="Tipo") #heading define o nome do cabeçalho da coluna
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Email/Professor", text="Email/Professor")

        self.tree.pack(fill="both", expand=True)

        #Preencher a tabela com registros de alunos professores e cursos
        self.carregar_registros()


    def conectar_banco_de_dados(self):
        conn = sqlite3.connect('academico.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Professores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                id_professor INTEGER,
                FOREIGN KEY (id_professor) REFERENCES Professores(id)
            )
        ''')
        conn.commit()
        conn.close()

    def salvar_aluno(self):
        nome = self.entry_nome_aluno.get()
        email = self.entry_email_aluno.get()
        if nome and email:
            conn = sqlite3.connect('academico.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Alunos (nome, email) VALUES (?, ?)", (nome, email))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Aluno salvo com sucesso!")
            self.entry_nome_aluno.delete(0, tk.END)
            self.entry_email_aluno.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

    def salvar_professor(self):
        nome = self.entry_nome_prof.get()
        email = self.entry_email_prof.get()
        if nome and email:
            conn = sqlite3.connect('academico.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Professores (nome, email) VALUES (?, ?)", (nome, email))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Professor salvo com sucesso!")
            self.entry_nome_prof.delete(0, tk.END)
            self.entry_email_prof.delete(0, tk.END)
            self.professor_combobox['values'] = self.obter_professores()
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

    def salvar_curso(self):
        nome = self.entry_nome_curso.get()
        id_professor = self.obter_id_professor(self.professor_combobox.get())
        if nome and id_professor:
            conn = sqlite3.connect('academico.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Cursos (nome, id_professor) VALUES (?, ?)", (nome, id_professor))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Curso salvo com sucesso!")
            self.entry_nome_curso.delete(0, tk.END)
            self.professor_combobox.set("")
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")

    def carregar_registros(self):
        conn = sqlite3.connect('academico.db')
        cursor = conn.cursor()

        # limpar a tabela antes de carregar os novos dados
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Carregar registros de alunos 
        cursor.execute("SELECT nome, email FROM Alunos") 
        for row in cursor.fetchall(): self.tree.insert("", "end", values=("Aluno", row[0], row[1])) 

        # Carregar registros de professores 
        cursor.execute("SELECT nome, email FROM Professores") 
        for row in cursor.fetchall(): self.tree.insert("", "end", values=("Professor", row[0], row[1]))

        # Carregar registros de cursos 
        cursor.execute(""" SELECT c.nome, p.nome 
                            FROM Cursos c 
                            JOIN Professores p ON c.id_professor = p.id
                        """) 
        for row in cursor.fetchall(): self.tree.insert("", "end", values=("Curso", row[0], row[1]))

        conn.close()

    def atualizar_tabela(self):
        self.carregar_registros() 

    def obter_professores(self):
        conn = sqlite3.connect('academico.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM Professores")
        professores = [row[0] for row in cursor.fetchall()]
        conn.close()
        return professores

    def obter_id_professor(self, nome_professor):
        conn = sqlite3.connect('academico.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM Professores WHERE nome=?", (nome_professor,))
        id_professor = cursor.fetchone()
        conn.close()
        if id_professor:
            return id_professor[0]
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaAcademico(root)
    root.mainloop()
