import tkinter as tk
from tkinter import messagebox

# Funções das operações matemáticas
def soma():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado.set(num1 + num2)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def subtracao():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado.set(num1 - num2)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def multiplicacao():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado.set(num1 * num2)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def divisao():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Erro", "Não é possível dividir por zero!")
        else:
            resultado.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Visual")

# Definindo as variáveis
resultado = tk.StringVar()

# Labels para os números
label_num1 = tk.Label(root, text="Primeiro número:")
label_num1.grid(row=0, column=0)

label_num2 = tk.Label(root, text="Segundo número:")
label_num2.grid(row=1, column=0)

label_resultado = tk.Label(root, text="Resultado:")
label_resultado.grid(row=2, column=0)

# Entradas para os números
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

entry_resultado = tk.Entry(root, textvariable=resultado, state="readonly")
entry_resultado.grid(row=2, column=1)

# Botões para as operações
botao_soma = tk.Button(root, text="+", width=10, command=soma)
botao_soma.grid(row=3, column=0)

botao_subtracao = tk.Button(root, text="-", width=10, command=subtracao)
botao_subtracao.grid(row=3, column=1)

botao_multiplicacao = tk.Button(root, text="*", width=10, command=multiplicacao)
botao_multiplicacao.grid(row=4, column=0)

botao_divisao = tk.Button(root, text="/", width=10, command=divisao)
botao_divisao.grid(row=4, column=1)

# Iniciar a interface gráfica
root.mainloop()
