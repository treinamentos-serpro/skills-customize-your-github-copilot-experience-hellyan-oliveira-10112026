# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing a collection of books with FastAPI. Practice HTTP methods, resource URLs, request validation, and appropriate status codes.

## 📝 Tasks

### 🛠️ Create the API and Read Books

#### Description
Install FastAPI and Uvicorn with `pip install fastapi uvicorn`. Use the provided starter code to create the application and implement endpoints for listing books and retrieving one book by its ID. Run the server with `uvicorn starter-code:app --reload` and explore the interactive API documentation at `/docs`.

#### Requirements
The completed program must:

- Create a FastAPI application
- Return all books from `GET /books`
- Return one book from `GET /books/{book_id}`
- Return status code `404` when the requested book does not exist

### 🛠️ Add Books with Validated Requests

#### Description
Implement an endpoint for adding a book. Use the provided Pydantic model to validate incoming data, and assign each new book a unique ID.

#### Requirements
The completed program must:

- Accept a new book through `POST /books`
- Validate the book's title and author using the provided model
- Assign and return a unique ID for the new book
- Return status code `201` when a book is created

### 🛠️ Update and Remove Books

#### Description
Complete the API by adding endpoints to replace a book's details and remove a book by ID. Try each endpoint in `/docs` and check both successful and not-found responses.

#### Requirements
The completed program must:

- Update a book through `PUT /books/{book_id}`
- Remove a book through `DELETE /books/{book_id}`
- Return status code `404` when an update or deletion targets a missing book
- Demonstrate the full create, read, update, and delete workflow