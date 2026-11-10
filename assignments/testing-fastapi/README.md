# 📘 Assignment: Testes Automatizados para FastAPI

## 🎯 Objective

Pratique testes automatizados com `pytest` em uma API FastAPI. Use `TestClient` para verificar respostas de sucesso, erros e validação sem iniciar um servidor, mantendo os dados de cada teste isolados.

## 📝 Tasks

### 🛠️ Executar e Entender o Teste Inicial

#### Descrição
Instale as dependências e execute o teste de exemplo fornecido. Observe como `TestClient` envia uma requisição diretamente à aplicação e como a fixture reinicia a coleção de livros antes e depois de cada teste.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install fastapi pytest httpx2`
- Executar os testes com `python -m pytest -q`
- Explicar o que o teste inicial verifica e por que os dados são reiniciados

### 🛠️ Testar Consultas, Criação e Validação

#### Descrição
Amplie `test_books.py` para verificar as operações de leitura e criação da API. Confira os códigos HTTP e os dados recebidos, incluindo as respostas para um livro inexistente e para uma requisição sem um campo obrigatório.

#### Requisitos
O programa concluído deve:

- Verificar que `GET /books` retorna status `200` e os livros existentes
- Verificar que `GET /books/{book_id}` retorna o livro solicitado
- Verificar que `POST /books` cria um livro e retorna status `201`
- Verificar status `404` para uma consulta de livro inexistente
- Verificar status `422` quando a criação não contém o título obrigatório

### 🛠️ Testar Atualização, Remoção e Isolamento

#### Descrição
Adicione testes para atualizar e remover livros. Inclua casos em que o ID não existe e execute a suíte completa para confirmar que os testes não dependem da ordem em que são executados.

#### Requisitos
O programa concluído deve:

- Verificar que `PUT /books/{book_id}` atualiza os dados de um livro
- Verificar que `DELETE /books/{book_id}` remove o livro
- Verificar status `404` ao tentar atualizar ou remover um livro inexistente
- Passar quando executado com `python -m pytest -q`, sem depender de outro teste ter sido executado antes