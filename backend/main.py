from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Carregar variáveis de ambiente
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

# Configuração de CORS para permitir requisições do Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção, coloque a URL do seu frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definir a função que o Gemini pode chamar
def consultar_banco_dados(termo_pesquisa: str) -> str:
    """Consulta o banco de dados SQLite de estoque para buscar informações detalhadas de produtos."""
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nome, quantidade, descricao, especificacoes FROM produtos WHERE nome LIKE ?", 
        (f"%{termo_pesquisa}%",)
    )
    resultados = cursor.fetchall()
    conn.close()
    
    if not resultados:
        return f"Nenhum produto encontrado contendo '{termo_pesquisa}'."
    
    resposta = "Dados encontrados:\n"
    for r in resultados:
        resposta += f"- Nome: {r[0]} | Quantidade em estoque: {r[1]} | Descrição: {r[2]} | Especificações: {r[3]}\n"
    return resposta

# Configurar o modelo com a ferramenta
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    tools=[consultar_banco_dados],
    system_instruction="Você é um assistente virtual de uma loja de informática. Responda de forma educada, formatada e clara com base nas informações do banco de dados."
)

# Inicializar o chat com chamada automática de funções ativada
chat = model.start_chat(enable_automatic_function_calling=True)

class MensagemRequest(BaseModel):
    mensagem: str

@app.post("/chat")
async def responder_chat(req: MensagemRequest):
    try:
        response = chat.send_message(req.mensagem)
        return {"resposta": response.text}
    except Exception as e:
        return {"erro": str(e)}