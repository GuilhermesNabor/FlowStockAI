# Chatbot com Gemini, SQLite e React

Este projeto é um assistente virtual inteligente capaz de consultar um banco de dados SQLite para responder perguntas sobre o estoque de produtos usando a API do Google Gemini (Function Calling).

## Tecnologias Utilizadas
* **Backend:** Python, FastAPI, SQLite3, Google Generative AI, Pytest.
* **Frontend:** React, TypeScript, Vite, CSS Vanilla.

## Pré-requisitos
* Python 3.9+
* Node.js 18+
* Chave de API do Google Gemini

## Como rodar o projeto

### 1. Configurando o Backend
Abra um terminal e navegue até a pasta `backend`:

```bash
cd backend
```

Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
# No Windows: venv\Scripts\activate
# No Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
```

Crie um arquivo .env na pasta backend e insira sua chave da API:

```bash
GEMINI_API_KEY=sua_chave_aqui
```

Inicialize o banco de dados (isso criará o estoque.db com dados iniciais):

```bash
python database.py
```

Inicie o servidor FastAPI:

```bash
uvicorn main:app --reload
```

A API estará rodando em http://localhost:8000.

### 2. Configurando o Frontend
Abra um novo terminal e navegue até a pasta `frontend`:

```bash
cd frontend
npm install
npm run dev
```

O frontend estará rodando (geralmente em http://localhost:5173). Abra o link no navegador para interagir com o chatbot.

### 3. Rodando os Testes (Pytest)
No terminal do backend, com o ambiente virtual ativado, rode:

```bash
pytest test_main.py -v
```