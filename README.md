# A FastAPI App

## Retrieve all the data
curl http://localhost:8000/todos/

## Upload new todos

curl -X POST http://localhost:8000/todos/ \
-H 'Content-Type: application/json' \
--data '{"title": "Third Addition", "description": "The Desc", "completed": false}'}'
