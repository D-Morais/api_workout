# WorkoutAPI — API Assíncrona para Gestão de Competição de Crossfit

Uma API moderna, rápida e escalável construída com FastAPI, utilizando arquitetura limpa, SQLAlchemy assíncrono, Pydantic v2 e Alembic para versionamento do banco.

O objetivo da WorkoutAPI é gerenciar atletas, categorias e centros de treinamento para uma competição de crossfit.

## 🚀 Tecnologias Utilizadas

Este projeto utiliza a seguinte stack:

FastAPI (async) → criação da API

SQLAlchemy 2.0 (async) → ORM assíncrono

Alembic → migrações do banco

Pydantic v2 → validação de dados

SQLite (default)

PostgreSQL (opcional via Docker)
<br>    
📁 Estrutura do Projeto<br>
workout_api/<br>
│<br>
├── alembic/                  # Migrations geradas automaticamente<br>
│<br>
├── app/<br>
│   ├── core/<br>
│   │   ├── config.py         # Configurações gerais do projeto<br>
│   │   └── database.py       # Conexão assíncrona com banco<br>
│   │<br>
│   ├── models/               # Modelos ORM (SQLAlchemy)<br>
│   │   ├── atleta_model.py<br>
│   │   ├── categoria_model.py<br>
│   │   └── centro_treinamento_model.py<br>
│   │<br>
│   ├── schemas/              # Schemas (Pydantic)<br>
│   │   ├── atleta_schema.py<br>
│   │   ├── categoria_schema.py<br>
│   │   └── centro_treinamento_schema.py<br>
│   │<br>
│   ├── routers/              # Rotas da API<br>
│   │   ├── atleta_router.py<br>
│   │   ├── categoria_router.py<br>
│   │   └── centro_treinamento_router.py<br>
│   │<br>
│   └── main.py               # Ponto de entrada da aplicação<br>
│<br>
├── alembic.ini<br>
├── requirements.txt<br>
└── README.md<br>
<br>

##🧬 Modelagem de Entidades
🧍 Atleta

Campo	Tipo

pk_id	int (PK)

nome	varchar(50)

cpf	varchar(11)

idade	int

peso	float

altura	float

sexo	varchar(1)

centro_treinamento_id	FK

categoria_id	FK

🏷 Categoria

Campo	Tipo

pk_id	int (PK)

nome	varchar(10)


🏋️ Centro de Treinamento

Campo	Tipo

pk_id	int (PK)

nome	varchar(20)

endereco	varchar(60)

proprietario	varchar(30)


##🛠 Instalação do Projeto
1️⃣ Clonar o repositório

git clone https://github.com/D-Morais/api_workout.git

cd workout_api

2️⃣ Criar ambiente virtual

python -m venv venv

source venv/bin/activate          # Linux/Mac

venv\Scripts\activate             # Windows

3️⃣ Instalar dependências

pip install -r requirements.txt


🗄 Configuração do Banco de Dados

O projeto usa SQLite por padrão.

Se quiser usar PostgreSQL via Docker, você poderá configurar no config.py.


##🧬 Rodando as Migrações

Criar primeira migração (apenas uma vez):

alembic revision --autogenerate -m "create tables"


Executar as migrações:

alembic upgrade head

▶️ Rodando a API

uvicorn app.main:app --reload


A API estará acessível em:

📍 http://localhost:8000

Documentação automática:

📘 Swagger UI → http://localhost:8000/docs

📗 Redoc → http://localhost:8000/redoc

📡 Exemplos de Requisições

<br>
➕ Criar um Atleta
POST /atletas/

{
  "nome": "João Silva",
  "cpf": "12345678901",
  "idade": 29,
  "peso": 82.5,
  "altura": 1.78,
  "sexo": "M",
  "centro_treinamento_id": 1,
  "categoria_id": 2
}

<br>
🔍 Listar categorias

GET /categorias/

<br>
🏋️ Criar Centro de Treinamento

POST /centros/

{
  "nome": "CT IronBox",
  "endereco": "Rua dos Atletas, 123",
  "proprietario": "Carlos Almeida"
}

