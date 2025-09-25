import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        valor_str = entry_valor.get()
        valor_str = valor_str.replace(".", "")
        valor_str = valor_str.replace(",", ".")
        valor_bruto = float(valor_str)

        total_alunos = int(entry_alunos.get())

      
        barao = 0.32
        anglo = 0.04
        ateneu = 0.18
        liceu = 0.18
        instituto = 0.28

        valor_barao = valor_bruto * barao
        valor_anglo = valor_bruto * anglo
        valor_ateneu = valor_bruto * ateneu
        valor_liceu = valor_bruto * liceu
        valor_instituto = valor_bruto * instituto
        
        alunos_barao = total_alunos * barao
        alunos_anglo = total_alunos * anglo
        alunos_ateneu = total_alunos * ateneu
        alunos_liceu = total_alunos * liceu
        alunos_instituto = total_alunos * instituto

        
        resultado = "Barão: R$ " + str(round(valor_barao, 2)) + " | Alunos: " + str(round(alunos_barao)) + "\n"
        resultado += "Anglo: R$ " + str(round(valor_anglo, 2)) + " | Alunos: " + str(round(alunos_anglo)) + "\n"
        resultado += "Ateneu: R$ " + str(round(valor_ateneu, 2)) + " | Alunos: " + str(round(alunos_ateneu)) + "\n"
        resultado += "Liceu: R$ " + str(round(valor_liceu, 2)) + " | Alunos: " + str(round(alunos_liceu)) + "\n"
        resultado += "Instituto: R$ " + str(round(valor_instituto, 2)) + " | Alunos: " + str(round(alunos_instituto))

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
