import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        valor_bruto = float(entry_valor.get())
        total_alunos = int(entry_alunos.get())

        empresas = {
            "empresa1": 0.32,
            "empresa2": 0.04,
            "empresa3": 0.18,
            "empresa4": 0.18,
            "empresa5": 0.28
        }

        resultado = ""
        for nome, percentual in empresas.items():
            valor_empresa = valor_bruto * percentual
            alunos_empresa = total_alunos * percentual
            resultado += f"{nome}:\n   Valor: R$ {valor_empresa:,.2f}\n   Alunos: {alunos_empresa:.0f}\n\n"

        messagebox.showinfo("Distribuição", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos!")


root = tk.Tk()
root.title("Distribuição de Valores e Alunos")

tk.Label(root, text="Valor Bruto (R$):").grid(row=0, column=0, padx=5, pady=5)
entry_valor = tk.Entry(root)
entry_valor.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Total de Alunos:").grid(row=1, column=0, padx=5, pady=5)
entry_alunos = tk.Entry(root)
entry_alunos.grid(row=1, column=1, padx=5, pady=5)

btn = tk.Button(root, text="Calcular", command=calcular)
btn.grid(row=2, columnspan=2, pady=10)

root.mainloop()


