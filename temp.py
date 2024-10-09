import os
import tkinter as tk
from tkinter import messagebox

def agendar_desligamento():
    try:
        minutos = int(entry_minutos.get())
        segundos = minutos * 60
        comando = f"shutdown /s /t {segundos}"
        os.system(comando)
        messagebox.showinfo("Sucesso", f"Desligamento agendado para {minutos} minutos.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def cancelar_desligamento():
    os.system("shutdown /a")
    messagebox.showinfo("Cancelado", "Desligamento cancelado.")

# Criação da janela principal
root = tk.Tk()
root.title("Temporizador de Desligamento")
root.geometry("350x180")
root.resizable(False, False)

# Configuração de estilo e layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True)

# Título
titulo = tk.Label(frame, text="Desligamento Temporizado", font=("Arial", 14))
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Campo para inserção de minutos
label_instrucoes = tk.Label(frame, text="Digite o tempo em minutos:")
label_instrucoes.grid(row=1, column=0)

entry_minutos = tk.Entry(frame, width=10)
entry_minutos.grid(row=1, column=1, pady=10)

# Botão para agendar o desligamento
button_agendar = tk.Button(frame, text="Agendar Desligamento", command=agendar_desligamento, width=20)
button_agendar.grid(row=2, column=0, columnspan=2, pady=5)

# Botão para cancelar o desligamento
button_cancelar = tk.Button(frame, text="Cancelar Desligamento", command=cancelar_desligamento, width=20)
button_cancelar.grid(row=3, column=0, columnspan=2, pady=5)

# Iniciar o loop da interface gráfica
root.mainloop()