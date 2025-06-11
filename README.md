
-----



````markdown
# Desafio Desenvolvedor - API de Instrumentos Financeiros

![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-green.svg)
![Docker](https://img.shields.io/badge/Docker-25%2B-blue.svg)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)

Este repositório contém a solução para o **Desafio de Desenvolvedor da Oliveira Trust**. O projeto consiste em uma API RESTful para processar, armazenar e consultar dados de instrumentos financeiros, com base nos arquivos disponibilizados pela B3.

A aplicação foi desenvolvida em Python, utilizando o framework FastAPI, e estruturada com foco em **Clean Code** e **Clean Architecture**, visando a manutenibilidade, testabilidade e separação de responsabilidades. O ambiente é totalmente containerizado com Docker para garantir consistência e facilidade no setup.

## ✨ Principais Funcionalidades

- **Upload de Arquivos:** Endpoint para receber arquivos nos formatos `.csv` e `.xlsx`. Possui uma trava para impedir o processamento do mesmo arquivo (baseado no conteúdo) mais de uma vez.
- **Histórico de Uploads:** Endpoint que permite consultar os arquivos que já foram processados, com filtros por nome e data de upload.
- **Busca de Instrumentos:** Endpoint robusto para consultar os dados dos instrumentos, permitindo filtros por `TckrSymb` e `RptDt`. Caso nenhum filtro seja aplicado, o resultado é paginado.

## 🏛️ Arquitetura do Projeto

Para garantir um código desacoplado e organizado, a aplicação segue os princípios da **Arquitetura Limpa (Clean Architecture)**. As responsabilidades são divididas em camadas:

- **`src/domain`**: A camada mais interna. Contém as entidades de negócio e as regras puras.
- **`src/application`**: Contém os casos de uso que orquestram o fluxo de dados.
- **`src/infrastructure`**: A camada mais externa. Contém os detalhes de implementação (FastAPI, SQLAlchemy, etc.).

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Framework da API:** FastAPI
- **Processamento de Dados:** Pandas & OpenPyXL
- **Banco de Dados:** SQLite (via SQLAlchemy Core)
- **Containerização:** Docker & Docker Compose
- **Servidor ASGI:** Uvicorn

## 🚀 Como Executar o Projeto

Existem duas formas de executar a aplicação. A maneira com Docker é a mais recomendada por ser mais simples e garantir um ambiente consistente.

### Opção 1: Com Docker (Recomendado)

Esta abordagem garante que você não precise se preocupar com versão do Python ou dependências.

**Pré-requisitos:**
- Docker
- Docker Compose

**Execução:**
Na raiz do projeto, execute o seguinte comando:
```bash
docker compose up --build
````

Isso irá construir a imagem Docker e iniciar o contêiner da aplicação. A API estará disponível em `http://127.0.0.1:8000`.

Para parar a aplicação, pressione `Ctrl + C` no terminal e depois execute `docker compose down` para remover os contêineres.

### Opção 2: Localmente (Sem Docker)

**Pré-requisitos:**

  - Git
  - Python 3.12 ou superior

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd desafio-desenvolvedor
    ```
2.  **Crie e ative um ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Inicie o servidor:**
    ```bash
    uvicorn main:app --reload
    ```

A API estará disponível em `http://127.0.0.1:8000`.

## 📚 Documentação e Uso da API

A documentação interativa da API é gerada automaticamente pelo FastAPI e pode ser acessada em:

  * **Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)

Nesta página, é possível visualizar todos os endpoints e testá-los diretamente pelo navegador.

### Exemplos de Uso com `curl`

#### 1\. Upload de Arquivo

```bash
curl -X POST -F "file=@/caminho/para/seu/teste.csv" [http://127.0.0.1:8000/api/upload](http://127.0.0.1:8000/api/upload)
```

#### 2\. Consultar Histórico de Uploads

```bash
curl -X GET "[http://127.0.0.1:8000/api/history?filename=teste.csv](http://127.0.0.1:8000/api/history?filename=teste.csv)"
```

#### 3\. Buscar Conteúdo dos Arquivos

```bash
curl -X GET "[http://127.0.0.1:8000/api/instruments?TckrSymb=AMZO34&RptDt=2025-06-11](http://127.0.0.1:8000/api/instruments?TckrSymb=AMZO34&RptDt=2025-06-11)"
```

## ⭐ Possíveis Melhorias (Bônus)

Para demonstrar conhecimento em tecnologias adicionais e escalabilidade, as seguintes melhorias podem ser implementadas:

  - **Filas (Celery & Redis):** Mover o processamento de arquivos para uma tarefa assíncrona.
  - **Cache (Redis):** Implementar um cache para as consultas mais frequentes.
  - **Testes Automatizados (`pytest`):** Adicionar testes unitários e de integração para garantir a qualidade do código.
  - **Banco de Dados NoSQL (MongoDB):** Migrar a persistência dos dados para um banco de dados orientado a documentos.
  - **Autenticação (JWT):** Proteger os endpoints da API utilizando tokens JWT.

-----

Feito por **[Gabriell Maia do Amaral Duarte]**

  * **LinkedIn:** [https://www.linkedin.com/in/biellmaaia/](https://www.google.com/search?q=https://www.linkedin.com/in/biellmaaia/)
  * **GitHub:** [https://github.com/maia2a](https://www.google.com/search?q=https://github.com/maia2a)

<!-- end list -->
