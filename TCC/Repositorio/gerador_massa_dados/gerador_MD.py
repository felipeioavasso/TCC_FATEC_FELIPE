import os
import random

# Tamanho total em bytes (2 GB)
tamanho_total = 2 * 1024 * 1024 * 1024

# Tamanho máximo de cada arquivo (54,50 MB)
tamanho_max_arquivo = 54.50 * 1024 * 1024

# Lista para armazenar os tamanhos de cada arquivo
tamanhos_arquivos = []

# Preencher a lista com tamanhos aleatórios até atingir ou ultrapassar o tamanho total
tamanho_atual = 0
while tamanho_atual < tamanho_total:
    tamanho_arquivo = random.randint(1, int(tamanho_max_arquivo))  # Tamanho aleatório entre 1 byte e o máximo permitido
    if tamanho_atual + tamanho_arquivo > tamanho_total:
        tamanho_arquivo = tamanho_total - tamanho_atual  # Ajustar o último arquivo para que o total seja exatamente 2 GB
    tamanhos_arquivos.append(tamanho_arquivo)
    tamanho_atual += tamanho_arquivo

# Gerar arquivos com tamanhos variados
for i, tamanho_arquivo in enumerate(tamanhos_arquivos):
    # Nome do arquivo de saída
    nome_arquivo = f"dados_{i + 1}.txt"
    
    # Gerar dados aleatórios e escrevê-los no arquivo
    with open(nome_arquivo, 'wb') as arquivo:
        tamanho_atual = 0
        while tamanho_atual < tamanho_arquivo:
            dados_aleatorios = os.urandom(1024)  # Gera 1 KB de dados aleatórios
            arquivo.write(dados_aleatorios)
            tamanho_atual += len(dados_aleatorios)

    print(f"Arquivo {nome_arquivo} gerado com sucesso.")

print("Todos os arquivos foram gerados com sucesso!")
