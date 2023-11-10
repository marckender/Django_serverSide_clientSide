import tkinter as tk
from tkinter import simpledialog
import requests

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        self.usuario = simpledialog.askstring("Usuário", "Digite seu nome de usuário:")
        self.mensagens_text = tk.Text(self.root, wrap="word", state=tk.DISABLED)
        self.entry = tk.Entry(self.root, width=50)
        self.send_button = tk.Button(self.root, text="Enviar", command=self.enviar_mensagem)

        self.mensagens_text.pack(padx=10, pady=10)
        self.entry.pack(padx=10, pady=10, side=tk.LEFT)
        self.send_button.pack(pady=10, side=tk.RIGHT)

        self.atualizar_mensagens()

    def enviar_mensagem(self):
        mensagem = self.entry.get()
        if mensagem:
            self.enviar_para_api(mensagem)

            self.entry.delete(0, tk.END)

            self.atualizar_mensagens()

    def enviar_para_api(self, mensagem):
        api_url = "http://127.0.0.1:8000/api/mensagens/"
        data = {"usuario": self.usuario, "mensagem": mensagem}

        try:
            response = requests.post(api_url, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem para a API: {e}")

    def buscar_mensagens_api(self):
        api_url = "http://127.0.0.1:8000/api/mensagens/"

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar mensagens da API: {e}")
            return []

    def atualizar_mensagens(self):
        self.mensagens_text.config(state=tk.NORMAL)
        self.mensagens_text.delete(1.0, tk.END)

        mensagens = self.buscar_mensagens_api()

        for mensagem in mensagens:
            self.mensagens_text.insert(tk.END, f"{mensagem['usuario']}: {mensagem['mensagem']}\n")

        self.mensagens_text.yview(tk.END)

        self.mensagens_text.config(state=tk.DISABLED)

root = tk.Tk()
app = ChatApp(root)
root.mainloop()