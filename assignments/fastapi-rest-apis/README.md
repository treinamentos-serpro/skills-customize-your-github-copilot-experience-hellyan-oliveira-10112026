# 📘 Assignment: Criando APIs REST com FastAPI

## 🎯 Objective

Crie uma API REST para gerenciar uma coleção de livros usando FastAPI. Pratique métodos HTTP, URLs de recursos, validação de requisições e o uso adequado de códigos de status.

## 📝 Tasks

### 🛠️ Criar a API e Consultar Livros

#### Descrição
Instale FastAPI e Uvicorn com `pip install fastapi uvicorn`. Use o código inicial fornecido para configurar a aplicação e implementar endpoints para listar livros e consultar um livro pelo ID. Inicie o servidor com `uvicorn starter-code:app --reload` e explore a documentação interativa da API em `/docs`.

#### Requisitos
O programa concluído deve:

- Disponibilizar uma aplicação FastAPI
- Retornar todos os livros em `GET /books`
- Retornar um livro em `GET /books/{book_id}`
- Retornar o código de status `404` quando o livro solicitado não existir

### 🛠️ Adicionar Livros com Validação

#### Descrição
Implemente um endpoint para adicionar um livro. Use o modelo Pydantic fornecido para validar os dados recebidos e atribua um ID único a cada novo livro.

#### Requisitos
O programa concluído deve:

- Aceitar um novo livro por meio de `POST /books`
- Validar o título e o autor do livro usando o modelo fornecido
- Atribuir e retornar um ID único para o novo livro
- Retornar o código de status `201` quando um livro for criado

### 🛠️ Atualizar e Remover Livros

#### Descrição
Complete a API adicionando endpoints para substituir os dados de um livro e removê-lo pelo ID. Teste cada endpoint em `/docs` e confira tanto as respostas de sucesso quanto as respostas para recursos não encontrados.

#### Requisitos
O programa concluído deve:

- Atualizar um livro por meio de `PUT /books/{book_id}`
- Remover um livro por meio de `DELETE /books/{book_id}`
- Retornar o código de status `404` quando uma atualização ou remoção buscar um livro inexistente
- Demonstrar o fluxo completo de criação, consulta, atualização e remoção