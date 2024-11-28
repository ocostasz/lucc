import tkinter as tk

# Função para calcular o IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())  # Pega o peso digitado
        altura = float(entry_altura.get())  # Pega a altura digitada
        imc = peso / (altura ** 2)  # Fórmula do IMC
        label_resultado.config(text=f"Seu IMC é: {imc:.2f}")  # Exibe o resultado
    except ValueError:
        label_resultado.config(text="Por favor, insira valores válidos.")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("500x500")  # Definindo o tamanho da janela

# Criando os rótulos (labels) para os inputs
label_peso = tk.Label(janela, text="Digite o peso (kg):")
label_peso.pack(pady=10)

# Criando o campo de entrada para o peso
entry_peso = tk.Entry(janela)
entry_peso.pack(pady=10)

# Criando o rótulo para altura
label_altura = tk.Label(janela, text="Digite a altura (m):")
label_altura.pack(pady=10)

# Criando o campo de entrada para a altura
entry_altura = tk.Entry(janela)
entry_altura.pack(pady=10)

# Criando o botão para calcular o IMC
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack(pady=20)

# Criando o label para mostrar o resultado
label_resultado = tk.Label(janela, text="Seu IMC será exibido aqui.")
label_resultado.pack(pady=10)

# Rodando a interface gráfica
janela.mainloop()
