# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### Documentation Example

`GET '/api/v1.0/get-categories'`
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.
```json
{
    "success": True,
    "categories": [
      {
          "id": 1,
          "type": "Science"
      },
      {
          "id": 2,
          "type": "Art"
      },
      {
          "id": 3,
          "type": "Geography"
      },
      {
          "id": 4,
          "type": "History"
      },
      {
          "id": 5,
          "type": "Entertainment"
      },
      {
          "id": 6,
          "type": "Sports"
      }
    ],
}
```

`GET '/api/v1.0/get-questions?page=1'`
- Request Arguments: page=1
- Returns: An object with `categories`, `current_category`, `questions`, `total_questions`, `success`.
```json
{
    "categories": [
        {
            "id": 1,
            "type": "Science"
        },
    ],
    "current_category": "",
    "questions": [
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
    ],
    "success": true,
    "total_questions": 1
}
```


`GET '/api/v1.0/delete-question/1'`
- Request Arguments: id
- Returns: An object with `result`, message success.
```json
{
  "result": "Delete question successfully"
}


`GET '/api/v1.0/create-questions'`
- Request Arguments:
  {
    "question": "Which country won the first ever soccer World Cup in 1930?",
    "answer": "Uruguay",
    "difficulty": "4",
    "category": "5"
  }
- Returns: An object with `response`, message success.
```json
{
  "response": "Created successfully"
}


`GET '/api/v1.0/search-questions'`
- Request Arguments: searchTerm = "question-name"
- Returns: An object
```json
{
    "categories": [
      {
          "id": 1,
          "type": "Science"
      },
      {
          "id": 2,
          "type": "Art"
      },
      {
          "id": 3,
          "type": "Geography"
      },
      {
          "id": 4,
          "type": "History"
      },
      {
          "id": 5,
          "type": "Entertainment"
      },
      {
          "id": 6,
          "type": "Sports"
      }
    ],
    "current_category": "",
    "questions": [
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        }
    ],
    "success": true,
    "total_questions": 1
}
```

`GET '/api/v1.0/categories/3/question'`
- Request Arguments: id (category)
- Returns: An object
```json
{
    "current_category": "Geography",
    "questions": [
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
    ],
    "success": true,
    "total_questions": 1
}


`GET '/api/v1.0/quizzes'`
- Request Arguments: 
{
  "previous_questions": [11,13],
  "quiz_category": 1
}
- Returns: An object
```json
{
    "force_end": false,
    "question": {
        "answer": "The Liver",
        "category": 1,
        "difficulty": 4,
        "id": 20,
        "question": "What is the heaviest organ in the human body?"
    }
}

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
