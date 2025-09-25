import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        valor_str = entry_valor.get()
        valor_str = valor_str.replace(".", "")
        valor_str = valor_str.replace(",", ".")
        valor_bruto = float(valor_str)

        total_alunos = int(entry_alunos.get())

        empresa1 = 0.32
        empresa2 = 0.04
        empresa3 = 0.18
        empresa4 = 0.18
        empresa5 = 0.28

        valor_barao = valor_bruto * empresa1
        valor_anglo = valor_bruto * empresa2
        valor_ateneu = valor_bruto * empresa3
        valor_liceu = valor_bruto * empresa4
        valor_instituto = valor_bruto * empresa5

        alunos_barao = total_alunos * empresa1
        alunos_anglo = total_alunos * empresa2
        alunos_ateneu = total_alunos * empresa3
        alunos_liceu = total_alunos * empresa4
        alunos_instituto = total_alunos * empresa5

        resultado = "empresa1: R$ " + str(round(valor_barao, 2)) + " | Alunos: " + str(round(alunos_barao)) + "\n"
        resultado += "empresa2: R$ " + str(round(valor_anglo, 2)) + " | Alunos: " + str(round(alunos_anglo)) + "\n"
        resultado += "empresa3: R$ " + str(round(valor_ateneu, 2)) + " | Alunos: " + str(round(alunos_ateneu)) + "\n"
        resultado += "empresa4: R$ " + str(round(valor_liceu, 2)) + " | Alunos: " + str(round(alunos_liceu)) + "\n"
        resultado += "empresa5: R$ " + str(round(valor_instituto, 2)) + " | Alunos: " + str(round(alunos_instituto))

        messagebox.showinfo("Distribuição", resultado)

    except:
        messagebox.showerror("Erro", "Digite números válidos!")


root = tk.Tk()
root.title("Distribuição")

tk.Label(root, text="Valor Bruto:").grid(row=0, column=0)
entry_valor = tk.Entry(root)
entry_valor.grid(row=0, column=1)

tk.Label(root, text="Total de Alunos:").grid(row=1, column=0)
entry_alunos = tk.Entry(root)
entry_alunos.grid(row=1, column=1)

btn = tk.Button(root, text="Calcular", command=calcular)
btn.grid(row=2, column=0, columnspan=2)

root.mainloop()
