import sqlite3

def init_db():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            descricao TEXT,
            especificacoes TEXT
        )
    ''')
    
    # Inserir dados de teste (apenas se a tabela estiver vazia)
    cursor.execute("SELECT COUNT(*) FROM produtos")
    if cursor.fetchone()[0] == 0:
        produtos = [
            ("Placa Mãe B550", 15, "Placa mãe ATX para processadores AMD", "Chipset B550, 4x DDR4, 2x M.2"),
            ("Processador Ryzen 5", 30, "Processador de 6 núcleos", "Frequência base 3.7GHz, AM4"),
            ("Memória RAM 16GB", 50, "Módulo de memória DDR4", "3200MHz, CL16, RGB")
        ]
        cursor.executemany("INSERT INTO produtos (nome, quantidade, descricao, especificacoes) VALUES (?, ?, ?, ?)", produtos)
        conn.commit()
        
    conn.close()
    print("Banco de dados inicializado com sucesso.")

if __name__ == "__main__":
    init_db()