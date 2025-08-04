import os
import shutil

origem = os.path.expanduser("~/Downloads")
destino = os.path.expanduser("~/Arquivos_Organizados")

for nome_arquivo in os.listdir(origem):
    origem_arquivo = os.path.join(origem, nome_arquivo)
    if os.path.isfile(origem_arquivo):
        extensao = nome_arquivo.split('.')[-1]
        destino_pasta = os.path.join(destino, extensao)
        os.makedirs(destino_pasta, exist_ok=True)
        shutil.move(origem_arquivo, os.path.join(destino_pasta, nome_arquivo))

print("Arquivos organizados com sucesso.")
