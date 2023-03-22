# Bookstore

This is a simple bookstore application that allows you to create, read, update and delete books.

To run the application locally:

```shell
uvicorn bookstore.main:app --reload

or

uvicorn bookstore.main:app --reload --port 8080
```

Or run application with gunicorn:

```shell
gunicorn -w 4 --worker-class uvicorn.workers.UvicornWorker --bind :9000 bookstore.main:app
```

## Run Tests

```shell
pytest
```