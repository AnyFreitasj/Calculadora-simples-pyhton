import tkinter as tk
from tkinter import messagebox

# Funções das operações matemáticas
def adicionar_numero(numero):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + str(numero))

def limpar_display():
    entry_display.delete(0, tk.END)

def calcular_resultado():
    try:
        current = entry_display.get()
        resultado = eval(current)  # Avalia a expressão matemática
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, resultado)
    except Exception:
        messagebox.showerror("Erro", "Entrada inválida!")

def operação(op):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + op)

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Visual")

# Tela de exibição
entry_display = tk.Entry(root, width=16, font=('Arial', 24), bd=10, relief="sunken", justify="right")
entry_display.grid(row=0, column=0, columnspan=4)

# Botões numéricos (0-9)
botoes = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '+',
    '-', '*', '/'
]

# Adiciona os botões numéricos e de operações
linha = 1
coluna = 0
for botao in botoes:
    if botao == '=':
        tk.Button(root, text=botao, width=10, height=2, font=('Arial', 18), command=calcular_resultado).grid(row=linha, column=coluna)
    elif botao in ('+', '-', '*', '/'):
        tk.Button(root, text=botao, width=5, height=2, font=('Arial', 18), command=lambda op=botao: operação(op)).grid(row=linha, column=coluna)
    else:
        tk.Button(root, text=botao, width=5, height=2, font=('Arial', 18), command=lambda numero=botao: adicionar_numero(numero)).grid(row=linha, column=coluna)

    coluna += 1
    if coluna > 2:  # Ajusta a quantidade de colunas, já que temos 4 botões por linha
        coluna = 0
        linha += 1

# Botão de limpar
tk.Button(root, text="C", width=5, height=2, font=('Arial', 18), command=limpar_display).grid(row=linha, column=0)

# Botão de igual
tk.Button(root, text="=", width=5, height=2, font=('Arial', 18), command=calcular_resultado).grid(row=linha, column=1)

# Iniciar a interface gráfica
root.mainloop()
