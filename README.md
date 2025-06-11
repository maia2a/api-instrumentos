

# Desafio Desenvolvedor - API de Instrumentos Financeiros

Este repositório contém a solução para o **Desafio de Desenvolvedor da Oliveira Trust**. O projeto consiste em uma API RESTful para processar, armazenar e consultar dados de instrumentos financeiros, com base nos arquivos disponibilizados pela B3.

A aplicação foi desenvolvida em Python, utilizando o framework FastAPI, e estruturada com foco em **Clean Code** e **Clean Architecture**, visando a manutenibilidade, testabilidade e separação de responsabilidades.

## ✨ Principais Funcionalidades

  - **Upload de Arquivos:** Endpoint para receber arquivos nos formatos `.csv` e `.xlsx`. Possui uma trava para impedir o processamento do mesmo arquivo (baseado no conteúdo) mais de uma vez.
  - **Histórico de Uploads:** Endpoint que permite consultar os arquivos que já foram processados, com filtros por nome e data de upload.
  - **Busca de Instrumentos:** Endpoint robusto para consultar os dados dos instrumentos, permitindo filtros por `TckrSymb` e `RptDt`. Caso nenhum filtro seja aplicado, o resultado é paginado.

## 🏛️ Arquitetura do Projeto

Para garantir um código desacoplado e organizado, a aplicação segue os princípios da **Arquitetura Limpa (Clean Architecture)**. As responsabilidades são divididas em camadas:

  - **`src/domain`**: A camada mais interna. Contém as entidades de negócio (`Instrument`, `UploadHistory`) e as regras de negócio puras, sem depender de frameworks ou banco de dados.
  - **`src/application`**: Contém os casos de uso da aplicação, que orquestram o fluxo de dados entre as camadas. É aqui que a lógica da aplicação reside (ex: `processar_upload`, `buscar_instrumentos`).
  - **`src/infrastructure`**: A camada mais externa. Contém os detalhes de implementação, como o servidor web (FastAPI), a lógica de acesso ao banco de dados (SQLAlchemy) e outras ferramentas externas.

Essa estrutura torna a aplicação mais resiliente a mudanças e mais fácil de testar.

## 🚀 Tecnologias Utilizadas

  - **Linguagem:** Python 3.12+
  - **Framework da API:** FastAPI
  - **Processamento de Dados:** Pandas
  - **Banco de Dados:** SQLite (via SQLAlchemy Core para simplicidade e portabilidade)
  - **Servidor ASGI:** Uvicorn
  - **Validação de Dados:** Pydantic

## ⚙️ Configuração do Ambiente

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos

  - Git
  - Python 3.12 ou superior
  - `venv` (geralmente incluído no Python)

### Passos para Instalação

1.  **Clone o repositório:**

    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd desafio-desenvolvedor
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    # Criar o ambiente
    python3 -m venv venv

    # Ativar no Linux/macOS/WSL
    source venv/bin/activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Executando a Aplicação

Com o ambiente virtual ativado e as dependências instaladas, inicie o servidor com o seguinte comando:

```bash
uvicorn main:app --reload
```

  - `--reload`: Faz com que o servidor reinicie automaticamente após qualquer alteração no código.

A API estará disponível em `http://127.0.0.1:8000`.

## 📚 Documentação e Uso da API

A documentação interativa da API é gerada automaticamente pelo FastAPI e pode ser acessada em:

  * **Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)

Nesta página, é possível visualizar todos os endpoints e testá-los diretamente pelo navegador.

### Exemplos de Uso com `curl`

#### 1\. Upload de Arquivo

```bash
curl -X POST -F "file=@/caminho/para/seu/teste.csv" http://127.0.0.1:8000/api/upload
```

> **Nota:** Substitua `/caminho/para/seu/teste.csv` pelo caminho real do arquivo que deseja enviar.

#### 2\. Consultar Histórico de Uploads

```bash
# Buscar todo o histórico
curl -X GET http://127.0.0.1:8000/api/history

# Filtrar por nome do arquivo
curl -X GET "http://127.0.0.1:8000/api/history?filename=teste.csv"
```

#### 3\. Buscar Conteúdo dos Arquivos

```bash
# Busca geral paginada
curl -X GET http://127.0.0.1:8000/api/instruments

# Busca filtrando por Ticker Symbol
curl -X GET "http://127.0.0.1:8000/api/instruments?TckrSymb=AMZO34"

# Busca combinando Ticker e Data
curl -X GET "http://127.0.0.1:8000/api/instruments?TckrSymb=AMZO34&RptDt=2025-06-11"
```

## ⭐ Possíveis Melhorias (Bônus)

Para demonstrar conhecimento em tecnologias adicionais e escalabilidade, as seguintes melhorias podem ser implementadas:

  - **Containers (Docker):** Criar um `Dockerfile` e `docker-compose.yml` para facilitar o setup e garantir a portabilidade do ambiente.
  - **Filas (Celery & Redis):** Mover o processamento de arquivos para uma tarefa assíncrona, fazendo com que o endpoint de upload responda instantaneamente ao usuário.
  - **Cache (Redis):** Implementar um cache para as consultas mais frequentes no endpoint de busca, diminuindo a carga no banco de dados e o tempo de resposta.
  - **Banco de Dados NoSQL (MongoDB):** Migrar a persistência dos dados para um banco de dados orientado a documentos, que pode ser mais adequado para a natureza dos dados.
  - **Autenticação (JWT):** Proteger os endpoints da API utilizando tokens JWT.

-----

Feito por **Gabriell Maia do Amaral Duarte**

  * **LinkedIn:** [https://www.linkedin.com/in/biellmaaia/](https://www.google.com/search?q=https://www.linkedin.com/in/biellmaaia/)
  * **GitHub:** [https://github.com/maia2a](https://www.google.com/search?q=https://github.com/maia2a)
