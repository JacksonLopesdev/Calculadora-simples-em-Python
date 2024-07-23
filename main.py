import tkinter as tk

def botao_clique(caracter):
    if caracter == 'AC':
        visor_var.set("0")
    elif caracter == '=':
        try:
            resultado = eval(visor_var.get())
            visor_var.set(str(resultado))
        except Exception as e:
            visor_var.set("Erro")
    else:
        # Concatena o caracter ao visor
        valor_atual = visor_var.get()
        if valor_atual == "0":
            visor_var.set(caracter)
        else:
            visor_var.set(valor_atual + caracter)

root = tk.Tk()
root.title('Calculadora Simples')
root.geometry('300x300')

visor_var = tk.StringVar()
visor_var.set("0")  

visor_label = tk.Label(root, textvariable=visor_var, font=("Arial", 20), width=15, bd=5, relief="sunken", anchor="e")
visor_label.place(x=180, y=10, width=100, height=100)

botoes_config = [
    ('0', 60, 190), ('.', 10, 248),
    ('1', 10, 10), ('2', 60, 10), ('3', 110, 10),
    ('7', 10, 130), ('8', 60, 130), ('9', 110, 130),
    ('4', 10, 70), ('5', 60, 70), ('6', 110, 70),
    ('+', 10, 190), ('-', 110, 190),
    ('*', 60, 248), ('/', 110, 248),
    ('AC', 180, 248), ('=', 240, 248)
]

for btn_text, btn_x, btn_y in botoes_config:
    botao = tk.Button(root, text=btn_text, command=lambda txt=btn_text: botao_clique(txt), bg="black", fg="white", font=("Arial", 12), padx=10, pady=8)
    botao.pack()
    botao.place(x=btn_x, y=btn_y)

root.mainloop()
