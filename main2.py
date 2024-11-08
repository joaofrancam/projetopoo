import tkinter as tk
from tkinter import ttk, messagebox

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Registro Acadêmico")
        self.master.geometry("500x250")

        # Cria um frame dentro do widget master
        self.frame = ttk.Frame(master)
        self.frame.pack(pady=20)

        #Label REgistro Acadêmico
        self.titulo = ttk.Label(self.frame, text="Registro Acadêmico")
        self.titulo.pack(pady=20)

        # Botão Registro Aluno
        self.registro_aluno = ttk.Button(self.frame, text="Registro Aluno", command=self.abrir_janela_registro)
        self.registro_aluno.pack(pady=10)

        # Botão Notas
        self.notas = ttk.Button(self.frame, text="Notas", command=self.abrir_janela_notas)
        self.notas.pack()

    def abrir_janela_registro(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("Registro Aluno")
        self.new_window.geometry("700x500")
        Janela_registro(self.new_window)

    def abrir_janela_notas(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("Notas")
        self.new_window.geometry("700x500")
        Janela_notas(self.new_window)

class Janela_registro:
    def __init__(self, master=None):
        self.master = master

        self.frame = ttk.Frame(master)
        self.frame.pack(pady=20)

        #Nome
        self.label_nome = tk.Label(self.frame, text="Nome do Aluno:")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        #Curso
        self.label_curso = tk.Label(self.frame, text="Curso:")
        self.label_curso.grid(row=1, column=0, padx=5, pady=5)
        self.curso_var = tk.StringVar()
        cursos = ["ADS", "Administração", "Medicina"]
        for idx, curso in enumerate(cursos):
            self.raddio_cursos = tk.Radiobutton(self.frame, text=curso, variable=self.curso_var, value=curso)
            self.raddio_cursos.grid(row=1, column=idx+1, padx=5, pady=5, sticky='w')
        
        #email
        self.label_email = tk.Label(self.frame, text="Email:")
        self.label_email.grid(row=2, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(self.frame)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        #Botão Salvar
        self.btn_salvar = tk.Button(self.frame, text='Salvar', command=self.salvar_dados)
        self.btn_salvar.grid(row=3, columnspan=5, pady=10)

    def salvar_dados(self):
        nome = self.entry_nome.get()
        curso = self.curso_var.get()
        email = self.entry_email.get()
        if nome and curso and email:
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
            self.entry_nome.delete(0, tk.END)
            self.curso_var.set("")
            self.entry_email.delete(0,tk.END)
        else:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")


class Janela_notas:
    def __init__(self, master=None):
        self.master = master

        self.frame = ttk.Frame(master)
        self.frame.pack(pady=20)

        # Cria titulo janela Notas
        self.label = ttk.Label(self.frame, text="Notas")
        self.label.pack(pady=20)

        # Cria um botão para fechar a janela notas
        self.close_button = ttk.Button(self.frame, text="Fechar", command=self.master.destroy)
        self.close_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()