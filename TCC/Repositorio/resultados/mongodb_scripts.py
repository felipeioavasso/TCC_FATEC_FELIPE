from pymongo import MongoClient
import os
import csv
import time

# Função para inserir dados no MongoDB e registrar o tempo de execução
def inserir_dados_mongodb(arquivo_resultados, arquivos):
    # Conexão com o servidor do MongoDB
    client = MongoClient('localhost', 27017)

    # Selecionar o banco de dados e a coleção
    db = client.nome_do_banco
    collection = db.nome_da_colecao

    # Início do cronômetro
    start_time = time.time()

    try:
        # Iniciar operação de inserção em lote (bulk insert)
        bulk_operations = []
        for arquivo in arquivos:
            with open(arquivo, 'r') as file:
                dados = file.read()
                bulk_operations.append({'data': dados})

        # Executar a inserção em lote
        result = collection.insert_many(bulk_operations)

        # Fim do cronômetro e cálculo do tempo total
        end_time = time.time()
        total_time = end_time - start_time

        # Registro do par ordenado (tamanho, tempo) em um arquivo CSV
        with open(arquivo_resultados, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([sum(os.path.getsize(arquivo) for arquivo in arquivos), total_time])

    except Exception as e:
        print("Erro durante a inserção:", e)

    finally:
        # Fechar conexão com o servidor do MongoDB
        client.close()

# Exemplo de uso
if __name__ == "__main__":
    # Lista de arquivos para inserção
    arquivos = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt"]  # Adapte conforme necessário

    # Arquivo CSV para registrar os resultados
    arquivo_resultados = "resultados.csv"

    # Inserir dados no MongoDB e registrar o tempo de execução
    inserir_dados_mongodb(arquivo_resultados, arquivos)
