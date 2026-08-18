# API Connect

API REST desenvolvida para cadastrar, listar e consultar usuários. O projeto foi criado como um MVP de back-end, utilizando armazenamento temporário em memória.

## Tecnologias utilizadas

- Python 3
- Flask
- Flask Blueprint
- python-dotenv
- Git e GitHub
- JSON para troca de dados

## Estrutura do projeto

```text
aula 1/
├── controllers/
│   ├── __init__.py
│   └── connect_controller.py
├── data/
│   ├── __init__.py
│   └── connect_data.py
├── routes/
│   ├── __init__.py
│   └── connect_routes.py
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## Pré-requisitos

Antes de iniciar, instale:

- Python 3
- Git

## Instalação e execução local

### 1. Clone o repositório

```bash
git clone https://github.com/kelvin587-12/api-connect-kelvin-almeida.git
```

Entre na pasta do projeto:

```bash
cd api-connect-kelvin-almeida
```

### 2. Crie o ambiente virtual

No Windows PowerShell:

```powershell
py -m venv .venv
```

### 3. Ative o ambiente virtual

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instale as dependências

```powershell
python -m pip install -r requirements.txt
```

### 5. Inicie a aplicação

```powershell
python app.py
```

A API ficará disponível em:

```text
http://127.0.0.1:5000
```

## Endpoints

| Método | URL | Descrição | Corpo da requisição |
|---|---|---|---|
| `GET` | `/` | Verifica se a API está funcionando | Não possui |
| `POST` | `/users` | Cadastra um usuário | `name` e `email` |
| `GET` | `/users` | Lista todos os usuários | Não possui |
| `GET` | `/users/<user_id>` | Consulta um usuário pelo ID | Não possui |

## Exemplos de utilização

### Verificar o funcionamento da API

```http
GET /
```

Resposta com status `200 OK`:

```json
{
  "status": "success",
  "message": "API Connect está funcionando."
}
```

### Cadastrar um usuário

```http
POST /users
Content-Type: application/json
```

Corpo da requisição:

```json
{
  "name": "Maria Silva",
  "email": "maria@email.com"
}
```

Resposta com status `201 Created`:

```json
{
  "data": {
    "id": 1,
    "name": "Maria Silva",
    "email": "maria@email.com"
  }
}
```

Se o nome não for informado, a API retornará `400 Bad Request`:

```json
{
  "error": "O campo name é obrigatório."
}
```

Se o e-mail não for informado, a API retornará `400 Bad Request`:

```json
{
  "error": "O campo email é obrigatório."
}
```

### Listar usuários

```http
GET /users
```

Resposta com status `200 OK`:

```json
{
  "data": [
    {
      "id": 1,
      "name": "Maria Silva",
      "email": "maria@email.com"
    }
  ]
}
```

### Consultar um usuário pelo ID

```http
GET /users/1
```

Resposta com status `200 OK`:

```json
{
  "data": {
    "id": 1,
    "name": "Maria Silva",
    "email": "maria@email.com"
  }
}
```

Quando o usuário não existe, a resposta possui status `404 Not Found`:

```json
{
  "error": "Usuário não encontrado."
}
```

## Testes e validação

Com a aplicação em execução, abra no navegador:

```text
http://127.0.0.1:5000/
```

Para listar os usuários:

```text
http://127.0.0.1:5000/users
```

O cadastro pode ser testado com Postman, Insomnia ou outra ferramenta de requisições HTTP, utilizando:

- Método: `POST`
- URL: `http://127.0.0.1:5000/users`
- Cabeçalho: `Content-Type: application/json`
- Corpo:

```json
{
  "name": "Maria Silva",
  "email": "maria@email.com"
}
```

## Observação

Os dados são armazenados temporariamente em uma lista na memória. Por isso, todos os usuários cadastrados são apagados quando o servidor é encerrado ou reiniciado.

## Autoria

Desenvolvido por kelvin.