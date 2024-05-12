import psycopg2
import csv
import time

# Função para inserir dados no PostgreSQL e registrar o tempo de execução
def inserir_dados_postgres(arquivo_resultados, arquivos):
    # Conexão com o banco de dados PostgreSQL
    conn = psycopg2.connect(
        dbname="nome_do_banco",
        user="usuario",
        password="senha",
        host="localhost"
    )
    
    # Cursor para executar comandos SQL
    cursor = conn.cursor()

    # Início do cronômetro
    start_time = time.time()

    # Iniciar transação
    cursor.execute("BEGIN")

    try:
        # Inserção dos dados de cada arquivo
        for arquivo in arquivos:
            with open(arquivo, 'r') as file:
                dados = file.read()
                cursor.execute("INSERT INTO tabela (coluna) VALUES (%s)", (dados,))

        # Commit da transação
        conn.commit()

        # Fim do cronômetro e cálculo do tempo total
        end_time = time.time()
        total_time = end_time - start_time

        # Registro do par ordenado (tamanho, tempo) em um arquivo CSV
        with open(arquivo_resultados, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([sum(os.path.getsize(arquivo) for arquivo in arquivos), total_time])

    except Exception as e:
        # Rollback da transação em caso de erro
        conn.rollback()
        print("Erro durante a inserção:", e)

    finally:
        # Fechar conexão com o banco de dados
        cursor.close()
        conn.close()

# Exemplo de uso
if __name__ == "__main__":
    # Lista de arquivos para inserção
    arquivos = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt"]  # Adapte conforme necessário

    # Arquivo CSV para registrar os resultados
    arquivo_resultados = "resultados.csv"

    # Inserir dados no PostgreSQL e registrar o tempo de execução
    inserir_dados_postgres(arquivo_resultados, arquivos)
