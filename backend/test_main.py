from fastapi.testclient import TestClient
from main import app, consultar_banco_dados
import sqlite3

client = TestClient(app)

def test_consultar_banco_dados():
    # Testa a função interna do banco
    resultado = consultar_banco_dados("Placa Mãe")
    assert "Placa Mãe B550" in resultado
    assert "Nenhum produto encontrado" not in resultado

def test_endpoint_chat_erro_sem_body():
    # Testa se a API rejeita requisições mal formadas
    response = client.post("/chat")
    assert response.status_code == 422 # Unprocessable Entity