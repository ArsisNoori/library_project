# Library Management API

A RESTful API for managing books, built with **Django** and **Django REST Framework**.

## Features

* CRUD operations for books
* ModelViewSet
* DefaultRouter
* Search books by:

  * Title
  * Author
  * ISBN
* Ordering by:

  * Price
  * Published Year
  * Pages

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

## API Endpoints

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| GET    | `/api/books/`      | List all books    |
| POST   | `/api/books/`      | Create a new book |
| GET    | `/api/books/{id}/` | Retrieve a book   |
| PUT    | `/api/books/{id}/` | Update a book     |
| DELETE | `/api/books/{id}/` | Delete a book     |

## Search

Example:

```
GET /api/books/?search=python
```

## Ordering

Examples:

```
GET /api/books/?ordering=price
```

```
GET /api/books/?ordering=-price
```

## Project Status

This project is currently under development.

### Planned Features

* Filtering
* Pagination
* JWT Authentication
* Permissions
* Image Upload
* Nested Serializers
* Query Optimization

## Author

Arsis Noori
