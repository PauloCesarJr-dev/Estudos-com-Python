'''n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
# print('A soma de', n1, 'e', n2, 'vale', s)
print('A soma entre {} e {} vale {}' .format(n1, n2, s))'''
import tkinter as tk
import random

def mover_botao(event):
    novo_x = random.randint(0, 300)
    novo_y = random.randint(0, 300)
    botao.place(x=novo_x, y=novo_y)

def mensagem_boa_noite():
    label.config(text="Vamos dormir juntinhos! 💤")

janela = tk.Tk()
janela.title("Pegue o botão!")
janela.geometry("400x400")

label = tk.Label(janela, text="Tente clicar no botão!", font=("Arial", 14))
label.pack(pady=20)

botao = tk.Button(janela, text="Se conseguir clicar hoje tem", command=mensagem_boa_noite)
botao.place(x=150, y=150)

botao.bind("<Enter>", mover_botao)

janela.mainloop()