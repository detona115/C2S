[![GitHub license](https://img.shields.io/badge/implemented%20by-Andy-blue)](https://www.linkedin.com/in/andy-kiaka-76a983110/)

# C2S


## Sumário

- [C2S](#c2s)
  - [Sumário](#sumário)
  - [Introdução](#introdução)
  - [Funcionalidades](#funcionalidades)
  - [Modelagem de Dados](#modelagem-de-dados)
  - [Arquitetura e Organização](#arquitetura-e-organização)
  - [Instalação e Setup](#instalação-e-setup)
    - [Pré-requisitos](#pré-requisitos)
    - [Instalação](#instalação)
  - [Como Rodar](#como-rodar)
    - [Servidor FastAPI](#servidor-fastapi)
    - [Agente Virtual (Terminal)](#agente-virtual-terminal)
    - [Build e execução do servidor via Docker (Opcional)](#build-e-execução-do-servidor-via-docker-opcional)
    - [Agente Virtual no Docker (Terminal)](#agente-virtual-no-docker-terminal)
  - [API (Protocolo MCP)](#api-protocolo-mcp)
  - [Agente Virtual no Terminal](#agente-virtual-no-terminal)
  - [Testes Automatizados](#testes-automatizados)
  - [Considerações Técnicas](#considerações-técnicas)
  - [Contato](#contato)

---

## Introdução

Este projeto é uma aplicação FastAPI para consulta de automóveis, com comunicação via protocolo MCP e interface de agente virtual no terminal. 

---

## Funcionalidades

- Consulta de veículos com múltiplos filtros (marca, modelo, ano, combustível, preço, etc.)
- Banco de dados populado automaticamente com dados fictícios realistas
- API robusta e validada via FastAPI + Pydantic
- Protocolo MCP para comunicação client-server
- Agente virtual interativo no terminal (CLI)
- Testes automatizados para API e agente

---

## Modelagem de Dados

- **Carro (Car):**
  - id (UUID)
  - marca
  - modelo
  - ano
  - motorização
  - tipo_combustivel
  - cor
  - quilometragem
  - numero_portas
  - transmissao
  - preco
  - placa
  - data_cadastro

---

## Arquitetura e Organização

```
C2S/
│
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── database.py       # DB setup
│   ├── crud.py           # CRUD operations
│   ├── seed.py           # Script para popular o banco
│   └── mcp.py            # Lógica do protocolo MCP
│
├── agent/
│   └── agent_cli.py      # Agente virtual no terminal
│
├── tests/
│   ├── test_api.py
│   └── test_agent.py
│
├── requirements.txt
├── README.md
└── .env.example
```

- **Separação de responsabilidades:** Models, Schemas, CRUD, Seed, MCP, CLI, Testes
- **Padrões modernos:** Dependency Injection, Lifespan, Pydantic v2, SQLAlchemy

---

## Instalação e Setup

### Pré-requisitos

- Python 3.10+

### Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/detona115/C2S.git
   cd C2S
   ```
2. Crie e ative o ambiente virtual:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Popule o banco de dados:
   ```sh
   python -m app.seed
   ```

---

## Como Rodar

### Servidor FastAPI

```sh
uvicorn app.main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

### Agente Virtual (Terminal)

Em outro terminal:

```sh
python agent/agent_cli.py
```

### Build e execução do servidor via Docker (Opcional)

 ```sh
docker build -t c2s-app .
docker run --rm -p 8000:8000 c2s-app
```

### Agente Virtual no Docker (Terminal)
Em outro terminal:

```sh
docker exec -it <container_id> python agent/agent_cli.py
```

---

## API (Protocolo MCP)

- **Endpoint:** `POST /mcp/query`
- **Payload:** JSON com filtros (marca, modelo, ano, tipo_combustivel, cor, transmissao, preco_min, preco_max)
- **Resposta:** Lista de veículos compatíveis (campos: marca, modelo, ano, cor, quilometragem, preço, etc)

Exemplo de payload:

```json
{
  "marca": "Fiat",
  "ano": 2020,
  "tipo_combustivel": "Flex",
  "preco_min": 30000,
  "preco_max": 60000
}
```

NB: É preferível fornecer o menor número de filtros possível para evitar filtros muito explicitos, pois a base de dados é pequena e fake.

Ex: marca Fiat, modelo Uno.

---

## Agente Virtual no Terminal

- Interface conversacional (não menu fixo)
- Coleta filtros de forma natural
- Envia consulta via MCP para o servidor
- Exibe resultados amigáveis (marca, modelo, ano, cor, km, preço)

---

## Testes Automatizados

- Testes de API (`tests/test_api.py`)
- Testes do agente CLI (`tests/test_agent.py`)
- Execute:

```sh
python -m pytest
```

---

## Considerações Técnicas

- **Pydantic v2:** Uso de `ConfigDict(from_attributes=True)` para compatibilidade
- **FastAPI Lifespan:** Inicialização do banco via contexto lifespan
- **SQLAlchemy:** ORM robusto e performático
- **Faker:** Dados realistas para seed
- **Prompt Toolkit:** CLI moderna e amigável
- **Testabilidade:** Separação clara de camadas e testes automatizados

---

## Contato

Dúvidas ou sugestões? [LinkedIn - Andy Kiaka](https://www.linkedin.com/in/andy-kiaka-76a983110/)
